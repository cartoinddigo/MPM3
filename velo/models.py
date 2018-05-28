from django.db import models
from django.utils import timezone
from math import *



class Player(models.Model):

    # author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # title = models.CharField(max_length=200)
    # text = models.TextField()
    # created_date = models.DateTimeField(
    #         default=timezone.now)
    # published_date = models.DateTimeField(
    #         blank=True, null=True)


    CTX_GEO_LIB = ((4.9, 'Centre-ville'),(1.7, 'Banlieues'),(1.5, 'Rural'),(2.2, 'Moyenne nationale'),)
    ACC_LIB = (('bonne','bonne' ),('moyenne','moyenne'),('mauvaise','mauvaise'))

    MG1=((10, 'Réticent'),(25, 'Non sensibilisé '),(45, 'Sensibilisé'),(75, 'Motivé'),(100, 'Impliqué et acteur'),)
    MG2=((10, 'Réfractaire aux vélos'),(25, 'Sensibilisé mais apeuré'),(45, 'Usager ponctuel  pour le loisir'),(75, 'Usager quotidien'),(100, 'Cycliste expert'),)
    MG3=((10, 'Pas acté'),(25, 'Actions  vélos en réflexion'),(45, 'Actions vélos mises en place'),(75, 'Démarche en cours'),(100, 'Démarche lancée'),)



    entrep = models.CharField(default = 'votre entreprise', max_length=250,verbose_name = "Le nom de votre entreprise",)
    nom = models.CharField(default = 'votre nom', max_length=250,verbose_name = "votre nom",)
    adresse = models.CharField(max_length=250,verbose_name = "Votre adresse",)
    ville = models.CharField(max_length=250,verbose_name = "Votre ville",)
    #mail = models.EmailField()

    nbsal = models.IntegerField(default=0,verbose_name = "Nombre de salariés",)
    freq = models.IntegerField(default = 65, verbose_name = "Fréquence moyenne de la pratique des cyclistes (en pourcentage de jours travaillés)",)
    dist = models.IntegerField(default = 3, verbose_name = "Distance Domicile travail moyenne des cyclistes de votre entreprise",)
    access = models.CharField(default='Bonne',choices=ACC_LIB,verbose_name = "Accessibilite du site",max_length=10)
    ctxgeolib = models.FloatField(choices=CTX_GEO_LIB,default='Centre-ville',verbose_name = "Contexte geographique")

    g1 = models.IntegerField(choices=MG1,verbose_name = "Motivation de la direction de l’entreprise")
    g2 = models.IntegerField(choices=MG2,verbose_name = "Motivation des salariés")
    g3 = models.IntegerField(choices=MG3,verbose_name = "Etat d'avancement du PDE")

    published_date = models.DateTimeField(blank=True, null=True)
    vctx = models.IntegerField(blank=True, null=True, default=0,verbose_name = "Var ctx")
    #g4 = models.IntegerField(default=0)

    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    def publish(self):
    	self.published_date = timezone.now()
    	self.save()

    def pvelo(self):
        """Calcul du potentiel vélo"""
        self.pv = (float(self.ctxgeolib)*int(self.nbsal))/100
        self.pv = ceil(self.pv)
        return self.pv

    def paccess(self):
        """Calcul du coef de pondération Accessibilité"""
        if self.access == "bonne":
            self.pa = self.freq/100
        elif self.access == "moyenne":
            self.pa = self.freq/100*0.9
        else:
            self.pa = self.freq/100*0.8
        return self.pa

    def evocycliste(self):
        """fonction d'evaluation de l'evolution du nombre de cyclistes"""
        self.evocycl = self.pvelo() *(1+0.5)
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
        if (0 <= self.g1 <= 20):
            self.recog1 = "Taux d'adhésion de la direction inférieur à 20 %"
        elif(20 <= self.g1 <= 50):
            self.recog1 = "Taux d'adhésion de la direction compris entre 20 et 50%"
        elif (50 <= self.g1 <= 75):
            self.recog1 = "Taux d'adhésion de la direction compris entre 50 et 75%"
        else:
            self.recog1 = "Taux d'adhésion de la direction sup à 75%"
        return self.recog1

    def recosal(self):
        """Génération des recommendations auprès des salariés"""
        if (0 <= self.g2 <= 20):
            self.recog2 = "Taux d'adhésion des salariés inférieur à 20 %"
        elif(20 <= self.g2 <= 50):
            self.recog2 = "Taux d'adhésion des salariés compris entre 20 et 50%"
        elif (50 <= self.g2 <= 75):
            self.recog2 = "Taux d'adhésion des salariés compris entre 50 et 75%"
        else:
            self.recog2 = "Taux d'adhésion des salariés sup à 75%"
        return self.recog2

    def recopde(self):
        """Génération des recommendations en fonction de l'avancement du PDE"""
        if (0 <= self.g3 <= 20):
            self.recog3 = "Avancée du PDE inférieur à 20 %"
        elif(20 <= self.g3 <= 50):
            self.recog3 = "Avancée du PDE compris entre 20 et 50%"
        elif (50 <= self.g3 <= 75):
            self.recog3 = "Avancée du PDE compris entre 50 et 75%"
        else:
            self.recog3 = "Avancée du PDE sup à 75%"
        return self.recog3

    def varctx(self):
        """retourne le switch ctx"""
        if self.recopde() == "Avancée du PDE inférieur à 20 %": #TODO !!!
            self.vctx = 0
        else:
            self.vctx = 1
        return self.vctx

    def recoscore(self):
        """fonction de scorind de l'évaluation du PDE"""
        score = int((self.g1+self.g2+self.g3)/300*100)
        return score

    def reusite(self):
        """fonction d'évaluation de la réusite du PDE en fonction de la motive"""
        if self.ctxgeolib == '4.9':
            self.notegeo = 100
        elif self.ctxgeolib == '1.7':
            self.notegeo = 50
        elif self.ctxgeolib == '1.5':
            self.notegeo = 1
        else:
            self.notegeo = 50

        if self.access == "bonne":
            self.noteacces = 100
        elif self.access == "moyenne":
            self.noteacces = 50
        else:
            self.noteacces = 1

        self.notefreq = self.freq

        reusite = (self.notegeo + self.noteacces + self.notefreq + self.recoscore())/400
        return reusite












    def __str__(self):
        return self.nom