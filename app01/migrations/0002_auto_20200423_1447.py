# Generated by Django 3.0.2 on 2020-04-23 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='administrator',
            old_name='pssword',
            new_name='password',
        ),
    ]
