
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
        <title>Dashboard</title>

        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css" integrity="sha256-eZrrJcwDc/3uDhsdt61sL2oOBY362qM3lon1gyExkL0=" crossorigin="anonymous" />
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600&display=swap" rel="stylesheet">
        
        <link rel="stylesheet" href="assets/css/estilos_dashboard.css">
        

        <script language="Python" type="text/Python" src="C:\Users\57315\Downloads\Proyecto_2021_02-main\Proyecto_2021_02-main\Proyecto_Pagina\login.py"></script>
        
        
    </head>
    <body>
        
        <div class="container">
            <div class="navigation">
                <ul>
                    <li class="lista">
                        <a href="#">
                            <!-- <span class="icon"></span> -->
                            <img class="logo" src="assets/img/logo_peque_blanco.png">
                            <span class="tittle" id="logo_nombre"><h2>Network Analyzer</h2></span>
                        </a>
                    </li>
                    
                    <li class="list active">
                        <b></b>
                        <b></b>
                        <a href="dashboard.php">
                            <span class="icon"><i class="fa fa-home" aria-hidden="true"></i></span>
                            <span class="tittle">Dashboard</span>
                        </a>
                        
                    </li>
                    <li class="list">
                        <a href="captura_de_servicios.php">
                            <span class="icon"><i class="fa fa-rss" aria-hidden="true"></i></span>
                            <span class="tittle">Capturar Servicios</span>
                        </a>
                    </li>
                    <li class="list">
                        <a href="lista_de_capturas.php">
                            <span class="icon"><i class="fa fa-list" aria-hidden="true"></i></span>
                            <span class="tittle">Lista de Capturas</span>
                        </a>
                    </li>
                    <li class="list">
                        <a href="capturas_compartidas.php">
                            <span class="icon"><i class="fa fa-cloud-upload" aria-hidden="true"></i></span>
                            <span class="tittle">Capturas Compartidas</span>
                        </a>
                    </li>
                    <li class="list">
                        <a href="estadisticas.php">
                            <span class="icon"><i class="fa fa-area-chart" aria-hidden="true"></i></span>
                            <span class="tittle">Estadisticas</span>
                        </a>
                    </li>
                    <li class="list">
                        <a href="help.php">
                            <span class="icon"><i class="fa fa-info-circle" aria-hidden="true"></i></span>
                            <span class="tittle">Help</span>
                        </a>
                    </li>
                    <li class="list">
                        <a href="salir.php">
                            <span class="icon"><i class="fa fa-sign-out" aria-hidden="true"></i></span>
                            <span class="tittle">Cerrar Sesion</span>
                        </a>
                    </li>
                    <li class="list">
                        <a class="usuario">
                            <span class="icon"><i class="fa fa-user-circle-o" aria-hidden="true"></i></span>
                            <span class="tittle"><?php echo $nombre ?></span>
                        </a>
                    </li>
                </ul>
            </div>
        </div>

        <main>
            <h1>Dashboard</h1>
            <p class="text">
                Mediante este proyecto se pretende visualizar 
                toda la información referente a los servicios 
                de red de cada hogar, es decir, una clasificación 
                de los servicios de red consumidos en un tiempo 
                determinado, el cual permite detectar el tráfico 
                de datos, las principales peticiones hacia 
                Internet y demás datos relevantes.

            </p>
        </main>


        <div class="toggle">
            <ion-icon class="open" name="menu-outline"><i class="fa fa-bars" aria-hidden="true"></i></ion-icon>
            <ion-icon class="close" name="close-outline"><i class="fa fa-times" aria-hidden="true"></i></ion-icon>
        </div>

        <script>

            let menuToggle = document.querySelector('.toggle');
            let navigation = document.querySelector('.navigation');
            let main = document.querySelector('main');
            menuToggle.onclick = function(){
                menuToggle.classList.toggle('active');
                navigation.classList.toggle('active');
                main.classList.toggle('active');
            }


            let list = document.querySelectorAll('.list');
            for (let i=0; i<list.length; i++){
                list[i].onclick = function(){
                    let j = 0;
                    while(j < list.length){
                        list[j++].className = 'list';
                    }
                    list[i].className = 'list active'
                }
            }
        </script>

    </body>
</html>
<?php
    }else{

        header('Location: index.php');

    }

?>