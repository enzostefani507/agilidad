from django.contrib import admin
from estado.models import cambios

class cambiosAdmin(admin.ModelAdmin):
    fields = ('tipo','origen','destino')
    
    def save_model(self, request, obj, form, change):
        obj.origen = request.user
        obj.save()

admin.site.register(cambios, cambiosAdmin)

