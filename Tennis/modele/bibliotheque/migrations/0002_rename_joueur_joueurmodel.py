# Generated by Django 4.0.4 on 2022-05-17 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bibliotheque', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Joueur',
            new_name='JoueurModel',
        ),
    ]