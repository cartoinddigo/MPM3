from django import forms

from .models import Player


class PlayerForm(forms.ModelForm):

    class Meta:
        model = Player
        fields = ('nom', 'entrep', 'ville', 'ctxgeolib', 'access','nbsal','freq','g1','g2','g3','g4', ) #