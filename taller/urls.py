from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("servicio/<int:serv_id>/", views.VerServicio, name="ventaProducto"),
    # CrudProductos
    path("crud/productos", views.crudProductos, name="crudProductos"),
    path(
        "crud/eliminarProducto/<int:prod_id>",
        views.eliminarProducto,
        name="eliminarProducto",
    ),
    path("crud/agregarProductoForm", views.agregarProducto),
    path(
        "crud/editarProducto/<int:prod_id>",
        views.cargarEditarProducto,
        name="editarProducto",
    ),
    path("crud/editarProducto", views.editarProducto),
    path("crud/agregarCategoriaForm", views.agregarCategoria),
    # CRUD Servicios
    path("crud/servicios", views.crudServicios, name="crudServicios"),
    path("crud/agregarServicioForm", views.agregarServicio),
    path(
        "crud/eliminarServicio/<int:serv_id>",
        views.eliminarServicio,
        name="eliminarServicio",
    ),
    path(
        "crud/editarServicio/<int:serv_id>",
        views.cargarEditarServicio,
        name="editarProducto",
    ),
    path("crud/editarServicio", views.editarServicio),
    # Crud empleados
    path("crud/empleados", views.crudEmpleados, name="crudEmpleados"),
    path("crud/agregarEmpleadoForm", views.agregarEmpleado),
    path(
        "crud/eliminarEmpleado/<int:id>",
        views.eliminarEmpleado,
        name="eliminarEmpleado",
    ),
    path(
        "crud/editarEmpleado/<int:id>",
        views.cargarEditarEmpleado,
        name="editarEmpleado",
    ),
    path("crud/editarEmpleado", views.editarEmpleado),
    # Compra y carrito
    path("carrito", views.carrito, name="carrito"),
    path("carrito/confirmarServicio", views.confirmarServicio),
    # CRUD Proveedores
    path("crud/proveedores", views.crudProveedores, name="crudProveedores"),
    path("crud/proveedores/agregarRubroForm", views.agregarRubro),
    path("crud/proveedores/agregarProveedorForm", views.agregarProveedor),
    path(
        "crud/proveedores/eliminarProveedor/<int:prov_id>",
        views.eliminarProveedor,
        name="eliminarProducto",
    ),
    # Inicio de sesion
    path("iniciar_sesion", views.cargarInicioSesion, name="CargarInicioSesion"),
    path("iniciar_sesion/iniciarSesionForm", views.iniciarSesion),
    path("cerrar_sesion", views.cerrarSesion),
    path("iniciar_sesion/registro_cliente", views.registroCliente, name="RegistroCliente"),
    path("iniciar_sesion/registro_cliente/registroClienteForm", views.registroCliente, name="RegistroCliente"),
    #Lista de servicios
    path("servicios", views.ListaServicio, name="VerServicios"),
    path("carrito/servicio_confirmado", views.servicioFinalizado),
]
