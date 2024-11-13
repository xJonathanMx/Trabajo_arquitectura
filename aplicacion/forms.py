from .models import Usuario
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class UsuarioForm(forms.ModelForm):
    class Meta:
        model= Usuario
        fields=("nombre_completo",'telefono','correo_usuario')
        
class UpdUsuarioForm(forms.ModelForm):
    class Meta:
        model=Usuario
        fields=('nombre_completo','telefono','correo_usuario')