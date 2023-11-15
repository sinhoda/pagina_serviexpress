from django.db import models
from django.conf import settings

# Create your models here.
class Taller(models.Model):
    id_taller= models.IntegerField(default=0)
    nombre= models.CharField(max_length=200)
    direccion= models.CharField(max_length=200)
    telefono= models.IntegerField(default=0)
    ciudad= models.CharField(max_length=200)


class Cliente(models.Model):
    rut= models.CharField(max_length=12)
    nombre= models.CharField(max_length=200)
    apellido_paterno= models.CharField(max_length=200)
    apellido_materno= models.CharField(max_length=200)
    numero_contacto= models.IntegerField()
    correo_electronico= models.CharField(max_length=200)    
    direccion_vivienda= models.CharField(max_length=200)
    autos= models.CharField(max_length=200) #Cambiar a futuro

class Auto(models.Model):
    patente= models.CharField(max_length=6)
    marca= models.CharField(max_length=200)
    modelo= models.CharField(max_length=200)
    anio_auto= models.IntegerField() #Cambiar a date 
    def __str__(self):
        txt = "Patente: {0} - Marca: {1} - Modelo: {2} - Año: {3}"
        return txt.format(self.patente , self.marca, self.modelo, self.anio_auto)



 

class Categoria_producto(models.Model):
    id_categoria = models.IntegerField(primary_key=True)
    nombre_categoria = models.CharField(max_length=200)
    def __str__(self):
        txt = "Categoria: {0}"
        return txt.format(self.nombre_categoria)


class Producto(models.Model):
    id_producto= models.IntegerField(default=0, primary_key=True)
    nombre_producto= models.CharField(max_length=200)
    precio= models.IntegerField(default=0)
    descripcion= models.CharField(max_length=200)
    imagenUrl = models.ImageField(upload_to="imagenesProducto")
    stock = models.IntegerField(default=0)
    categoria = models.ForeignKey(Categoria_producto, on_delete=models.CASCADE)


class Estado_civil(models.Model):
    id_estado_civil= models.IntegerField(primary_key=True)
    estado_civil = models.CharField(max_length=200)

class Tipo_empleado(models.Model):
    id_tipo_empleado = models.IntegerField(primary_key=True)
    tipo_empleado = models.CharField(max_length=200)

class Empleado(models.Model):
    rut= models.CharField(max_length=12, primary_key=True)
    nombre= models.CharField(max_length=200)
    apellido_paterno= models.CharField(max_length=200)
    apellido_materno= models.CharField(max_length=200)
    numero_contacto= models.IntegerField()
    correo_electronico= models.CharField(max_length=200)
    direccion_vivienda= models.CharField(max_length=200)
    estado_civil= models.ForeignKey(Estado_civil, on_delete=models.CASCADE) 
    tipo_empleado= models.ForeignKey(Tipo_empleado, on_delete=models.CASCADE)


class Servicio(models.Model):
    id_servicio= models.IntegerField(default=0, primary_key=True)
    nombre_servicio= models.CharField(max_length=200)
    descripcion= models.CharField(max_length=200)
    encargado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    precio= models.IntegerField(default=1)


class Reserva(models.Model):
    id_reserva= models.IntegerField(default=0, primary_key=True)
    precio= models.IntegerField(default=0)   
    fecha_atencion= models.CharField(max_length=200) #Cambiar a date



class Detalle_reserva(models.Model):
    id_detalle_reserva= models.IntegerField(default=0, primary_key=True)
    id_reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    servicio= models.CharField(max_length=200) #Cambiar a foreign key de servicio    
    

