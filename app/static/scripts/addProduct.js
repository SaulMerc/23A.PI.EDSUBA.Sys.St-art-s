//cat pic obr desc pri ext        addProd
 

const cargarCategorias = async() => {
    const url = "http://127.0.0.1:3000/api/category/";
    const selectCat = document.querySelector("#cat");
  
    try {
      const response = await axios.get(url);
      const categorias = response.data;
  
      categorias.forEach((categoria) => {
        const option = document.createElement("option");
        option.value = categoria.categoria;
        option.textContent = categoria.categoria;
        selectCat.appendChild(option);
      });
    } catch (error) {
      console.log(error);
    }
  };


  document.addEventListener("DOMContentLoaded", cargarCategorias);  

  document.getElementById('productForm').addEventListener('click', async function(e) {
    e.preventDefault(); // Evita que se envíe el formulario de manera tradicional
  
    var form = new FormData(this); // Crea un objeto FormData con los datos del formulario
  
    try {
      const response = await axios.post('http://127.0.0.1:3000/api/addProduct/', form, {
        headers: {
          'Content-Type': 'multipart/form-data',// Establece el encabezado Content-Type adecuado
          'Access-Control-Allow-Origin': "*" 
        }
      });
      console.log(response.data.mensaje);
    } catch (error) {
      console.log('Error al agregar el producto');
    }
  });
  



//cat pic obr desc pri ext        addProd

// const addProd = async()=> {
//     try {
//         var categoria = document.getElementById("cat").value,
//         titulo = document.getElementById("obr").value,
//         descripcion = document.getElementById("desc").value,
//         precio = document.getElementById("pri").value,
//         existencia = document.getElementById("ext").value,
//         usuario = localStorage.getItem("id");


//     const body = {
//         "id_user" : usuario,
//         "titulo":titulo,
//         "descripcion": descripcion,
//         "existencia": existencia,
//         "precio": precio,
//         "categoria": categoria,
//     };
//     //const url = "http://34.208.161.62/api/addUser/"; // url produccion
//     const url = "http://127.0.0.1:3000/api/addProduct/"; // url dev
    
//       const respuesta = await axios.post(url, body, {
//         headers: {
//           "Content-Type": "application/json",
//           'Access-Control-Allow-Origin': "*"
//         }
//         });
//         alert("Producto agregado con exito")
//         location.reload(); 
//         console.log(respuesta)
//     } catch (error) {
//         console.log(error)
//     }
    
    
//     }

//     // const addImage = () => {
//     //     const url = "http://127.0.0.1:3000/api/addProd/" //dev
//     //     //url = //produccion


//     // }

//     var submitFormulario = document.querySelector("#addProd");
//     submitFormulario.addEventListener('click',(event) => {
//         event.preventDefault(); 
//         addProd();
//       });
  
    

    



       


          
