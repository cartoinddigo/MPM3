# Generated by Django 2.0.1 on 2018-04-16 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('velo', '0007_auto_20180416_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='vctx',
            field=models.IntegerField(default=0, verbose_name='Var ctx'),
        ),
    ]
