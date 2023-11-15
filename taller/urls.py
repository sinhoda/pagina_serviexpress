from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("producto/<int:prod_id>/", views.ventaProducto, name="ventaProducto"),
    #CrudProductos
    path("crud/productos", views.crudProductos, name="crudProductos"),
    path('crud/eliminarProducto/<int:prod_id>',views.eliminarProducto, name="eliminarProducto"),
    path('crud/agregarProductoForm',views.agregarProducto),
    path('crud/editarProducto/<int:prod_id>',views.cargarEditarProducto, name="editarProducto"),
    path('crud/editarProducto',views.editarProducto),
    path('crud/agregarCategoriaForm',views.agregarCategoria),
    #CRUD Servicios
    path("crud/servicios", views.crudServicios, name="crudServicios"),
    path('crud/agregarServicioForm',views.agregarServicio),
    path('crud/eliminarServicio/<int:serv_id>',views.eliminarServicio, name="eliminarServicio"),
    path('crud/editarServicio/<int:serv_id>',views.cargarEditarServicio, name="editarProducto"),
    path('crud/editarServicio',views.editarServicio),
    #Crud empleados
    path("crud/empleados", views.crudEmpleados, name="crudEmpleados"),
    path('crud/agregarEmpleadoForm',views.agregarEmpleado),
    path('crud/eliminarEmpleado/<int:rut>',views.eliminarEmpleado, name="eliminarEmpleado"),
    path('crud/editarEmpleado/<int:rut>',views.cargarEditarEmpleado, name="editarEmpleado"),
    path('crud/editarEmpleado',views.editarEmpleado),

]