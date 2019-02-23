# Generated by Django 2.1.2 on 2018-12-14 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entrep', models.CharField(max_length=250, verbose_name='Le nom de votre entreprise')),
                ('nbsal', models.PositiveIntegerField(verbose_name='Nombre de salariés')),
            ],
        ),
        migrations.CreateModel(
            name='ChoixAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NumFiche', models.IntegerField(choices=[('1', 'Fiche 1'), ('2', 'Fiche 2'), ('3', 'Fiche 3')], default='Fiche 1', verbose_name='Selectionnez votre fiche')),
            ],
        ),
    ]