# Generated by Django 2.0.5 on 2018-07-03 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('velo', '0007_remove_player_pccyclichk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='pccycliste',
            field=models.PositiveIntegerField(choices=[(5, 'Moins de 5 %'), (20, 'Environ un quart'), (50, 'Environ la moitié'), (80, 'Plus de la moitié')], default='3', verbose_name='NPourcentages cyclistes'),
        ),
    ]