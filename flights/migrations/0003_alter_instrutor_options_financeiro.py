# Generated by Django 4.0.4 on 2022-07-08 00:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flights', '0002_alter_voo_data'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='instrutor',
            options={'verbose_name_plural': 'Instrutores'},
        ),
        migrations.CreateModel(
            name='Financeiro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('Hangaragem', 'Hangaragem'), ('Mensalidade', 'Mensalidade')], default='Pagamento', max_length=12)),
                ('valor', models.FloatField(max_length=7)),
                ('data_financeiro', models.DateField(blank=True, null=True)),
                ('referente', models.CharField(max_length=100)),
                ('socio', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
