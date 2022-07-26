from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from member.models import Socio

class SocioInLine(admin.StackedInline):
    model = Socio
    can_delete = False
    verbose_name_plural = 'Sócios'

class UserAdmin(BaseUserAdmin):
    inlines = (SocioInLine,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
