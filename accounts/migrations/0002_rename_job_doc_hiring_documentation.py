# Generated by Django 4.2.11 on 2024-04-03 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hiring',
            old_name='job_doc',
            new_name='documentation',
        ),
    ]
