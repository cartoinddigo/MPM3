from django import forms

from .models import Player


class PlayerForm(forms.ModelForm):

    class Meta:
        model = Player
        fields = ('entrep', 'adresse', 'ville', 'ctxgeolib', 'nbsal','partmodal','txpratique','access','g1','g2','g3')