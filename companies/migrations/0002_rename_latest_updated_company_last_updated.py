# Generated by Django 3.2.5 on 2021-07-14 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='latest_updated',
            new_name='last_updated',
        ),
    ]
