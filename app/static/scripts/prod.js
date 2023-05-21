(function(){

//Funcion del modal para agregar al carrito
const cl = document.querySelector(".close");
const modal = document.querySelector(".alert");
let clic = false;

    const addCart = document.querySelector("#addCart");
    addCart.addEventListener('click', ()=>{
                if (clic ==false) {
                    //Aviso o alerta cuando se agregue al carrito
                var alert = document.getElementById("alerts");
                var newP = document.createElement('p');
                var cl = document.createElement('span');
                modal.classList.remove("oculto");
                
                newP.textContent = "Elemento agregado al carrito!!!";
                cl.classList.add("close");
                alert.appendChild(newP);
                alert.appendChild(cl);
                clic =  true;
                }else if (clic == true) {
                    modal.classList.remove("oculto");
                }
                cl.addEventListener('click', ()=>{
                    modal.classList.add("oculto");
                });
    });

})();
