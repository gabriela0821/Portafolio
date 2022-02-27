const inputs = document.querySelectorAll('.input');

function focusFunc(){
    let parent = this.parentNode.parentNode;
    parent.classList.add('focus')
}

inputs.forEach(input => {
    input.addEventListener('focus', focusFunc);
});


function btnGuardar(){
    let nombre = document.getElementById("nombre").value;
    let contraseña = document.getElementById("contraseña").value;

    let datosPersona = {
        "datosPersonales": {
            "nombre": nombre,
            "contraseña": contraseña
        }
    }
    
    console.log(datosPersona);


}