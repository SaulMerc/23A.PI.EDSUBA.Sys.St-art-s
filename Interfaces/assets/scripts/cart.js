//Redireccionar con el boton a otro pagina
const redPay = document.querySelector("#pPay");

redPay.addEventListener('click', function(){
    setTimeout(function(){
    window.location.href = "procPay.html";
    },1000)
});
