<?php
  
    include "conexion.php";
    
    //$query = mysqli_query($conectar, $insertar);

    if(!$connection) {
            echo "No se ha podido conectar con el servidor" . mysqli_error();
    }else{
        

        $query="SELECT * FROM usuario WHERE nombre_usuario='$nombre' AND respuesta_seg='$respuesta'";  
        $consulta = mysqli_query($connection, $query);
        $cantidad = mysqli_num_rows($consulta);

        if($cantidad>0){
            $instruccion_SQL = "UPDATE usuario SET contrasena='$contrasena' WHERE nombre_usuario='$nombre'";
            $resultado = mysqli_query($connection,$instruccion_SQL);
            if($resultado){
                
                echo "<script> alert('contraseña recuperada');window.location= 'index.php' </script>";
            }else{
                echo "<script> alert('Hubo un error al actualizar los datos');window.location= 'recuperar.html' </script>";
            }
            
        }else{
            echo "<script> alert('Datos incorrectos o inexistentes');window.location= 'recuperar.html' </script>";
           
        }
        
    }
?>