# Generated by Django 5.1.5 on 2025-05-21 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lycee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='enseignant',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=254),
        ),
    ]
