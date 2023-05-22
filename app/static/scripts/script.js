/**
 * Carga de sesion iniciada o iniciar sesion
 */
//Carga de la pagina iniciada sesion o no
window.addEventListener("load", () => {
  const header = document.querySelector(".login");
  const loged =
  '<img src="" alt="" class="imgUser">'+
  '<ul class="bcSec">'+
      '<li><a href="../static/pages/sell.html" class="cBlack">Vender</a></li>'+
      '<li><a href="../static/pages/sell.html" class="cBlack">Avisos</a></li>'+
      '<li><a href="../static/pages/edProd.html" class="cBlack">Editar productos</a></li>'+
      '<li><a href="../static/pages/edArt.html" class="cBlack">Editar perfil</a></li>'+
      '<li><button type="button" id="clS" class="unset">Cerrar sesión</button></li>'+
  '</ul>';
  const nologed = '<a href="../static/pages/signIn.html">Iniciar sesión</a>&nbsp;&nbsp;'+
  '<a href="../static/pages/signUp.html">Registrarse</a>';
  if (localStorage.getItem('id') != null) {
    header.classList.add('nav');
    header.innerHTML = loged;
    ses = true;
  }else{
    header.innerHTML = nologed;
    ses = false;
  }
  var clS = document.querySelector("#clS")

  clS.addEventListener('click', ()=>{ 
    localStorage.removeItem('id');
    location.reload();
  })
});


// Obtener elementos del DOM
const sidebar = document.querySelector('.sidebar');
const toggleBtn = document.querySelector('.menu');

// Función para abrir/cerrar la barra lateral
function toggleSidebar() {
  sidebar.classList.toggle('sidebar-open');
}

// Agregar evento de clic al botón de alternar
toggleBtn.addEventListener('click', toggleSidebar);

const darkModeToggle = document.querySelector('#dark__ModeToggle');

darkModeToggle.addEventListener('click', () => {
  document.body.classList.toggle('dark__Mode');

  if (document.body.classList.contains('dark__Mode')) {
    localStorage.setItem('dark-mode', 'true');

  }else{
    localStorage.setItem('dark-mode', 'false');
  }
});

if (localStorage.getItem('dark-mode') === 'true') {
document.body.classList.add('dark__Mode');
}else{
document.body.classList.remove('dark__Mode');
}



// var clS = document.querySelector("#clS")

// clS.addEventListener('click', (event)=>{
//   event.preventDefault(); 
//   cerrarSesion();
// })
