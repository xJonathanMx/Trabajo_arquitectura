from .models import Residente,departamento,Gasto_Comun
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class UsuarioForm(forms.ModelForm):
    class Meta:
        model= Residente
        fields=("rut","nombre_completo",'telefono','correo_usuario');
        
class UpdUsuarioForm(forms.ModelForm):
    class Meta:
        model=Residente
        fields=('nombre_completo','telefono','correo_usuario');
class GastoComunForm(forms.ModelForm):
    class Meta:
        model=Gasto_Comun
        fields=('monto','fecha_vencimiento','residente');
class DepartamentoForm(forms.ModelForm):
    class Meta:
        model=departamento
        fields=('numero_piso','descripcion_dpto','num_habitaciones','residente');
class UpDepaForm(forms.ModelForm):
    class Meta:
        model=departamento
        fields=('numero_piso','descripcion_dpto','num_habitaciones','residente');
class UpGastoForm(forms.ModelForm):
    class Meta:
        model=Gasto_Comun
        fields=('monto','fecha_vencimiento','residente');