# Generated by Django 4.0.1 on 2022-01-08 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('towns', '0002_alter_uktowns_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uktowns',
            name='country',
            field=models.CharField(max_length=16, null=True, unique=True),
        ),
    ]
