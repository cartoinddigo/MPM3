# Generated by Django 2.1.2 on 2018-12-15 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('action', '0004_choixaction_lstaction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choixaction',
            name='lstaction',
        ),
    ]
