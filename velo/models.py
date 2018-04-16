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
    partmodal = models.IntegerField(default=0,verbose_name = "Nombre de cyclistes dans l'entreprise",)
    txpratique = models.IntegerField(default=65,verbose_name = "Taux de pratique (en pourcentages de jours travaillés)",)
    access = models.TextField(default='bonne',choices=ACC_LIB,verbose_name = "Accessibilite du site",)
    #ctxgeo = models.IntegerField()
    ctxgeolib = models.TextField(choices=CTX_GEO_LIB,verbose_name = "Contexte geographique")
    g1 = models.IntegerField(default=0,verbose_name = "Motivation de la direction de l’entreprise")
    g2 = models.IntegerField(default=0,verbose_name = "Motivation des salariés")
    g3 = models.IntegerField(default=0, verbose_name = "Etat d'avancement du PDE")
    
    ctx = 0
    pde = 0
    pcdir = 0
    pcsal = 0

    published_date = models.DateTimeField(blank=True, null=True)
    #g4 = models.IntegerField(default=0)

    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    def publish(self):
    	self.published_date = timezone.now()
    	self.save()

    def pvelo(self):
        self.pv = (float(self.ctxgeolib)/int(self.nbsal))*100
        self.pv = ceil(self.pv)
        return self.pv


    def __str__(self):
        return self.nom