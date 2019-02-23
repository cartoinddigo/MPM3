# Generated by Django 2.1.2 on 2018-12-18 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('action', '0009_delete_site'),
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(default='', max_length=250, verbose_name='Le nom de votre entreprise')),
                ('lstaction', models.CharField(default='', max_length=400, verbose_name='code des actions selectionnees dans une liste python')),
            ],
        ),
    ]