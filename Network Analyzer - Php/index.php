   
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <meta name="Author" content="width=device-width, initial-scale=1">
        <title>Login</title>
        <!-- <link rel="stylesheet" type="text/css" href="css/estilos.css"> -->
        <link rel="stylesheet" href="assets/css/estilos.css">
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600&display=swap" rel="stylesheet">
        <script src="https://kit.fontawesome.com/a81368914c.js"></script>
    </head>
    <body>
        <!-- CUADRO DONDE SE INGRESA EL USUARIO Y CONTRASEÑA-->
        <div class="container">
            <div class="login_cuadro">
                <form method="POST" action="login.php" class="login-form">
                    <!-- <img class="logo" src="img/logo.png"> -->
                    <img class="logo" src="assets/img/logo.png">
                    <h2>Bienvenido</h2>

                    <!-- INGRESAR USUARIO-->
                    <div class="input-div one">
                        <div class="i">
                            <i class="fas fa-user"></i>
                        </div>
                        <div>
                            <h5>Usuario</h5>
                            <input id="usuario" name="usuario" class="input" type="text">
                        </div>
                    </div>

                    <!-- INGRESAR CONTRASEÑA-->
                    <div class="input-div two">
                        <div class="i">
                            <i class="fas fa-lock"></i>
                        </div>
                        <div>
                            <h5>Contraseña</h5>
                            <input id="contraseña" name="contrasena" class="input" type="password">
                        </div>
                    </div>

                    <!-- ACCION DE CAMBIAR CONTRASEÑA-->
                    <a class="olvido_contrasena" style="text-decoration:none" href="recuperar.html">¿Olvidó su Contraseña?</a>
                    <input type="submit" class="btn_iniciarSesion" value="Iniciar Sesión">

                    <!-- ACCION DE REGISTRARSE-->
                    <a class="registrarse" style="text-decoration:none" href="registro.html" >Registrarse</a>
                </form>
            </div>
        </div>
        
        <!--<script type="text/javascript" src="js/main.js"></script> -->
        <script type="text/javascript" src="assets/js/main.js"></script>
        <script type="text/javascript" src="assets/js/script.js"></script>
    </body>





</html>