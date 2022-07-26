from django.contrib import admin
from . import models

class AeronaveAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'valor_hora')

admin.site.register(models.Voo)
admin.site.register(models.Aeronave, AeronaveAdmin)
admin.site.register(models.Instrutor)
admin.site.register(models.Financeiro)


