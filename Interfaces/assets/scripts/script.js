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
});


//mostrarD
//Funcion del modal para la dirección
const bModalD = document.querySelector(".closeD");
const modalD = document.querySelector("#modalD");
const bAddD = document.querySelector("#mostrarD");

bModalD.addEventListener('click', showD);
bAddD.addEventListener('click', hideD);

function showD(){
  modalD.classList.add("oculto");
}
function hideD(){
  modalD.classList.remove("oculto");
}

//mostarP
//Funcion del modal para agregar el método de pago
const bModal = document.querySelector(".closeP");
const modal = document.querySelector("#modalP");
const bAddP = document.querySelector("#mostrarP");

bModal.addEventListener('click', showP);
bAddP.addEventListener('click', hideP);

function showP(){
  modal.classList.add("oculto");
}
function hideP(){
  modal.classList.remove("oculto");
}
