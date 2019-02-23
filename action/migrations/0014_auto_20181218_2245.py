# Generated by Django 2.1.2 on 2018-12-18 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('action', '0013_action'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='enjeux',
            field=models.IntegerField(choices=[('1', "Introduction au plan d'actions"), ('2', 'Manager et piloter le plan de mobilité'), ('3', 'Communiquer et animer globalement'), ('4', 'Favoriser les modes actifs'), ('5', "Favoriser l'usage des transports collectifs"), ('6', 'Réduire les déplacements'), ('7', "Réduire l'impact des véhicules"), ('8', 'Promouvoir la multimodalité'), ('9', 'Développer la multimodalité'), ('10', 'Autres')], default=0, verbose_name="enjeux de l'action"),
        ),
    ]