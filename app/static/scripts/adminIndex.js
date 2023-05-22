

const url ="http://127.0.0.1:3000/api/users/" //url dev
//const url = "http://34.208.161.62/api/users/" //url produccion


const cargarUsuarios = async () => {
    try {

        const response = await axios.get(url);
        const usuarios = response.data;

        const tbody = document.querySelector("tbody");

        usuarios.forEach((usuario)=>{
            const fila = document.createElement("tr");

            const id = document.createElement("td");
            id.textContent=usuario.id;
            fila.appendChild(id);

            const nombre = document.createElement("td");
            nombre.textContent=usuario.nombre;
            fila.appendChild(nombre);

            const telefono = document.createElement("td");
            telefono.textContent=usuario.numero_tel;
            fila.appendChild(telefono);

            const correo = document.createElement("td");
            correo.textContent=usuario.correo;
            fila.appendChild(correo);

            const nombreU = document.createElement("td");
            nombreU.textContent=usuario.nombre_usuario;
            fila.appendChild(nombreU);

            const fechaN = document.createElement("td");
            fechaN.textContent=usuario.f_nacimiento;
            fila.appendChild(fechaN);

            const activoD = document.createElement("td");
            activoD.textContent=usuario.activo_desde;
            fila.appendChild(activoD);

            const rol = document.createElement("td");
            rol.textContent=usuario.rol;
            fila.appendChild(rol);

            const botones = document.createElement("td");
        const editarBtn = document.createElement("button");
        editarBtn.textContent = "Editar";
        editarBtn.classList.add("editar");
        botones.appendChild(editarBtn);

        const eliminarBtn = document.createElement("button");
        eliminarBtn.textContent = "Eliminar";
        eliminarBtn.classList.add("eliminar");
        botones.appendChild(eliminarBtn);
        
        fila.appendChild(botones);

        tbody.appendChild(fila);

        });


    } catch (error) {
        console.log(error)
    }





};

cargarUsuarios();