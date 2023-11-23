from django.db import models
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin

from django.db.models.signals import post_save
from django.dispatch import receiver


class Taller(models.Model):
    id_taller = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    telefono = models.IntegerField(default=0)
    ciudad = models.CharField(max_length=200)


class Tipo_empleado(models.Model):
    id_tipo_empleado = models.AutoField(primary_key=True)
    tipo_empleado = models.CharField(max_length=200)

    def __str__(self):
        txt = "id: {0} - tipo empleado: {1} "
        return txt.format(self.id_tipo_empleado, self.tipo_empleado)


class Estado_civil(models.Model):
    id_estado_civil = models.AutoField(primary_key=True)
    estado_civil = models.CharField(max_length=200)

    def __str__(self):
        txt = "id: {0} - estado civil: {1} "
        return txt.format(self.id_estado_civil, self.estado_civil)

class Tipo_usuario(models.Model):
    id_tipo_usuario = models.AutoField(primary_key=True)
    tipo_usuario = models.CharField(max_length=200)
    def __str__(self):
        txt = "id: {0} - tipo usuario: {1} "
        return txt.format(self.id_tipo_usuario, self.tipo_usuario)


class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Se necesita un correo")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False) 
        extra_fields.setdefault('is_superuser', False) 
        return self._create_user(email, password, **extra_fields)
        
    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True) 
        extra_fields.setdefault('is_superuser', True) 
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(blank=True, default='', unique=True)
    nombre = models.CharField(max_length=200, blank=True)
    rut = models.IntegerField(blank=True, null=True)
    ap_paterno = models.CharField(max_length=200, blank=True)
    ap_materno = models.CharField(max_length=200, blank=True)
    direccion = models.CharField(max_length=200, blank=True)
    numero_contacto = models.IntegerField(blank=True, null=True )

    is_empleado = models.BooleanField(default=False)
    tipo_empleado = models.ForeignKey(Tipo_empleado, on_delete=models.CASCADE, null=True, blank=True)
    estado_civil = models.ForeignKey(Estado_civil, on_delete=models.CASCADE, null=True)
    taller = models.ForeignKey(Taller, on_delete=models.CASCADE, null=True, blank=True)



    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'   
    REQUIRED_FIELDS = []



@receiver(post_save, sender=User)
def user_empleado(sender, instance, created, **kwargs):
    if created and instance.is_empleado:
        pass


# Create your models here.


class Auto(models.Model):
    patente = models.CharField(max_length=6, primary_key=True)
    marca = models.CharField(max_length=200)
    modelo = models.CharField(max_length=200)
    anio_auto = models.DateField()  # Cambiar a date
    """ duenio = models.ForeignKey(Cliente, on_delete=models.CASCADE) """

    def __str__(self):
        txt = "Patente: {0} - Marca: {1} - Modelo: {2} - Año: {3}"
        return txt.format(self.patente, self.marca, self.modelo, self.anio_auto)


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
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=200)
    precio = models.IntegerField(default=0)
    descripcion = models.CharField(max_length=200)
    imagenUrl = models.ImageField(upload_to="imagenesProducto")
    stock = models.IntegerField(default=0)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria_producto, on_delete=models.CASCADE)

    def __str__(self):
        txt = "id: {0} - nombre: {1} - precio: {2}"
        return txt.format(self.id_producto, self.nombre_producto, self.precio)


class Servicio(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    nombre_servicio = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    """ encargado = models.ForeignKey(Empleado, on_delete=models.CASCADE) """
    precio = models.IntegerField(default=1)
    imagenUrl = models.ImageField(upload_to="imagenesServicios")

    def __str__(self):
        txt = "id: {0} - servicio: {1} - precio: {2} - encargado: {3}"
        return txt.format(
            self.id_servicio, self.nombre_servicio, self.precio, self.encargado
        )


class Reserva(models.Model):
    id_reserva = models.AutoField(primary_key=True)
    precio = models.IntegerField(default=0)
    fecha_solicitud = models.DateField(auto_now_add=True)
    """ FK_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE) """
    fecha_realizar = models.DateField()


class Detalle_reserva(models.Model):
    id_detalle_reserva = models.AutoField(primary_key=True)
    id_reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    FK_servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
