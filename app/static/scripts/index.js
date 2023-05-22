function cargar(){
    const main = document.querySelector(".gridM")
const div = document.createElement("div")
const a = document.createElement("a")
const img = document.createElement("img")
const h2 = document.createElement("h2")
const h3 = document.createElement("h3")
const h4= document.createElement("h4")
const p = document.createElement("p")

div.classList.add("card__Large")
div.classList.add("grid__shop")

a.href = "../static/pages/product.html"

img.classList.add("grid__image")
img.classList.add("img__card")
img.classList.add("img__cardG")
img.src = "../static/images/logo.png"



h2.textContent="Nombre del autor"
h2.classList.add("grid__author")
h3.textContent="Nombre de la obra"
h3.classList.add("grid__obName")

h4.textContent="Categoria"
h4.classList.add("grid__cat")
p.textContent= "price"
p.classList.add("grid__price")

a.appendChild(img)
div.appendChild(a)
div.appendChild(h2)
div.appendChild(h3)
div.appendChild(h4)
div.appendChild(p)
main.appendChild(div)
}
cargar()