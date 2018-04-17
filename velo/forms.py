from django import forms

from .models import Player


class PlayerForm(forms.ModelForm):

    class Meta:
        model = Player
        fields = ('nom', 'entrep', 'ville', 'ctxgeolib','nbsal','freq','access','g1','g2','g3')