const btn = document.getElementById("com")
const com = document.getElementById("comentario")

btn.addEventListener('click', ()=>{
    if (com.value === "") {
        alert("Inserta tu opinion en el comentario")
    }else{
        const comm = document.getElementById("comments")
    const val = document.createElement("div")
    const text = document.createElement("p")

    val.classList.add("cardDef")
    val.classList.add("bcWhite")
    text.textContent= com.value;

    val.appendChild(text)
    comm.appendChild(val)
    }


});
