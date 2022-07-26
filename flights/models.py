from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Financeiro(models.Model):
    tipo = models.CharField(default='Pagamento',
                        max_length=12,
                        choices=(
                        ('Pagamento', 'Pagamento'),
                        ('Hangaragem', 'Hangaragem'),
                        ('Mensalidade', 'Mensalidade')
                        )       
                        )
    socio = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    valor = models.FloatField(max_length=7)
    data_financeiro = models.DateField(blank=True, null=True)
    referente = models.CharField(max_length=100, blank=True)

class Instrutor(models.Model):
    nome_instrutor = models.CharField(max_length=30)
    canac_instrutor = models.CharField(max_length=6)

    def __str__(self):
        return self.nome_instrutor

    class Meta:
        verbose_name_plural = 'Instrutores'

class Aeronave(models.Model):
    matricula = models.CharField(max_length=6)
    valor_hora = models.FloatField(max_length=7)

    def __str__(self):
        return self.matricula

class Voo(models.Model):
    horimetro_inicial = models.CharField(max_length=6)
    horimetro_final = models.CharField(max_length=6)
    piloto = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    data = models.DateField(blank=True, null=True)
    mostrar = models.BooleanField(default=True)
    tipo = models.CharField(default='Instrução',
                            max_length=10,
                            choices=(
                                ('Instrução', 'Instrução'),
                                ('Privado', 'Privado')
                            )       
                            )
    instrutor = models.ForeignKey(Instrutor, on_delete=models.DO_NOTHING)
    aeronave = models.ForeignKey(Aeronave, on_delete=models.DO_NOTHING)
    valor_voo_total = models.FloatField(editable=False, null=True)

    def __str__(self):
        return self.horimetro_inicial

    class Meta:
        verbose_name = 'Voo'

    def save(self, *args, **kwargs):
        self.valor_voo_total = (float(self.horimetro_final) - float(self.horimetro_inicial))*self.aeronave.valor_hora
#        self.valor_voo_total.save()
        return super(Voo, self).save(*args, **kwargs)

    @property
    def tempo_voo(self):
        calculo = (float(self.horimetro_final) - float(self.horimetro_inicial))*60
        return f'{calculo:.2f}'


