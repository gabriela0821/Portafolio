<?php 
	
    include_once 'conexion.php';
    

    if(isset($_GET["id1"])){

        $sql = "UPDATE usuario SET rol_id_rol = 2 WHERE idusuario ='" . $_GET['id1'] . "'";
        if(mysqli_query($connection, $sql)){

            header("Location: lista_usuarios.php");
            
            
        }else{
            echo "error al aceptar registro: ". mysqli_error($connection);
        }
        mysqli_close($connection);
    }
	
?>


