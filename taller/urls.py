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
    path('crud/agregarCategoriaForm',views.agregarCategoria),
    #CRUD Servicios
    path("crud/servicios", views.crudServicios, name="crudServicios"),
    path('crud/agregarServicioForm',views.agregarServicio),
    
]