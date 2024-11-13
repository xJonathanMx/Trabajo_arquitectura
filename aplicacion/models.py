from django.db import models

# Create your models here.
class Usuario(models.Model):
    rut=models.IntegerField(primary_key=True)
    nombre_completo=models.CharField(max_length=100)
    telefono=models.IntegerField()
    correo_usuario=models.CharField( max_length=64)
    #detalle_pago=models.ForeignKey("detalle_pago", on_delete=models.CASCADE)


class departamento(models.Model):
    id_departamento=models.AutoField(primary_key=True)
    num_piso=models.IntegerField()
    descripcion_dpto=models.CharField( max_length=100)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class detalle_pago(models.Model):
    id_pago=models.AutoField(primary_key=True)
    fecha_pago=models.DateField()
    tipo_pago=models.IntegerField()
    gasto=models.ForeignKey("Gasto_Comun", on_delete=models.CASCADE)
    
class Gasto_Comun(models.Model):
    id_gasto_comun=models.AutoField(primary_key=True)
    monto=models.IntegerField()
    fecha_vencimiento=models.DateField()
    
