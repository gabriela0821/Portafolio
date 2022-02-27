
<?php 
	
	include_once 'conexion.php';

    

    $sql = "DELETE FROM usuario WHERE idusuario ='" . $_GET['id2'] . "'";
    if(mysqli_query($connection, $sql)){
        $sql2 = "ALTER TABLE usuario AUTO_INCREMENT=1";
        mysqli_query($connection, $sql2);

        header("Location: lista_usuarios.php");
        
        
    }else{
        
        echo "error al eliminar registro: ". mysqli_error($connection);
    }
    mysqli_close($connection);

?>


