# Generated by Django 2.0.1 on 2018-04-08 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('velo', '0003_remove_player_nom'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
