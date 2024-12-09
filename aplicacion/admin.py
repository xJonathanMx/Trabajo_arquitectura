from django.contrib import admin
from .models import Residente,departamento,Gasto_Comun
# Register your models here.

# 1. Usuario
@admin.register(Residente)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombre_completo', 'telefono', 'correo_usuario')
    search_fields = ('rut',)  

# 2. Departamento
@admin.register(departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('numero_piso', 'descripcion_dpto')
    search_fields = ('id_departamento',)



# 4. Gasto Común
@admin.register(Gasto_Comun)
class GastoComunAdmin(admin.ModelAdmin):
    list_display = ('id_gasto_comun', 'monto', 'fecha_vencimiento')