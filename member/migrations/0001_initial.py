# Generated by Django 4.0.4 on 2022-05-31 01:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Socio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('canac', models.CharField(default='null', max_length=6)),
                ('data_nascimento', models.DateTimeField(blank=True, null=True)),
                ('cpf', models.CharField(default='null', max_length=11)),
                ('socio', models.OneToOneField(default='null', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Sócio',
                'verbose_name_plural': 'Sócios',
            },
        ),
    ]
