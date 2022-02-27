<?php

    include_once 'conexion.php';
    #Conectamos con MySQL (en este caso es para un localhost)
    #$conexion = mysql_connect("localhost","root","root")
    #or die ("Fallo en el establecimiento de la conexión");
    #
    ##Seleccionamos la base de datos a utilizar
    #mysql_select_db("pruebas")
    #or die("Error en la selección de la base de datos");
    
    #Guardamos la variable enviada por POST#
    alert("hola")
    echo "<script> alert('contraseña recuperada');window.location= 'help.php' </script>";
    if(!isset($_POST['cat'])){
        echo "<script> alert('contraseña recuperada');window.location= 'help.php' </script>";
    }
    #if($cat==SMTP){
    #    console.log("entro al if cat");
    #    header("captura_de_servicios_smtp.php");
    #}
    #else{
    #    echo "<script> alert('cate error');window.location= 'captura_de_servicios_smtp.php' </script>";
    #}
    
    #$result = mysql_query ("select * from productos where categoria = '$cat'" )
    #or die("Error en la consulta SQL");
    
    
 
    
 
    mysql_close($conexion);

?>