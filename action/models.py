from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone





class Site(models.Model):
    nom = models.CharField(default='', max_length=250,verbose_name = "Le nom de votre entreprise",)
    lstaction = models.CharField(default='', max_length=400,verbose_name = "code des actions selectionnees dans une liste python",)

class Action(models.Model):
    nomfiche= models.CharField(default='', max_length=250,verbose_name = 'Nom de fiche',)
    catenjeux= models.CharField(default='', max_length=250,verbose_name = 'Catégorie d\'enjeux',)
    codecouleur= models.CharField(default='', max_length=250,verbose_name = 'Code couleur',)
    numfiche= models.CharField(default='', max_length=250,verbose_name = 'Numéro de fiche',)
    typeaction= models.CharField(default='', max_length=250,verbose_name = 'Typologie d\'action',)
    constat= models.CharField(default='', max_length=250,verbose_name = 'Constat',)
    objectif= models.CharField(default='', max_length=250,verbose_name = 'Objectif',)
    ccible= models.CharField(default='', max_length=250,verbose_name = 'Cible',)
    objmoyen= models.CharField(default='', max_length=250,verbose_name = 'Moyens pour atteindre l\'objectif',)
    factreu= models.CharField(default='', max_length=250,verbose_name = 'Facteurs de réussite',)
    porteur= models.CharField(default='', max_length=250,verbose_name = 'Porteur de l\'action',)
    intervenant= models.CharField(default='', max_length=250,verbose_name = 'Intervenants potentiels',)
    planning= models.CharField(default='', max_length=250,verbose_name = 'Planning',)
    impacts= models.CharField(default='', max_length=250,verbose_name = 'Impacts: facilité de mise en œuvre, innovation et image du territoire, économie de CO2 réalisée, amélioration du climat social,  moyens financiers et humains à mettre en œuvre',)
    indicateurs= models.CharField(default='', max_length=250,verbose_name = 'Indicateurs',)
    indicateurs_tp= models.CharField(default='', max_length=250,verbose_name = 'Périodicité de relevé des indicateurs',)
    cinvestdet= models.CharField(default='', max_length=250,verbose_name = 'Coût d\'investissement détail',)
    cinvestchi= models.CharField(default='', max_length=250,verbose_name = 'Coût d\'investissement chiffré',)
    cfonctiondet= models.CharField(default='', max_length=250,verbose_name = 'Coûts de fonctionnement détail',)
    cfonctionchi= models.CharField(default='', max_length=250,verbose_name = 'Coût de fonctionnement chiffré',)
    periodicite= models.CharField(default='', max_length=250,verbose_name = 'Priorité ',)
    tellmemore= models.CharField(default='', max_length=250,verbose_name = 'Pour aller plus loin',)

