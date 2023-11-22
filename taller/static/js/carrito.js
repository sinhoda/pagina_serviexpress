$(function () {    
    if (localStorage.getItem("carrito") == null) {
        localStorage.setItem("carrito", JSON.stringify([]))
        console.log("no hay items");
        let contCarrito = $("#containerCarrito");
        let html = $(`<h1> No se han agregado servicios al carrito   </h1>`)        
        contCarrito.append(html)
    } else {
        console.log("si hay items");
        cargar()
       
    }


    $("#btnComprar").on("click", function(){
        let carrito = JSON.parse(localStorage.getItem("carrito"))
        let productos = [];
        carrito.forEach(p => {
            let producto = {
                "id": p.id_servicio,
            }
            productos.push(producto)
        });

        var csrfToken = $(this).data("csrf-token");
        var datos = {
            mi_dato: JSON.stringify(productos),
            csrfmiddlewaretoken: csrfToken,
        };
        

        $.ajax({
            type: 'POST',
            url: 'carrito/confirmarServicio',
            data: datos,
            success: function(response) {
                console.log(response);
                // Manejar la respuesta del servidor aquí
            },
            error: function(error) {
                console.log(error);
                // Manejar errores aquí
            }
        });
    })

})


function quitarCantidad(codigo){    
    let arrayTemporal = [];
    let carrito = JSON.parse(localStorage.getItem("carrito"));
    console.log(carrito);

    let index = carrito.findIndex(object => {
        return object.id_producto == codigo;
    })
    
    carrito[index].cantidad -= 1;   

    carrito.forEach(producto => {
        if (producto.cantidad > 0){
            arrayTemporal.push(producto)
        }
    });

    console.log(arrayTemporal);


    if (carrito[index].cantidad <= 0){
        $(`#prodCod${codigo}`).remove()

    } 

    localStorage.setItem("carrito", JSON.stringify(arrayTemporal)) 
    cargar()
    
}



function agregarCantidad(codigo){
    let carrito =  JSON.parse( localStorage.getItem("carrito"));    
    let index = carrito.findIndex(object => {
        return object.id_producto == codigo;
    })

    carrito[index].cantidad =  carrito[index].cantidad  + 1;   
    
    console.log(carrito);

    localStorage.setItem("carrito", JSON.stringify(carrito));  

    
    cargar()
    
};


function totalCarrito(){
    let carrito = JSON.parse(localStorage.getItem("carrito"));
    let totalCarrito = 0;
    carrito.forEach(servicio => {
    totalCarrito += Number(servicio.precio)
    });
    $("#totalPagar").text(`$${totalCarrito}`)
}


function cargar() {
    $(".rowProducto").remove();
    let carrito = JSON.parse(localStorage.getItem("carrito"));
    console.log(carrito);
    if (carrito.length <= 0) {
        let contCarrito = $("#containerCarrito");
        let html = $(`<h1> No se han agregado servicios al carrito   </h1>`);
        contCarrito.append(html);
    } else {
        let contCarrito = $("#containerCarrito");
        for (const c of carrito) {
            let idServicio = c.id_servicio; // Corregido aquí
            let nombreServicio = c.nombre;
            let precioServicio = c.precio;
            let imagenServicio = c.imagen;

            console.log(idServicio);

            let html = $(`<div id="servCod${idServicio}" class="row mt-3 rowProducto text">
                <div class="col">
                    <img class="imgCarrito" src=${imagenServicio} alt="" srcset="" width="100px" height="100px">
                </div>
                <div class="col text-center">
                    <p id="nombreServicio">${nombreServicio}</p>
                </div>
                <div class="col">
                    <p id="precioUnitario${idServicio}" class="p"> $${precioServicio}</p>
                </div>
            </div>`);
            contCarrito.append(html);
        }
        totalCarrito();
    }
}
