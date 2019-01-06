from django import forms

from .models import Site, Action

LST_ACTION = (
    ('1', 'Action 1'),
    ('2', 'Action 2'),
    ('3', 'Action 3'),
)


ENJEUX = (
    ('1', "Introduction au plan d'actions"),
    ('2', "Manager et piloter le plan de mobilité"),
    ('3', "Communiquer et animer globalement"),
    ('4', "Favoriser les modes actifs"),
    ('5', "Favoriser l'usage des transports collectifs"),
    ('6', "Réduire les déplacements"),
    ('7', "Réduire l'impact des véhicules"),
    ('8', "Promouvoir la multimodalité"),
    ('9', "Développer la multimodalité"),
    ('10', "Autres"),
)


class LstAction(forms.Form):
    nom = forms.CharField(max_length=250)
    lstaction = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=LST_ACTION,
    )

class CatAction(forms.Form):
    nomfiche = forms.CharField(max_length=250,)
    catenjeux = forms.ChoiceField(choices=ENJEUX,)
    codecouleur = forms.CharField(max_length=250,)
    numfiche = forms.CharField(max_length=250,)
    typeaction = forms.CharField(max_length=250,required=False)
    constat = forms.CharField(max_length=250,widget=forms.Textarea,required=False)
    objectif = forms.CharField(max_length=250,required=False)
    ccible = forms.CharField(max_length=250,required=False)
    objmoyen = forms.CharField(max_length=250,required=False)
    factreu = forms.CharField(max_length=250,required=False)
    porteur = forms.CharField(max_length=250,required=False)
    intervenant = forms.CharField(max_length=250,required=False)
    planning = forms.CharField(max_length=250,required=False)
    impacts = forms.CharField(max_length=250,required=False)
    indicateurs = forms.CharField(max_length=250,required=False)
    indicateurs_tp = forms.CharField(max_length=250,required=False)
    cinvestdet = forms.CharField(max_length=250,required=False)
    cinvestchi = forms.CharField(max_length=250,required=False)
    cfonctiondet = forms.CharField(max_length=250,required=False)
    cfonctionchi = forms.CharField(max_length=250,required=False)
    periodicite = forms.CharField(max_length=250,required=False)
    tellmemore = forms.CharField(max_length=250,required=False)





