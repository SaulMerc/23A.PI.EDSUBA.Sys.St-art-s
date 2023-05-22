

const iniciarSesion = async() => {
  try {
    var correo = document.getElementById("correo").value;
     var password = document.getElementById("password").value;
    if (correo == "" || password == "") {
      alert("Por favor ingresa tu usuario y tu contraseña")
      return;
    }
   
    //const url = "http://34.208.161.62/api/addUser/"    //prod
    const url = "http://127.0.0.1:3000/api/login/" //Dev
    
    body = {
      "correo":correo,
      "contrasena" : password
    }
  
    const respuesta = await axios.post(url,body,{
      headers:{
        "Content-Type": "application/json",
        'Access-Control-Allow-Origin': "*"
      }
      });

      const {status , data} = respuesta;
      
    if(status==200){
      alert("Inicio de sesion exitoso")
      localStorage.setItem('id', data)
      window.location.href = "/";
    }else{
      alert("No se encontro el usuario")
    }
    





  } catch (error) {
    alert("Ups... Creo que algo salio mal, verifica tu usuario y tu contraseña");
  }
 

}



var submitsingIn = document.querySelector("#in");
submitsingIn.addEventListener('click',(event) => {
    event.preventDefault(); 
    iniciarSesion();
  });





// function login() {
//     event.preventDefault(); 
//     var username = document.getElementById("username").value;
//     var password = document.getElementById("password").value;
    
//     iniciarSesion(username,password);
//     // Comprueba si los campos de nombre de usuario y contraseña están vacíos
  
//   }
  