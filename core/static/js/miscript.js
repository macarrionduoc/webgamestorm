
//FUNCION PARA VALIDAR FORMATO DE LA CONTRASEÑA (Que sea de un minimo de 4 caracteres, que contenga 1 mayuscula y 1 numero)
function validarContrasena(inputPassword) {
  // variable de requisitos
  var regex = /^(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{4,}$/;
  // si cumple los requisitos, se devuelve true
  if (regex.test(inputPassword)) {
    return true;
  }
  // si no, devuelve false
  else {
    return false;
  }
}
var formulario = document.getElementById("formulario");
formulario.addEventListener("submit", function(event) {
  // se obtiene el valor de la contraseña ingresada
  var inputPassword = document.getElementById("inputPassword").value;
  // se llama a la función que valida la contraseña y guardar el resultado
  var valido = validarContrasena(inputPassword);
  // si el resultado es falso, se mostrara un mensaje o alerta de error
  if (!valido) {
    alert("La contraseña debe tener al menos 4 caracteres, una mayúscula y un número");
    event.preventDefault();
  }
});
