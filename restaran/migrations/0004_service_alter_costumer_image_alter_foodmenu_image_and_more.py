# Generated by Django 5.0.4 on 2024-05-12 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaran', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='costumer',
            name='image',
            field=models.ImageField(upload_to='media/costumer/'),
        ),
        migrations.AlterField(
            model_name='foodmenu',
            name='image',
            field=models.ImageField(upload_to='media/menu/'),
        ),
        migrations.AlterField(
            model_name='masterchef',
            name='image',
            field=models.ImageField(upload_to='media/chef/'),
        ),
    ]