# Generated by Django 4.0.1 on 2022-01-08 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('towns', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uktowns',
            name='country',
            field=models.CharField(max_length=16, unique=True),
        ),
    ]
