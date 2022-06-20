from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from math import *
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor



class Player(models.Model):




    CTX_GEO_LIB = ((4.9, 'Centre ville ou urbain'),(1.7, 'Périurbain ou zone d\'activités'),(1.5, 'Rural'),) # suprimer moyenne nationale
    ACC_LIB = ((3,'Bonne' ),(2,'Moyenne'),(1,'Mauvaise'))
    FREQF_LIB = ((5, 'moins de 1 jour'),(15, '1 jour'),(35, '2 jours'),(65, '3 jours'),(80, '4 jours'),(100, '5 jours'),)

    MG1=((2, 'Réticents'),(25, 'Non sensibilisés'),(45, 'Sensibilisés'),(75, 'Motivés'),(100, 'Impliqués et acteurs'),)
    MG2=((10, 'Réfractaires aux vélos'),(25, 'Sensibilisés mais pas confiants'),(45, 'Usagers ponctuels pour le loisir'),(75, 'Usagers au quotidien'),(100, 'Cyclistes experts'),)
    MG3=((10, 'Inexistant'),(50, 'En réflexion'),(100, 'Actif'),)
    MG4=((10, 'Aucune action envisagée'),(50, 'Actions vélos en réflexion'),(100, 'Actions vélos mises en place'),)

    PCY=((2, 'Moins de 3%'),(4,'Entre 3 et 5%'),(7, 'Entre 5 et 8%'),(15, 'Environ 15 %'),(25, 'Environ 25 %'),(50,'Plus de 25 %'),)



    entrep = models.CharField(max_length=250,verbose_name = "Le nom de votre entreprise",)
    nom = models.CharField( max_length=250,verbose_name = "votre nom",)
    #adresse = models.CharField(max_length=250,verbose_name = "Votre adresse",)
    ville = models.CharField( max_length=250,verbose_name = "Votre ville",)
    mail = models.EmailField(verbose_name = "Votre email",)

    nbsal = models.PositiveIntegerField(verbose_name = "Nombre de salariés",)
    pccycliste = models.PositiveIntegerField(choices=PCY,verbose_name = "Pourcentages cyclistes", default = '50',)
    freq = 65
    #freq = models.IntegerField(default=65,choices=FREQF_LIB,verbose_name = "fréquence d'utilisation")
    #freq = models.PositiveIntegerField(default = 65, validators=[MinValueValidator(0), MyMaxValueValidator(100,"The value should be lesser than %(limit_value)s.")], verbose_name = "Fréquence moyenne de la pratique des cyclistes (en pourcentage de jours travaillés)",)
    dist = models.IntegerField(default = 3, verbose_name = "Distance Domicile travail moyenne des cyclistes de votre entreprise",)
    access = models.IntegerField(default=3,choices=ACC_LIB,verbose_name = "Accessibilite du site")
    ctxgeolib = models.FloatField(choices=CTX_GEO_LIB,default='Centre-ville',verbose_name = "Contexte geographique")

    #PM = models.IntegerField(default = 0, verbose_name = "Part Modale vélo Attendue (Pour débugages)",)

    g1 = models.IntegerField(choices=MG1,verbose_name = "Motivation de la direction de l’entreprise")
    g2 = models.IntegerField(choices=MG2,verbose_name = "Motivation des salariés")
    g3 = models.IntegerField(choices=MG3,verbose_name = "Etat d'avancement du PDE")
    g4 = models.IntegerField(choices=MG4,verbose_name = "Actions vélo", default=50)

    published_date = models.DateTimeField(blank=True, null=True)
    

    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()nb


    def publish(self):
    	self.published_date = timezone.now()
    	self.save()

    def score(self):
        """Calcul du score global"""
        if self.ctxgeolib == '4.9':
            self.notegeo = 100
        elif self.ctxgeolib == '1.7':
            self.notegeo = 50
        elif self.ctxgeolib == '1.5':
            self.notegeo = 10
        else:
            self.notegeo = 65

        if self.access == "bonne":
            self.noteacces = 100
        elif self.access == "moyenne":
            self.noteacces = 50
        else:
            self.noteacces = 10

        self.notefreq = self.freq
        self.moy = ((self.notegeo + self.noteacces + self.notefreq +  self.g1 + self.g2 + self.g3 +self.g4 )/700) #+ self.g4
        return self.moy

    # def pvelo(self):
    #     """Calcul du potentiel vélo avec une part modale mini de 3% et un part modale maxi de 30 %
    #     selon la fonction y = 31.177.x-2.4684"""
    #     pm = 34.177*self.score()-2.4684        
    #     self.reusite =(self.nbsal /100 * pm)
    #     return ceil(self.reusite)

    def pvelo(self):
        """Prédiction de la part modale vélo potentielle"""
        # Charge les donnees de train dans panda
        features = pd.read_csv('MPM3/velo/train.csv', sep=';',)
        # One-hot encode categorical features
        features = pd.get_dummies(features)
        # Labels are the values we want to predict
        labels = np.array(features['PM'])
        # Remove the labels from the features
        # axis 1 refers to the columns
        features= features.drop('PM', axis = 1)
        # Saving feature names for later use
        feature_list = list(features.columns)

        # Convert to numpy array
        features = np.array(features)

        # Split the data into training and testing sets
        train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size = 0.05, random_state = 42)
        # Instantiate model 
        rf = RandomForestRegressor(n_estimators= 1000, 
                                    max_depth=None,
                                    min_samples_leaf=1,
                                    min_samples_split=5,)
        # Train the model on training data
        rf.fit(train_features, train_labels)
        # Use the forest's predict method on the test data
        predictions = rf.predict(test_features)
        # Calculate the absolute errors
        errors = abs(predictions - test_labels)
        # Calculate mean absolute percentage error (MAPE)
        mape = 100 * (errors / test_labels)

        # Calculate and display accuracy
        accuracy = 100 - np.mean(mape)
        print('Accuracy:', round(accuracy, 2), '%.')

        # Compile les features du player dans un dic

        

        pm = rf.predict([[self.nbsal,
                            self.access,
                            self.ctxgeolib,
                            self.pccycliste,
                            self.g1,
                            self.g2,
                            self.g3,
                            self.g4,
                            ]])
        
        print (self.nbsal,
                            self.access,
                            self.ctxgeolib,
                            self.pccycliste,
                            self.g1,
                            self.g2,
                            self.g3,
                            self.g4,
                            )

        self.reusite =(self.nbsal / 100*pm)
        return ceil(self.reusite)

    def paccess(self):
        """Calcul du coef de pondération Accessibilité"""
        if self.access == "bonne":
            self.pa = self.freq/100
        elif self.access == "moyenne":
            self.pa = self.freq/100*0.8
        else:
            self.pa = self.freq/100*0.6
        return self.pa

    def evocycliste(self):
        """fonction d'evaluation de l'evolution du nombre de cyclistes"""
        self.evocycl = self.pvelo()*(1+0.25) 
        self.evocycl = ceil(self.evocycl)
        return self.evocycl

    def evoar(self):
        """fonction d'evaluation du nombre de trajets DT"""
        self.evoar = self.evocycliste()*218*self.freq/100
        self.evoar = ceil(self.evoar)
        return self.evoar

    def evoarp(self):
        """fonction d'evaluation ponderee du nombre de trajets DT"""
        self.evoarp = self.evocycliste()*218*self.paccess()
        self.evoarp = ceil(self.evoarp)
        return self.evoarp

    def distance(self):
        """Fonction d'evaluation de la distance moyenne parcourue"""
        if self.ctxgeolib == '4.9':
            self.distance = 3 * self.evoarp
        elif self.ctxgeolib == '1.7':
            self.distance = 4 * self.evoarp
        elif self.ctxgeolib == '1.5':
            self.distance = 4 * self.evoarp
        else:
            self.distance = 5 * self.evoarp
        return self.distance

    def distanced(self):
        """Fonction d'evaluation de la distance moyenne parcourue pour l'affichage sur la liste de players. histoire de méthode ?????"""
        if self.ctxgeolib == '4.9':
            self.distance = 3 * self.evoarp()
        elif self.ctxgeolib == '1.7':
            self.distance = 4 * self.evoarp()
        elif self.ctxgeolib == '1.5':
            self.distance = 4 * self.evoarp()
        else:
            self.distance = 5 * self.evoarp()
        return self.distance

    def km(self):
        """Recuperation des distances moyennes selon le ctx geo"""
        if self.ctxgeolib == '4.9':
            self.m = 3
        elif self.ctxgeolib == '1.7':
            self.m = 4
        elif self.ctxgeolib == '1.5':
            self.m = 4
        else:
            self.m = 5
        return int(self.m)

    
    def coutdist(self):
        """Fonction dévaluation du cout hors plafond de l'ikv en tenant compte des distance pondéres"""
        self.cout = 2 * 0.25 * self.distance
        return int(self.cout)

    def distmoy(self):
    	self.i= 218*2*self.km()*self.freq/100
    	return self.i

    def coutpt(self):
    	"""Fonction d'estimation du cout plafonné"""

    	# calcul des paramètres :

    	# plafond à 500 € par mois
    	p = 500 
		# Distance pour atteindre les 500
    	kmp = 0 
    	if p > 500:
    		kmp = 500/0.25
    	else:
    		kmp = p/0.25
		# Distance réalisée hors plafond
    	kmhp = self.distmoy()-kmp
		# Budget en deçà du plafond
    	bpmoins = 0
    	if self.distmoy() < kmp:
    		bpmoins = self.distmoy()*0.25*self.evocycliste()
    	else:
    		bpmoins = kmp*0.25*self.evocycliste()
		# Budget au delà du plafond
    	bpplus = kmhp*0.43*self.evocycliste()
		# Somme (budget à la pratique)
    	bsum = bpplus+bpmoins
    	# Budget plafond
    	bp = p*self.evocycliste()

    	# calcul des validation :
    	vkmhp = p/0.25
    	vbpmoins = vkmhp-kmp
    	i = vbpmoins*0.43*self.evocycliste()
    	if i > 0:
    		vbpplus = i
    	else:
    		vbpplus = 0
    	vbsum = bpmoins +(self.cout-bpmoins)*0.43/0.25
    	vbp = vbpplus+bpmoins

    	# calcul final
    	if vbp>vbsum:
    		valid = vbsum
    	else:
    		valid = vbp
    	#retourn la valeur du cout plafonné
    	return ceil(valid)



    	




    def recodir(self):
        """Génération des recommendations auprès de la direction"""
        if (0 <= self.g1 <= 2):
            self.recog1 = '1' #"Actions de sensibilisation fortes à mettre en place auprès de la direction"
        elif(2 < self.g1 <= 75):
            self.recog1 = '2' # "Actions pour conforter la motivation de la direction"
        else:
            self.recog1 = '3'  #"Direction OK"
        return self.recog1

    def recosal(self):
        """Génération des recommendations auprès des salariés"""

        if (self.g2 == 10):
            self.recog2 = '1' #"Un playdoyer actif doit être mis en place auprès des salariés"
        elif(self.g2 == 25):
            self.recog2 = '2' #Il faut conforter la motivation de vos salariés. Mettre en place des actions d'information et sensibilisation ;  Remise en selle."
        elif (self.g2 == 45):
            self.recog2 = '3' #"Favoriser l'utilisation quotidienne du vélo, aménagements sur le site mise en place de l'IKV, Référent vélo"
                            
        else:
            self.recog2 = '4'
        return self.recog2

    def recopde(self):
        """Génération des recommendations en fonction de l'avancement du PDM"""
        if (self.g3 == 10):
            self.recog3 = '1'
        elif(self.g3 == 50):
            self.recog3 = '2'
        else:
            self.recog3 = '3'
        return self.recog3








    def __str__(self):
        return self.nom
