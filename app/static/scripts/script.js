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



