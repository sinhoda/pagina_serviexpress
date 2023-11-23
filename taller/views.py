from django.http import Http404
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
import os
from django.conf import settings
from .models import *
from django.http import JsonResponse
import json
from django.contrib.auth import authenticate, login


def index(request):
    vServicios = Servicio.objects.all
    template = loader.get_template("taller/index.html")
    context = {"servicios": vServicios}

    return HttpResponse(template.render(context, request))


def VerServicio(request, serv_id):
    template = loader.get_template("taller/verServicio.html")
    try:
        vServicio = Servicio.objects.get(pk=serv_id)
        context = {"servicio": vServicio}
    except Producto.DoesNotExist:
        raise Http404("Producto no existe")
    return HttpResponse(template.render(context, request))


# CRUD Productos


def crudProductos(request):
    vProductos = Producto.objects.all
    vCategorias = Categoria_producto.objects.all
    template = loader.get_template("taller/crudProductos.html")
    context = {"productos": vProductos, "categorias": vCategorias}
    return HttpResponse(template.render(context, request))


def eliminarProducto(request, prod_id):
    producto = Producto.objects.get(pk=prod_id)
    ruta_imagen = os.path.join(settings.MEDIA_ROOT, str(producto.imagenUrl))
    os.remove(ruta_imagen)
    producto.delete()
    return redirect("/taller/crud/productos")


def agregarCategoria(request):
    v_nombre = request.POST["txtnombreCategoria"]
    Categoria_producto.objects.create(
        nombre_categoria=v_nombre,
    )

    return redirect("/taller/crud/productos")


def agregarProducto(request):
    v_categoria = Categoria_producto.objects.get(
        id_categoria=request.POST["cmbCategoria"]
    )

    v_nombre = request.POST["txtnombre"]
    v_precio = request.POST["txtprecio"]
    v_stock = request.POST["txtStock"]
    v_descripcion = request.POST["txtDescripcion"]
    v_imagen = request.FILES["txtImagen"]

    Producto.objects.create(
        nombre_producto=v_nombre,
        precio=v_precio,
        stock=v_stock,
        descripcion=v_descripcion,
        imagenUrl=v_imagen,
        categoria=v_categoria,
    )

    return redirect("/taller/crud/productos")


# Editar productos
def cargarEditarProducto(request, prod_id):
    prod = Producto.objects.get(pk=prod_id)
    categorias = Categoria_producto.objects.all()
    template = loader.get_template("taller/editarProducto.html")
    context = {"producto": prod, "categorias": categorias}
    return HttpResponse(template.render(context, request))


def editarProducto(request):
    v_categoria = Categoria_producto.objects.get(
        id_categoria=request.POST["cmbCategoria"]
    )

    v_sku = request.POST["txtSku"]
    productoBD = Producto.objects.get(pk=v_sku)
    v_nombre = request.POST["txtnombre"]
    v_precio = request.POST["txtprecio"]
    v_stock = request.POST["txtStock"]
    v_descripcion = request.POST["txtDescripcion"]

    try:
        v_imagen = request.FILES["txtImagen"]
        ruta_imagen = os.path.join(settings.MEDIA_ROOT, str(productoBD.imagenUrl))
        os.remove(ruta_imagen)
        productoBD.imagenUrl = v_imagen
    except:
        productoBD.imagenUrl = productoBD.imagenUrl

    productoBD.nombre_producto = v_nombre
    productoBD.precio = v_precio
    productoBD.stock = v_stock
    productoBD.descripcion = v_descripcion
    productoBD.categoriaId = v_categoria

    productoBD.save()

    return redirect("/taller/crud/productos")


# Servicios


def crudServicios(request):
    vServicios = Servicio.objects.all
    vEmpleados = Empleado.objects.all
    template = loader.get_template("taller/crudServicios.html")
    context = {"servicios": vServicios, "empleados": vEmpleados}
    return HttpResponse(template.render(context, request))


def agregarServicio(request):
    v_empleado = Empleado.objects.get(pk=request.POST["cmbEncargado"])
    v_nombre = request.POST["txtnombre"]
    v_precio = request.POST["txtprecio"]
    v_descripcion = request.POST["txtDescripcion"]
    v_imagen = request.FILES["txtImagen"]

    Servicio.objects.create(
        nombre_servicio=v_nombre,
        descripcion=v_descripcion,
        encargado=v_empleado,
        precio=v_precio,
        imagenUrl=v_imagen,
    )
    return redirect("/taller/crud/servicios")


def eliminarServicio(request, serv_id):
    servicio = Servicio.objects.get(pk=serv_id)
    servicio.delete()
    return redirect("/taller/crud/servicios")


def cargarEditarServicio(request, serv_id):
    serv = Servicio.objects.get(pk=serv_id)
    empleados = Empleado.objects.all()
    template = loader.get_template("taller/editarServicio.html")
    context = {"servicio": serv, "empleados": empleados}
    return HttpResponse(template.render(context, request))


def editarServicio(request):
    v_empleado = Empleado.objects.get(rut=request.POST["cmbEmpleado"])

    v_sku = request.POST["txtSku"]
    servicioBD = Servicio.objects.get(pk=v_sku)
    v_nombre = request.POST["txtnombre"]
    v_precio = request.POST["txtprecio"]
    v_descripcion = request.POST["txtDescripcion"]

    servicioBD.nombre = v_nombre
    servicioBD.precio = v_precio
    servicioBD.descripcion = v_descripcion
    servicioBD.encargado = v_empleado

    servicioBD.save()

    return redirect("/taller/crud/servicios")


# Crud empleados


def crudEmpleados(request):
    vEmpleados = Empleado.objects.all
    vTipo = Tipo_empleado.objects.all
    vEstado = Estado_civil.objects.all
    vTaller = Taller.objects.all
    template = loader.get_template("taller/crudEmpleados.html")
    context = {"empleados": vEmpleados, "tipo": vTipo, "estadoCivil": vEstado, "taller": vTaller}
    return HttpResponse(template.render(context, request))


def agregarEmpleado(request):
    vRut = request.POST["txtRut"]
    vNombre = request.POST["txtnombre"]
    vApPaterno = request.POST["txtApPat"]
    vApMaterno = request.POST["txtApMat"]
    vNumero = request.POST["txtNumero"]
    vCorreo = request.POST["txtCorreo"]
    vDireccion = request.POST["txtDireccion"]
    vPassword = request.POST["txtPassword"]
    vTipo = Tipo_empleado.objects.get(pk=request.POST["cmbTipo"])
    vEstadoCivil = Estado_civil.objects.get(pk=request.POST["cmbCivil"])


    Empleado.objects.create_user(
    username = vRut, 
    email = vCorreo, 
    password = vPassword, )

    Empleado.rut = vRut
    Empleado.first_name = vNombre
    Empleado.last_name = vApPaterno
    Empleado.apellido_materno = vApMaterno
    Empleado.numero_contacto = vNumero 
    Empleado.direccion_vivienda = vDireccion
    Empleado.estado_civil = vEstadoCivil
    Empleado.tipo_empleado = vTipo

    Empleado.save(self=Empleado)

    return redirect("/taller/crud/empleados")


def eliminarEmpleado(request, rut):
    Empleado.objects.get(pk=rut).delete()
    return redirect("/taller/crud/empleados")


def cargarEditarEmpleado(request, rut):
    vEmpleado = Empleado.objects.get(pk=rut)
    vTipo = Tipo_empleado.objects.all()
    vCivil = Estado_civil.objects.all()
    template = loader.get_template("taller/editarEmpleado.html")
    context = {"empleado": vEmpleado, "tipo": vTipo, "estadoCivil": vCivil}
    return HttpResponse(template.render(context, request))


def editarEmpleado(request):
    empleadoBD = Empleado.objects.get(rut=request.POST["txtRut"])
    vNombre = request.POST["txtNombre"]
    vApPaterno = request.POST["txtApPat"]
    vApMaterno = request.POST["txtApMat"]
    vNumero = request.POST["txtNumero"]
    vCorreo = request.POST["txtCorreo"]
    vDireccion = request.POST["txtDireccion"]
    vTipo = Tipo_empleado.objects.get(pk=request.POST["cmbTipo"])
    vEstadoCivil = Estado_civil.objects.get(pk=request.POST["cmbCivil"])

    empleadoBD.nombre = vNombre
    empleadoBD.apellido_paterno = vApPaterno
    empleadoBD.apellido_materno = vApMaterno
    empleadoBD.numero_contacto = vNumero
    empleadoBD.correo_electronico = vCorreo
    empleadoBD.direccion_vivienda = vDireccion
    empleadoBD.estado_civil = vEstadoCivil
    empleadoBD.tipo_empleado = vTipo

    empleadoBD.save()

    return redirect("/taller/crud/empleados")


# Carrito y realizar compra
def carrito(request):
    template = loader.get_template("taller/carrito.html")
    context = {"hola": False}
    return HttpResponse(template.render(context, request))


def confirmarServicio(request):
    if request.method == "POST":
        data = request.POST.get("mi_dato")
        jdata = json.loads(data)

        print(jdata)

        return JsonResponse({"mensaje": "Datos recibidos correctamente."})
    else:
        return JsonResponse({"error": "Método no permitido"}, status=405)


# CRUD Proveedor


def crudProveedores(request):
    vRubros = Rubro.objects.all
    vProveedores = Proveedor.objects.all
    template = loader.get_template("taller/crudProveedores.html")
    context = {"proveedores": vProveedores, "rubros": vRubros}
    return HttpResponse(template.render(context, request))


def agregarRubro(request):
    v_nombre = request.POST["txtNombreRubro"]
    Rubro.objects.create(
        nombre_rubro=v_nombre,
    )

    return redirect("/taller/crud/proveedores")


def agregarProveedor(request):
    v_nombre = request.POST["txtNombreProveedor"]
    v_telefono = request.POST["txtTelefono"]
    v_correo = request.POST["txtCorreo"]
    v_rubro = Rubro.objects.get(pk=request.POST["cmbRubro"])
    v_extra = request.POST["txtDatosExtras"]

    Proveedor.objects.create(
        nombre_proveedor=v_nombre,
        rubro=v_rubro,
        telefono=v_telefono,
        correo_electronico=v_correo,
        informacion_extra=v_extra,
    )

    return redirect("/taller/crud/proveedores")


def eliminarProveedor(request, prov_id):
    Proveedor.objects.get(pk=prov_id).delete()
    return redirect("/taller/crud/proveedores")


# Inicio de sesion
def cargarInicioSesion(request):
    template = loader.get_template("taller/inicioSesion.html")
    context = {}
    return HttpResponse(template.render(context, request))


def iniciarSesion(request):
    correo = request.POST["txtCorreo"]
    password = request.POST["txtPassword"]

    try:
        usuario = Cliente.objects.get(correo_electronico=correo, password=password)
        login(request, usuario)
        print(usuario)
    except:
        usuario = Empleado.objects.get(correo_electronico=correo, password=password)
        login(request, usuario)
        print(usuario)

    return redirect("/taller")
