# Generated by Django 2.1.2 on 2019-03-27 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('velo', '0008_auto_20190327_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='access',
            field=models.IntegerField(choices=[(3, 'Bonne'), (2, 'Moyenne'), (1, 'Mauvaise')], default=3, verbose_name='Accessibilite du site'),
        ),
    ]