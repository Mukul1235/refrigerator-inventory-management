# Generated by Django 5.1.5 on 2025-01-23 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='unit',
            field=models.CharField(choices=[('litre', 'litre'), ('gram', 'Gram'), ('units', 'Units')], max_length=20),
        ),
    ]
