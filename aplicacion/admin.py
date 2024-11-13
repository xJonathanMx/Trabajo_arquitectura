from django.contrib import admin
from .models import Usuario,departamento,detalle_pago,Gasto_Comun
# Register your models here.

# 1. Usuario
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombre_completo', 'telefono', 'correo_usuario')
    search_fields = ('rut',)  # Corregido a tupla con una coma

# 2. Departamento
@admin.register(departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('id_departamento', 'num_piso', 'descripcion_dpto')
    search_fields = ('id_departamento',)

# 3. Detalle Pago
@admin.register(detalle_pago)
class DetallePagoAdmin(admin.ModelAdmin):
    list_display = ('id_pago', 'fecha_pago', 'tipo_pago')

# 4. Gasto Común
@admin.register(Gasto_Comun)
class GastoComunAdmin(admin.ModelAdmin):
    list_display = ('id_gasto_comun', 'monto', 'fecha_vencimiento')