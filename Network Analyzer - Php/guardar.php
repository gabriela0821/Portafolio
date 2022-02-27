<?php
  
    include "conexion.php";
    
    $id  = 0;
    $nombre  = $_POST['usuario'];
    $contrasena  = $_POST['contrasena'];
    $respuesta = $_POST['respuesta'];
    $rol = 3;



    
    $query="SELECT * FROM usuario WHERE nombre_usuario='$nombre'";  
    $consulta = mysqli_query($connection, $query);
    $cantidad = mysqli_num_rows($consulta);

    if($cantidad>0){
        echo "<script> alert('nombre de usuario no disponible');window.location= 'registro.html' </script>";

    }else{

        $_SESSION['nombre_usuario']=$usuario;
        //insertamos datos de registro al mysql xamp, indicando nombre de la tabla y sus atributos
        $instruccion_SQL = "INSERT INTO usuario(idusuario, nombre_usuario, contrasena, respuesta_seg, rol_id_rol) 
        VALUES ('$id','$nombre','$contrasena','$respuesta','$rol')";
        $resultado = mysqli_query($connection,$instruccion_SQL);
        header("location: index.php");
       
    }

        
    

?>