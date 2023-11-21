from django.db import models
from django.conf import settings

# Create your models here.
class Taller(models.Model):
    id_taller= models.AutoField(primary_key=True)
    nombre= models.CharField(max_length=200)
    direccion= models.CharField(max_length=200)
    telefono= models.IntegerField(default=0)
    ciudad= models.CharField(max_length=200)

class Auto(models.Model):
    patente= models.CharField(max_length=6, primary_key=True)
    marca= models.CharField(max_length=200)
    modelo= models.CharField(max_length=200)
    anio_auto= models.DateField() #Cambiar a date 
    def __str__(self):
        txt = "Patente: {0} - Marca: {1} - Modelo: {2} - Año: {3}"
        return txt.format(self.patente , self.marca, self.modelo, self.anio_auto)

class Cliente(models.Model):
    rut= models.CharField(max_length=12, primary_key=True)
    nombre= models.CharField(max_length=200)
    apellido_paterno= models.CharField(max_length=200)
    apellido_materno= models.CharField(max_length=200)
    numero_contacto= models.IntegerField()
    correo_electronico= models.CharField(max_length=200)    
    direccion_vivienda= models.CharField(max_length=200)
    autos= models.ManyToManyField(Auto, null=True, blank=True) #Cambiar a futuro

class Rubro(models.Model):
    id_rubro = models.AutoField(primary_key=True)  
    nombre_rubro = models.CharField(max_length=200)
    

class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)  
    nombre_proveedor = models.CharField(max_length=200)
    rubro = models.ForeignKey(Rubro, on_delete=models.CASCADE)
    telefono = models.IntegerField()
    correo_electronico = models.CharField(max_length=200)
    informacion_extra = models.CharField(max_length=200, null=True, blank=True)


class Categoria_producto(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=200)
    def __str__(self):
        txt = "Categoria: {0}"
        return txt.format(self.nombre_categoria)

class Producto(models.Model):
    id_producto= models.AutoField(primary_key=True)
    nombre_producto= models.CharField(max_length=200)
    precio= models.IntegerField(default=0)
    descripcion= models.CharField(max_length=200)
    imagenUrl = models.ImageField(upload_to="imagenesProducto")
    stock = models.IntegerField(default=0)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria_producto, on_delete=models.CASCADE)
    def __str__(self):
        txt = "id: {0} - nombre: {1} - precio: {2}"
        return txt.format(self.id_producto, self.nombre_producto, self.precio)


class Estado_civil(models.Model):
    id_estado_civil= models.AutoField(primary_key=True)
    estado_civil = models.CharField(max_length=200)
    def __str__(self):
        txt = "id: {0} - estado civil: {1} "
        return txt.format(self.id_estado_civil, self.estado_civil)

class Tipo_empleado(models.Model):
    id_tipo_empleado = models.AutoField(primary_key=True)
    tipo_empleado = models.CharField(max_length=200)
    def __str__(self):
        txt = "id: {0} - tipo empleado: {1} "
        return txt.format(self.id_tipo_empleado, self.tipo_empleado)

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
    def __str__(self):
        txt = "rut: {0} - nombre: {1} - apellido paterno: {2} - apellido materno: {3} - tipo empleado: {4}"
        return txt.format(self.rut, self.nombre, self.apellido_paterno, self.apellido_materno, self.tipo_empleado)

class Servicio(models.Model):
    id_servicio= models.AutoField(primary_key=True)
    nombre_servicio= models.CharField(max_length=200)
    descripcion= models.CharField(max_length=200)
    encargado = models.ManyToManyField(Empleado)
    precio= models.IntegerField(default=1)
    imagenUrl = models.ImageField(upload_to="imagenesServicios")
    def __str__(self):
        txt = "id: {0} - servicio: {1} - precio: {2} - encargado: {3}"
        return txt.format(self.id_servicio, self.nombre_servicio, self.precio, self.encargado)
    

class Reserva(models.Model):
    id_reserva= models.AutoField(primary_key=True)
    precio= models.IntegerField(default=0)   
    fecha_solicitud = models.DateField(auto_now_add=True)
    FK_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_realizar = models.DateField()
    

class Detalle_reserva(models.Model):
    id_detalle_reserva= models.AutoField(primary_key=True)
    id_reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    FK_servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    

    
