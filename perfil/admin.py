from django.contrib import admin
from .models import *



class habilitarCambioAdmin(admin.ModelAdmin):
    actions = ['habilitarCambio']

    def habilitarCambio(self,request,queryset):
        queryset = queryset.exclude(gris_disponible = True)
        for miembro in queryset:
            miembro.gris_disponible = True
            miembro.save()

admin.site.register(Usuario,habilitarCambioAdmin)
admin.site.register(Equipo)