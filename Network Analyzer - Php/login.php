<?php
  
    include "conexion.php";

    session_start();

    $nombre  = $_POST['usuario'];
    $contrasena  = $_POST['contrasena'];  
    
    //$query = mysqli_query($conectar, $insertar);

        
    $query="SELECT * FROM usuario WHERE nombre_usuario='$nombre' AND contrasena='$contrasena'";  
    $consulta = mysqli_query($connection, $query);
    $cantidad = mysqli_num_rows($consulta);

    if($cantidad>0){
        
        $rol =1;
        $query2="SELECT * FROM usuario WHERE nombre_usuario='$nombre' AND rol_id_rol='$rol'";  
        $consulta2 = mysqli_query($connection, $query2);
        $cantidad2 = mysqli_num_rows($consulta2);

        //si es admin
        if($cantidad2>0){
            $_SESSION['nombre']=$nombre;
            header("location: dashboard_admin.php");

        }else{

            $rol=2;
            $query3="SELECT * FROM usuario WHERE nombre_usuario='$nombre' AND rol_id_rol='$rol'";  
            $consulta3 = mysqli_query($connection, $query3);
            $cantidad3 = mysqli_num_rows($consulta3);

            //si es cliente
            if($cantidad3>0){
                $_SESSION['nombre']=$nombre;
                header("location: dashboard.php");
            }
            //si esta en pendiente
            else{
                $_SESSION['nombre']=$nombre;
                header("location: pendiente.php");
            }
        }
    }else{
        echo "<script> alert('Error');window.location= 'index.php' </script>";
    
    }
        
    
?>