# Generated by Django 2.0.5 on 2018-07-03 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('velo', '0005_player_pccyclichk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='g3',
            field=models.IntegerField(choices=[(10, 'Inexistant'), (50, 'En réflexion'), (100, 'Actif')], verbose_name="Etat d'avancement du PDE"),
        ),
    ]
