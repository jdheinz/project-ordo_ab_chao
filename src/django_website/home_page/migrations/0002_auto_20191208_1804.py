# Generated by Django 2.2 on 2019-12-08 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='search',
            field=models.CharField(max_length=300),
        ),
    ]
