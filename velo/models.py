from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from math import *



class Player(models.Model):




    CTX_GEO_LIB = ((4.9, 'Centre ville ou urbain'),(1.7, 'Périurbain'),(1.5, 'Rural'),(2.2, 'Moyenne nationale'),) # suprimer moyenne nationale
    ACC_LIB = (('bonne','bonne' ),('moyenne','moyenne'),('mauvaise','mauvaise'))
    FREQF_LIB = ((5, 'moins de 1 jour'),(15, '1 jour'),(35, '2 jours'),(65, '3 jours'),(80, '4 jours'),(100, '5 jours'),)

    MG1=((2, 'Réticent'),(25, 'Non sensibilisé'),(45, 'Sensibilisé'),(75, 'Motivé'),(100, 'Impliqué et acteur'),)
    MG2=((10, 'Réfractaire aux vélos'),(25, 'Sensibilisé mais pas confiant'),(45, 'Usager ponctuel pour le loisir'),(75, 'Usager quotidien'),(100, 'Cycliste expert'),)
    MG3=((10, 'Pas acté'),(50, 'Démarche en cours'),(100, 'Démarche lancée'),)
    MG4=((10, 'Aucune action envisagée'),(50, 'Actions vélos en réflexion'),(100, 'Actions vélos mises en place'),) 



    entrep = models.CharField(default = 'votre entreprise', max_length=250,verbose_name = "Le nom de votre entreprise",)
    nom = models.CharField(default = 'votre nom', max_length=250,verbose_name = "votre nom",)
    adresse = models.CharField(max_length=250,verbose_name = "Votre adresse",)
    ville = models.CharField(max_length=250,verbose_name = "Votre ville",)
    #mail = models.EmailField()

    nbsal = models.PositiveIntegerField(verbose_name = "Nombre de salariés",)
    freq = models.IntegerField(default=65,choices=FREQF_LIB,verbose_name = "fréquence d'utilisation")
    #freq = models.PositiveIntegerField(default = 65, validators=[MinValueValidator(0), MyMaxValueValidator(100,"The value should be lesser than %(limit_value)s.")], verbose_name = "Fréquence moyenne de la pratique des cyclistes (en pourcentage de jours travaillés)",)
    dist = models.IntegerField(default = 3, verbose_name = "Distance Domicile travail moyenne des cyclistes de votre entreprise",)
    access = models.CharField(default='Bonne',choices=ACC_LIB,verbose_name = "Accessibilite du site",max_length=10)
    ctxgeolib = models.FloatField(choices=CTX_GEO_LIB,default='Centre-ville',verbose_name = "Contexte geographique")

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

    def pvelo(self):
        """Calcul du potentiel vélo avec une part modale mini de 3% et un part modale maxi de 30 %
        selon la fonction y = 31.177.x-2.4684"""
        pm = 34.177*self.score()-2.4684        
        self.reusite =(self.nbsal /100 * pm)
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
        self.evocycl = self.pvelo()*(1+0.5) 
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

    	# plafond à 200
    	p = 200 
		# Distance pour atteindre les 200
    	kmp = 0 
    	if p > 200:
    		kmp = 200/0.25
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