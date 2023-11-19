$(function(){
    if(localStorage.getItem("carrito") == null)
    {
        console.log("chao");
        let carrito = []
        localStorage.setItem("carrito", JSON.stringify(carrito))
    }    
})

$("#btnCantidadComprar").on("click", function(){
    let carrito = JSON.parse(localStorage.getItem("carrito"))
    
    console.log(carrito);

    //Obtener valores de html
    let idProducto = $("#idProducto").val()
    console.log(idProducto);
    let nombreProducto = $("#nombreProducto").val()
    console.log(nombreProducto);
    let precioProducto = $("#precioProducto").val()
    console.log(precioProducto);
    let vCantidad = Number( $("#cantidadComprarTxt").val())
    console.log(vCantidad);
    let imagenProducto =  $("#imagenProducto").val()
    console.log(imagenProducto);


    //Agregar a localstorage
    if (carrito.length == 0){
        const obj = {
            id_producto: idProducto,
            nombre: nombreProducto,
            precio: precioProducto,
            imagen: imagenProducto,
            cantidad: vCantidad
        }
        carrito.push(obj)
    }
    else{
        let index = carrito.findIndex(object => {
            return object.id_producto === idProducto;
        })
        if (index == -1){
            const obj = {
                id_producto: idProducto,
                nombre: nombreProducto,
                precio: precioProducto,
                imagen: imagenProducto,
                cantidad: vCantidad
            }
            carrito.push(obj)
        }
        else{
            carrito[index].cantidad     = carrito[index].cantidad + vCantidad;
        }
    }

    localStorage.setItem("carrito", JSON.stringify(carrito));
})






