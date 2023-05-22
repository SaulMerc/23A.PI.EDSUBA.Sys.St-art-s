/**
 * Script para los index dentro de templates
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


  const cargarCat = async() => {
    const url = "http://127.0.0.1:3000/api/category/";
    
  
    try {
      const response = await axios.get(url);
      const categorias = response.data;
      const cats = document.querySelector("#cats");
      categorias.forEach((categoria) => {
        const lis = document.createElement('li');
        const link = document.createElement('a');
        link.href='../pages/search.html';
        link.textContent = categoria.categoria;
        lis.appendChild(link);
        cats.appendChild(lis);
      });
    } catch (error) {
      console.log(error);
    }
  };
  cargarCat();