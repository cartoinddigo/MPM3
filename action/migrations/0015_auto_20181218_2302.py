# Generated by Django 2.1.2 on 2018-12-18 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('action', '0014_auto_20181218_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='enjeux',
            field=models.IntegerField(default=0, verbose_name="enjeux de l'action"),
        ),
    ]