function login() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
  
    // Comprueba si los campos de nombre de usuario y contraseña están vacíos
    if (username == "" || password == "") {
      alert("Por favor ingrese nombre de correo y contraseña");
      return false;
    }
    else {
      // Lógica de inicio de sesión aquí
      // Si los detalles de inicio de sesión son correctos, redirigir al usuario a la página principal
      // De lo contrario, se mostrará un mensaje de error
      alert("Inicio de sesión exitoso");
      return true;
    }
  }
  