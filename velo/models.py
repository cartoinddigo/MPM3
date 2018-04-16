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
    CTX1= '4.9'
    CTX2= '1.7'
    CTX3= '1.5'
    CTX4= '2.2'

    CTX_GEO_LIB = ((CTX1, 'Centre-ville'),(CTX2, 'Banlieues'),(CTX3, 'Rural'),(CTX4, 'Moyenne nationale'),)
    ACC_LIB = (('bonne','bonne' ),('moyenne','moyenne'),('mauvaise','mauvaise'))



    entrep = models.CharField(max_length=250,verbose_name = "Le nom de votre entreprise",)
    adresse = models.CharField(max_length=250,verbose_name = "Votre adresse",)
    ville = models.CharField(max_length=250,verbose_name = "Votre ville",)
    #mail = models.EmailField()

    nbsal = models.IntegerField(default=0,verbose_name = "Nombre de salariés",)
    freq = models.FloatField(default = 0.65, verbose_name = "Fréquence moyenne de la pratique des cycliste (en pourcentages de jours travaillés)",)
    dist = models.IntegerField(default = 3, verbose_name = "Distance Domicile travail moyenne des cyclistes de votre entreprise",)
    access = models.TextField(default='bonne',choices=ACC_LIB,verbose_name = "Accessibilite du site",)
    ctxgeolib = models.TextField(choices=CTX_GEO_LIB,verbose_name = "Contexte geographique")

    g1 = models.IntegerField(default=0,verbose_name = "Motivation de la direction de l’entreprise")
    g2 = models.IntegerField(default=0,verbose_name = "Motivation des salariés")
    g3 = models.IntegerField(default=0, verbose_name = "Etat d'avancement du PDE")

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
            self.pa = self.freq
        elif self.access == "moyenne":
            self.pa = self.freq*0.9
        else:
            self.pa = self.freq*0.8
        return self.pa

    def evocycliste(self):
        self.evocycl = self.pvelo() *(1+0.5)
        self.evocycl = ceil(self.evocycl)
        return self.evocycl

    def evoar(self):
        self.evoar = self.evocycliste()*218*self.freq
        self.evoar = ceil(self.evoar)
        return self.evoar

    def evoarp(self):
        self.evoarp = self.evocycliste()*218*self.paccess()
        self.evoarp = ceil(self.evoarp)
        return self.evoarp

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










    def __str__(self):
        return self.nom