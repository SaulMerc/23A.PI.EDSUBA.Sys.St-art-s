
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

