# Generated by Django 2.1.2 on 2018-12-15 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('action', '0007_auto_20181216_0000'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='lstaction',
            field=models.CharField(default='', max_length=400, verbose_name='code des actions selectionnees dans une liste python'),
        ),
    ]
