from import_export import resources
from import_export.fields import Field
from .models import Player

class Playerexp(resources.ModelResource):
    players = Player.objects.all()
    explvelo = Field(attribute='Player.pvelo')
    class Meta:
        
        model = Player