$(document).ready(function () {
    $("#mensaje").hide();
    $("#formulario").submit(function () {
        var error = "";
        if ($("#nombre").val().trim().length == 0) {
            error += "Debe Ingresar un nombre</br>"
            $("#nombre").addClass("colorearError");
        } else {
            $("#nombre").removeClass("colorearError");
        }
        if ($("#email").val().trim().length == 0) {
            error += "Debe Ingresar un correo</br>"
            $("#email").addClass("colorearError");
        } else {
            $("#email").removeClass("colorearError");
        }
  
        if ($("#pass").val().trim().length == 0) {
            error += "Debe Ingresar una Contraseña</br>"
            $("#pass").addClass("colorearError");
        } else {
            $("#pass").removeClass("colorearError");
        }
        if ($("#pass2").val().trim().length == 0) {
            error += "Debe Ingresar nuevamente la contraseña</br>"
            $("#pass2").addClass("colorearError");
        } else {
            $("#pass2").removeClass("colorearError");
        }
  
        if ($("#pass").val() != $("#pass2").val()) {
            error += "Las contraseñas ingresadas no coinciden</br>"
            $("#pass").addClass("colorearError");
            $("#pass2").addClass("colorearError");
        }
  
  
        if ($("#texto").val().trim().length == 0) {
            error += "Debe Ingresar un Comentario</br>"
            $("#texto").addClass("colorearError");
        } else {
            $("#texto").removeClass("colorearError");
        }
  
        if (error != "") {
            $("#mensaje").html(error);
            $("#mensaje").show();
            event.preventDefault();
        }
    });
  });