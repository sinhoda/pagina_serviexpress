from django.http import Http404
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
import os
from django.conf import settings


from .models import *


def index(request):
    vProductos = Producto.objects.all
    template = loader.get_template("taller/index.html")
    context = {
        "productos": vProductos
    }
    
    return HttpResponse(template.render(context, request))

def ventaProducto(request, prod_id):
    template = loader.get_template("taller/ventaProducto.html")
    try:
        vProducto = Producto.objects.get(pk=prod_id)
        context = { "producto": vProducto}
    except Producto.DoesNotExist:
        raise Http404("Producto no existe")
    return HttpResponse(template.render(context, request))
    
#CRUD Productos

def crudProductos(request):
    vProductos = Producto.objects.all
    vCategorias = Categoria_producto.objects.all
    template = loader.get_template("taller/crudProductos.html")
    context = {
        "productos": vProductos, "categorias": vCategorias
    }
    return HttpResponse(template.render(context, request))

def eliminarProducto(request,prod_id):
    producto = Producto.objects.get(pk=prod_id)
    ruta_imagen = os.path.join(settings.MEDIA_ROOT, str(producto.imagenUrl))
    os.remove(ruta_imagen)
    producto.delete()
    return redirect('/taller/crud/productos')

def agregarCategoria(request):

    v_id = request.POST['txtIdCategoria']
    v_nombre = request.POST['txtnombreCategoria']


    Categoria_producto.objects.create(
        id_categoria = v_id, 
        nombre_categoria = v_nombre, 
        )
    
    return redirect('/taller/crud/productos')


def agregarProducto(request):
    v_categoria = Categoria_producto.objects.get(id_categoria = request.POST['cmbCategoria'])
    
    v_sku = request.POST['txtSku']
    v_nombre = request.POST['txtnombre']
    v_precio = request.POST['txtprecio']
    v_stock = request.POST['txtStock']
    v_descripcion = request.POST['txtDescripcion']
    v_imagen = request.FILES['txtImagen']

    Producto.objects.create(
        id_producto = v_sku, 
        nombre_producto = v_nombre, 
        precio = v_precio,
        stock = v_stock, 
        descripcion = v_descripcion, 
        imagenUrl=v_imagen,
        categoria = v_categoria
        )
    
    return redirect('/taller/crud/productos')

#Editar productos
def cargarEditarProducto(request, prod_id):
    prod = Producto.objects.get(pk = prod_id)
    categorias = Categoria_producto.objects.all()
    template = loader.get_template("taller/editarProducto.html")
    context = {"producto": prod, "categorias": categorias}
    return HttpResponse(template.render(context, request))


def editarProducto(request):
    v_categoria = Categoria_producto.objects.get(id_categoria = request.POST['cmbCategoria'])

    v_sku = request.POST['txtSku']
    productoBD = Producto.objects.get(pk = v_sku)
    v_nombre = request.POST['txtnombre']
    v_precio = request.POST['txtprecio']
    v_stock = request.POST['txtStock']
    v_descripcion = request.POST['txtDescripcion']


    try:
        v_imagen = request.FILES['txtImagen']
        ruta_imagen = os.path.join(settings.MEDIA_ROOT, str(productoBD.imagenUrl))
        os.remove(ruta_imagen)
    except:
        v_imagen = productoBD.imagenUrl

    productoBD.nombre = v_nombre
    productoBD.precio = v_precio
    productoBD.stock = v_stock
    productoBD.descripcion = v_descripcion
    productoBD.categoriaId = v_categoria
    productoBD.imagenUrl = v_imagen
    
    productoBD.save()

    return redirect('/tienda/crudProductos')



# Servicios

def crudServicios(request):
    vServicios = Servicio.objects.all
    vEmpleados = Empleado.objects.all
    template = loader.get_template("taller/crudServicios.html")
    context = {
        "servicios": vServicios, "empleados": vEmpleados
    }
    return HttpResponse(template.render(context, request))

def agregarServicio(request):    
    v_empleado = Empleado.objects.get(pk = request.POST['cmbEncargado'])
    v_id = request.POST['txtIdServicio']
    v_nombre = request.POST['txtnombre']
    v_precio = request.POST['txtprecio']
    v_descripcion = request.POST['txtDescripcion']

    Servicio.objects.create(
        id_servicio = v_id, 
        nombre_servicio = v_nombre, 
        descripcion = v_descripcion, 
        encargado = v_empleado,
        precio = v_precio,        
    )
    return redirect('/taller/crud/servicios')