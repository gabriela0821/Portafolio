<?php 

	include "conexion.php";	
    session_start();
    $nombre = $_SESSION['nombre'];

    if(isset($_SESSION['nombre'])){

 ?>

<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <meta name="Author" content="width=device-width, initial-scale=1">
        <title>Login</title>
        <!-- <link rel="stylesheet" type="text/css" href="css/estilos.css"> -->
        <link rel="stylesheet" href="assets/css/estilos_pendiente.css">
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600&display=swap" rel="stylesheet">
        <script src="https://kit.fontawesome.com/a81368914c.js"></script>
    </head>
    <body>
        
        <div class="container">
            <div class="login_cuadro">
                <form class="login-form">
                    <!-- <img class="logo" src="img/logo.png"> -->
                    <img class="logo" src="assets/img/logo.png">
                    <h2>Pendiente</h2>

                    <p class="text">

                        Su perfil aun no ha sido aprobado</p><p  class="text">
                        intente ingresar mas tarde.
                    </p> 
        
                    

                    <a href="salir.php"><input type="button" class="btn_volver" value="Volver"></a>
                    

                    
                </form>
            </div>
        </div>
        
        <!--<script type="text/javascript" src="js/main.js"></script> -->
        <script type="text/javascript" src="assets/js/main.js"></script>
    </body>

</html>

<?php
    }else{

        header('Location: index.php');

    }

?>