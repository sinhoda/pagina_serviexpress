$(function () {    
    if (localStorage.getItem("carrito") == null) {
        localStorage.setItem("carrito", JSON.stringify([]))
        console.log("no hay items");
        let contCarrito = $("#containerCarrito");
        let html = $(`<h1> No se han agregado productos al carrito   </h1>`)        
        contCarrito.append(html)
    } else {
        console.log("si hay items");
        cargar()
       
    }


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
    carrito.forEach(producto => {
    totalCarrito += producto.precio * producto.cantidad
    });
    $("#totalPagar").text(`$${totalCarrito}`)
}


function cargar(){
    $(".rowProducto").remove()
    let carrito = JSON.parse(localStorage.getItem("carrito"))
        console.log(carrito);
        if(carrito.length <= 0){
            let contCarrito = $("#containerCarrito");
            let html = $(`<h1> No se han agregado productos al carrito   </h1>`)        
            contCarrito.append(html)

        } else{

            let contCarrito = $("#containerCarrito");
        for (const c of carrito) {
            let idProducto  = c.id_producto;
            let nombreProducto =   c.nombre;
            let precioProducto = c.precio;
            let imagenProducto =c.imagen;
            let vCantidad = c.cantidad;
            let precioTotal = precioProducto * vCantidad;

            console.log(idProducto);

            let html = $(`<div id="prodCod${idProducto}" class="row mt-3 rowProducto text">
        <div class="col">
            <img class="imgCarrito" src=${imagenProducto} alt="" srcset="" width="100px" height="100px">
        </div>
        <div class="col text-center">
            <p id="nombreProducto">${nombreProducto}</p>
        </div>
        <div class="col">
            <p id="cantidadProductos${idProducto}"> ${vCantidad} </p>
            <button onclick="quitarCantidad(${idProducto})" id="btnQuitarCantidad" class="btn btn-danger"> 
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-dash-circle-fill" viewBox="0 0 16 16">
            <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM4.5 7.5a.5.5 0 0 0 0 1h7a.5.5 0 0 0 0-1h-7z"/>
          </svg>
          </button>
            <button onclick="agregarCantidad(${idProducto})" id="btnAgregarCantidad" class="btn btn-success">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-plus-circle-fill" viewBox="0 0 16 16">
            <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8.5 4.5a.5.5 0 0 0-1 0v3h-3a.5.5 0 0 0 0 1h3v3a.5.5 0 0 0 1 0v-3h3a.5.5 0 0 0 0-1h-3v-3z"/>
          </svg>
            </button>  
            
        </div>
        <div class="col">
            <p id="precioUnitario${idProducto}" class="p"> $${precioProducto}</p>
        </div>
        <div class="col">
            <p id="precioTotal${idProducto}" class="p">$${precioTotal}</p>
        </div>
        <input value="${idProducto}" id="idProductoTxt" type="number" hidden>
        </div>`);
        
            contCarrito.append(html);
        }
        totalCarrito()

        }

        
}

