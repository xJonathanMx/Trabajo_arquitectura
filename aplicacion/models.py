from django.db import models

# Create your models here.
class Residente(models.Model):
    rut=models.IntegerField(primary_key=True,null=False)
    nombre_completo=models.CharField(max_length=100)
    telefono=models.IntegerField()
    correo_usuario=models.CharField( max_length=64)
    def __str__(self):
        return f"{self.rut} {self.nombre_completo}"
    
class departamento(models.Model):
    numero_piso=models.IntegerField(primary_key=True)
    descripcion_dpto=models.CharField( max_length=100)
    num_habitaciones=models.IntegerField()
    residente = models.ForeignKey(Residente,null=True,blank=True, on_delete=models.CASCADE)
   
    def __str__(self):
        return f"{self.numero_piso} {self.residente}"
    
class Gasto_Comun(models.Model):
    id_gasto_comun=models.AutoField(primary_key=True)
    monto=models.IntegerField()
    fecha_vencimiento=models.DateField()
    residente = models.ForeignKey(Residente, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.monto} {self.fecha_vencimiento}"
    
    
