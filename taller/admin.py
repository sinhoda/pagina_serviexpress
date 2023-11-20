from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Taller)
admin.site.register(Empleado)
admin.site.register(Servicio)
admin.site.register(Cliente)
admin.site.register(Auto)
admin.site.register(Reserva)
admin.site.register(Detalle_reserva)
admin.site.register(Categoria_producto)
admin.site.register(Producto)   
admin.site.register(Estado_civil)   
admin.site.register(Tipo_empleado)
admin.site.register(Venta)
admin.site.register(Detalle_venta)






