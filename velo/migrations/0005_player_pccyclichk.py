# Generated by Django 2.0.5 on 2018-07-03 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('velo', '0004_player_pccycliste'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='pccyclichk',
            field=models.PositiveIntegerField(default='0', verbose_name='Ne sais pas estimer'),
        ),
    ]