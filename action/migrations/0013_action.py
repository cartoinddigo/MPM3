# Generated by Django 2.1.2 on 2018-12-18 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('action', '0012_auto_20181218_2157'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomfiche', models.CharField(default='', max_length=250, verbose_name="Le nom de l'action")),
                ('enjeux', models.IntegerField(default=0, verbose_name="enjeux de l'action")),
            ],
        ),
    ]
