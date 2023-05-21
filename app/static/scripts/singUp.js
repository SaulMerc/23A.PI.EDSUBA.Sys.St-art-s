//date , nTel,   nUser,  acercaDe, mail, pass, passR, reg, term

const validarContraseña = (contrasena)=>{
    
    if(!contrasena.lenght > 7){
        return false;
    }
    
    if (!/\d/.test(contrasena)) {
        return false;
    }

    if (!/[A-Z]/.test(contrasena)) {
        return false;
    }

    return true;
      
}

var redi  = true;
const addUser = async()=> {
    try {
        var nombre = document.getElementById("nCom").value,
        fechaNacimiento = document.getElementById("date").value,
        numeroTelefono = document.getElementById("nTel").value,
        nombreUsuario= document.getElementById("nUser").value,
        acercaDe = document.getElementById("acercaDe").value,
        email = document.getElementById("mail").value,
        pass = document.getElementById("pass").value,
        passR = document.getElementById("passR").value,
        termCheckbox = document.getElementById("term");

    const body = {
        "correo" : email,
        "f_nacimiento":fechaNacimiento,
        "nombre": nombre,
        "nombre_usuario": nombreUsuario,
        "numero_tel": numeroTelefono,
        "acerca_mi": acercaDe,
        "contrasena" : pass
    };
    const url = "http://127.0.0.1:8000/api/addUser/";
    
    if (!validarContraseña(pass)) {
        alert("La contraseña debe tener al menos un número y una mayúscula y ser mayor a 7 caracteres");
        return;
      }
  
      if (!termCheckbox.checked) {
        alert("Debe aceptar los términos y condiciones");
        return;
      }
  
      if (pass !== passR) {
        alert("Las contraseñas no coinciden");
        return;
      }
  
      const respuesta = await axios.post(url, body, {
        headers: {
          "Content-Type": "application/json",
          'Access-Control-Allow-Origin': "*"
        }
      });
      alert("Usuario creado con exito")
      window.location.href = "../pages/signIn.html";

    } catch (error) {
        console.log(error)
    }
    
    
    }


    
  
    

    const valSpBlank = ()=>{
        spB = true;
        if (nombre === ""||fechaNacimiento === "" ||numeroTelefono === ""|| nombreUsuario === ""|| email === ""|| pass === ""|| passR === "") {
            alert("Rellene los espacios en blanco");
            return spB = false;
        } else {
            spB = false;
        }
        return spB;
    }



        var submitFormulario = document.querySelector("#reg");
        submitFormulario.addEventListener('click',(event) => {
            event.preventDefault(); 
            addUser();
          });