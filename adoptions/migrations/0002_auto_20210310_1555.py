# Generated by Django 3.1.7 on 2021-03-10 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adoptions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='vaccination',
            new_name='vaccinations',
        ),
    ]
