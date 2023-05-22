window.addEventListener("load", () => {
    const header = document.querySelector(".login");
    const loged =
    '<img src="" alt="" class="imgUser">'+
    '<ul class="bcSec">'+
        '<li><button type="button" id="clS" class="unset">Cerrar sesión</button></li>'+
    '</ul>';
    if (localStorage.getItem('id') != null) {
      header.classList.add('nav');
      header.innerHTML = loged;
      ses = true;
    }
    var clS = document.querySelector("#clS")
  
    clS.addEventListener('click', ()=>{ 
      localStorage.removeItem('id');
      location.reload();
    })
  });
