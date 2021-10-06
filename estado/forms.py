from django import forms
from perfil.models import Usuario 
from estado.models import cambios

class CambioForm(forms.ModelForm):

    class Meta:
        model = cambios
        fields = ('tipo','origen','destino')