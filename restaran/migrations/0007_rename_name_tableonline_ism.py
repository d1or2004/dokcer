# Generated by Django 5.0.4 on 2024-05-12 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaran', '0006_alter_tableonline_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tableonline',
            old_name='name',
            new_name='ism',
        ),
    ]
