$(function () {
    console.log("hola mundo");
    if (localStorage.getItem("carrito") == null) {
        console.log("chao");
        let carrito = []
        localStorage.setItem("carrito", JSON.stringify(carrito))
    }
})


$("#btnAddServicio").on("click", function () {
    let carrito = JSON.parse(localStorage.getItem("carrito"))

    console.log(carrito);

    //Obtener valores de html
    let idServicio = $("#idServicio").val()
    console.log(idServicio);
    let nombreServicio = $("#nombreServicio").val()
    console.log(nombreServicio);
    let precioServicio = $("#precioServicio").val()
    console.log(precioServicio);
    let imagenServicio = $("#imagenServicio").val()
    console.log(imagenServicio);
    

    //Agregar a localstorage
    if (carrito.length == 0) {
        const obj = {
            id_servicio: idServicio,
            nombre: nombreServicio,
            precio: precioServicio,
            imagen: imagenServicio,
            
        }
        carrito.push(obj)
    }
    else {
        let index = carrito.findIndex(object => {
            return object.id_servicio === idServicio;
        })
        if (index == -1) {
            const obj = {
                id_servicio: idServicio,
                nombre: nombreServicio,
                precio: precioServicio,
                imagen: imagenServicio,
            }
            carrito.push(obj)
        }        
        
    }

    localStorage.setItem("carrito", JSON.stringify(carrito));
    
   
})



$("#btnAddServicio").on("click", function Mensaje() {
    let carrito = JSON.parse(localStorage.getItem("carrito"))
    let index = carrito.findIndex(object => {
        return object.id_servicio === idServicio;
    })


    const msgDiv = $("#msgAgregar")

    if (msgDiv.attr('id') == "msgAgregar") {
        console.log("ya existe");
        msgDiv.remove()
    }

    const alertPlaceholder = document.getElementById('liveAlertPlaceholder')
    const appendAlert = (message, type) => {
        const wrapper = document.createElement('div')
            wrapper.innerHTML = [
                `<div id="msgAgregar" class="alert alert-${type} alert-dismissible" role="alert">`,
                `   <div>${message}</div>`,
                '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
                '</div>'
            ].join('')
        
        

        alertPlaceholder.append(wrapper)
    }
    
        appendAlert('Servicio agregado correctamente', 'success')
    
    

    
    setTimeout(eliminarMensaje, 5000)
})


function eliminarMensaje() {
    const msgEliminar = $("#msgAgregar")
    if (msgEliminar.attr('id') == "msgAgregar") {
        msgEliminar.remove();
    }
}