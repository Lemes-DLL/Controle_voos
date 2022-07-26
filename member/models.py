from re import search
from telnetlib import DO
from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError

class Socio(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.DO_NOTHING, default='null', verbose_name='Sócio')
    data_nascimento = models.DateField(blank=True, null=True)
    cpf = models.CharField(max_length=11, default='null')


    def __str__(self):
        return f'{self.usuario}'

    def clean(self):
        error_messages = {}
        if search(r'[^0-9]', self.canac) or len(self.canac) != 6:
            error_messages['canac'] = 'Coloque um CANAC válido'
        
        if error_messages:
            raise ValidationError(error_messages)

    
    class Meta:
        verbose_name = 'Sócio'
        verbose_name_plural = 'Sócios'

    