# Generated by Django 4.0.4 on 2022-05-31 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socio',
            name='data_nascimento',
            field=models.DateField(blank=True, null=True),
        ),
    ]