




const cargarRoles = async() => {
    const url = "http://127.0.0.1:3000/api/rol/";
    try {
        const response = await axios.get(url);
        const roles = response.data;
    
        const tbody = document.querySelector("#tablaRol tbody");
    
        roles.forEach((role) => {
          const fila = document.createElement("tr");
    
          const id = document.createElement("td");
          id.textContent = role.id;
          fila.appendChild(id);
    
          const rol = document.createElement("td");
          rol.textContent = role.rol;
          fila.appendChild(rol);
    
          const descripcion = document.createElement("td");
          descripcion.textContent = role.descripcion;
          fila.appendChild(descripcion);
    
          const botones = document.createElement("td");
          const eliminarBtn = document.createElement("button");
          eliminarBtn.textContent = "Eliminar";
          eliminarBtn.classList.add("eliminar");
          eliminarBtn.id = role.id;
          botones.appendChild(eliminarBtn);
    
          fila.appendChild(botones);
    
          tbody.appendChild(fila);
        });
      } catch (error) {
        console.log(error);
      }


}






const cargarCategorias = async() => {
    const url = "http://127.0.0.1:3000/api/category/";
    try {
        const response = await axios.get(url);
        const categorias = response.data;
    
        const tbody = document.querySelector("#tablaCategoria");
    
        categorias.forEach((categoria) => {
          const fila = document.createElement("tr");
    
          const id = document.createElement("td");
          id.textContent = categoria.id;
          fila.appendChild(id);
          
          const nombre = document.createElement("td");
          nombre.textContent = categoria.categoria;
          fila.appendChild(nombre);
    
          const botones = document.createElement("td");
          const eliminarBtn = document.createElement("button");
          eliminarBtn.textContent = "Eliminar";
          eliminarBtn.classList.add("eliminar");
          eliminarBtn.id = categoria.id;
          botones.appendChild(eliminarBtn);
    
          fila.appendChild(botones);
    
          tbody.appendChild(fila);
        });


      } catch (error) {
        console.log(error);
      }
    };
    


   

async function agregarCategoria() {

    const url = "http://127.0.0.1:3000/api/addCategory";


  const categoria = document.querySelector("#categoria").value;
  
  const body = {
    "categoria" : categoria
  }
  try {
    const response = await axios.post(url, body , {
        headers:{
          "Content-Type": "application/json",
          'Access-Control-Allow-Origin': "*"
        }
        });
    console.log(response); // Aquí puedes realizar alguna acción con la respuesta

    // Limpiar el formulario después de agregar la categoría
    categoriaInput.value = "";

    // Opcional: Recargar la tabla para mostrar la nueva categoría
    cargarRoles();
  } catch (error) {
    console.log(error);
  }
}
    const formularioCategoria = document.querySelector("#formCat");
    formularioCategoria.addEventListener('click',(event) => {
        event.preventDefault(); 
        agregarCategoria();
      });



      async function agregarRol() {

        const url = "http://127.0.0.1:3000/api/addRol";
    
    
      const rol = document.querySelector("#rol").value;
      const desc = document.querySelector("#desc").value;
      
      const body = {
        "rol" : rol,
        "descripcion" : desc
      }
      try {
        const response = await axios.post(url, body , {
            headers:{
              "Content-Type": "application/json",
              'Access-Control-Allow-Origin': "*"
            }
            });
        console.log(response); // Aquí puedes realizar alguna acción con la respuesta
    
        // Limpiar el formulario después de agregar la categoría
        categoriaInput.value = "";
    
        // Opcional: Recargar la tabla para mostrar la nueva categoría
        cargarCategorias();
      } catch (error) {
        console.log(error);
      }
    }
        const formularioRol = document.querySelector("#nuevoRol");
        formularioRol.addEventListener('click',(event) => {
            event.preventDefault(); 
            agregarRol();
          });



    cargarCategorias();
    cargarRoles();