'use stric'

//Devuelve true or dr false dependiendo si es aceptada o no
var confirmacion = confirm("Estas seguro de continuar?");

//Salida por ventana emergente
alert("Esto es una alerta");

//Entrada de datos
var edad = prompt("Introduzca edad:");

// Salida de datos leyendo desde una variable
alert("La edad introducida es: " + edad);


console.log("Esto es un mensaje en la consola");

// Salida de datos al BODY de mi página
document.write("<h1>Esto es un H1 puesto desde JavaScript</h1>");

var precio=30000;
var dinero=prompt("Introduce cuanto dinero tienes: ");
if(dinero>precio){
alert("Te puedes comprar el coche");
}else{
alert("Te vas en autobus");
}

var num1=prompt("Introduce numero");
var num2=prompt("Introduce numero2");
if(!isNaN(num1)&&!isNaN(num2)){
alert(parseInt(num1)+parseInt(num2));
}else{
alert("No has introducido números");
}

document.write("<ul>");
var nombres=["Angel", "Sara","Manolo", "Ana"];
nombres.forEach((elemento)=>{
document.write("<li>"+elemento+"</li>");
});
document.write("</ul>");




