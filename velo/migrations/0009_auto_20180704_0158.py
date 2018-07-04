# Generated by Django 2.0.5 on 2018-07-03 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('velo', '0008_auto_20180704_0129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='adresse',
        ),
        migrations.AlterField(
            model_name='player',
            name='pccycliste',
            field=models.PositiveIntegerField(choices=[(3, 'Moins de 5 %'), (20, 'Environ un quart'), (55, 'Environ la moitié'), (80, 'Plus de la moitié'), (50, 'Ne sais pas estimer')], default='3', verbose_name='NPourcentages cyclistes'),
        ),
    ]
