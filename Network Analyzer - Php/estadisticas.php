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
                    
                    <li class="list">
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
                    <li class="list active">
                        <b></b>
                        <b></b>
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
            
            <h1>Estadisticas</h1>
            <p class="text">
                A continuacion, se muestran las estadisticas de los servicios.

            </p>
            <br><br>
            <?php

                include "conexion.php";
                
                //DHCP
                $DHCP = "SELECT count(*) total
                FROM dhcp d, captura c, usuario usu
                WHERE nombre_usuario='$nombre'
                AND c.usuario_idusuario = usu.idusuario
                AND c.tipo_serv='DHCP'";

                //DNS
                $DNS = "SELECT count(*) total
                FROM dns d, captura c, usuario usu
                WHERE nombre_usuario='$nombre'
                AND c.usuario_idusuario = usu.idusuario
                AND c.tipo_serv='DNS'";

                //HTTP
                $HTTP = "SELECT count(*) total
                FROM http d, captura c, usuario usu
                WHERE nombre_usuario='$nombre'
                AND c.usuario_idusuario = usu.idusuario
                AND c.tipo_serv='HTTP'";

                //FTP
                $FTP = "SELECT count(*) total
                FROM ftp d, captura c, usuario usu
                WHERE nombre_usuario='$nombre'
                AND c.usuario_idusuario = usu.idusuario
                AND c.tipo_serv='ftp'";

                //POP3
                $POP3 = "SELECT count(*) total
                FROM pop3 d, captura c, usuario usu
                WHERE nombre_usuario='$nombre'
                AND c.usuario_idusuario = usu.idusuario
                AND c.tipo_serv='POP3'";

                //SMTP
                $SMTP = "SELECT count(*) total
                FROM smtp d, captura c, usuario usu
                WHERE nombre_usuario='$nombre'
                AND c.usuario_idusuario = usu.idusuario
                AND c.tipo_serv='smtp'";

                $result1 = mysqli_query($connection,$DHCP);
                $result2 = mysqli_query($connection,$DNS);
                $result3 = mysqli_query($connection,$HTTP);
                $result4 = mysqli_query($connection,$FTP);
                $result5 = mysqli_query($connection,$POP3);
                $result6 = mysqli_query($connection,$SMTP);

                $mostrar1 = mysqli_fetch_array($result1);
                $mostrar2 = mysqli_fetch_array($result2);
                $mostrar3 = mysqli_fetch_array($result3);
                $mostrar4 = mysqli_fetch_array($result4);
                $mostrar5 = mysqli_fetch_array($result5);
                $mostrar6 = mysqli_fetch_array($result6);

                /*
                echo 'Número de total de registros 1: ' . $mostrar1['total'];
                echo 'Número de total de registros 1: ' . $mostrar2['total'];
                echo 'Número de total de registros 1: ' . $mostrar3['total'];*/
                            
            ?>
            
            <canvas id="myChart" style="height: 40vh; width: 80vw"></canvas>
            <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
            <script>
                var ctx = document.getElementById('myChart');
                var myChart = new Chart(ctx, {
                    type: 'bar',
                    data: {
                        labels: ['DHCP', 'DNS', 'HTTP', 'FTP', 'SMTP'],
                        datasets: [{
                            label: 'Cantidad de Capturas por Protocolo',
                            
                            data: [<?php echo $mostrar1['total']; ?>, <?php echo $mostrar2['total']; ?>, 
                                   <?php echo $mostrar3['total']; ?>, <?php echo $mostrar4['total']; ?>, 
                                   <?php echo $mostrar6['total']; ?>],
                            
                            backgroundColor: [
                                'rgba(255, 99, 132, 0.2)',
                                'rgba(54, 162, 235, 0.2)',
                                'rgba(255, 206, 86, 0.2)',
                                'rgba(75, 192, 192, 0.2)',
                                'rgba(153, 102, 255, 0.2)',
                                'rgba(255, 159, 64, 0.2)'
                            ],
                            borderColor: [
                                'rgba(255, 99, 132, 1)',
                                'rgba(54, 162, 235, 1)',
                                'rgba(255, 206, 86, 1)',
                                'rgba(75, 192, 192, 1)',
                                'rgba(153, 102, 255, 1)',
                                'rgba(255, 159, 64, 1)'
                            ],
                            borderWidth: 1
                        }]
                    },
                    options: {
                        scales: {
                            y: {
                                beginAtZero: true
                            }
                        }
                    }
                });

                

            </script>
            <br><br>
            <br><br>

            <?php

                include "conexion.php";

                //DNS
                $DNS2  = "SELECT d.ip_host ip, count(*) cont
                from dns d, captura c, usuario usu
                WHERE nombre_usuario='$nombre'
                AND c.usuario_idusuario = usu.idusuario
                AND c.tipo_serv='DNS'
                GROUP BY ip_host
                order by cont desc limit 1";

                //HTTP
                $HTTP2 = "SELECT d.ip ip, count(*) cont
                from ftp d, captura c, usuario usu
                WHERE nombre_usuario='$nombre'
                AND c.usuario_idusuario = usu.idusuario
                AND c.tipo_serv='FTP'
                GROUP BY ip
                order by cont desc limit 1";

                //FTP
                $FTP2 = "SELECT d.ip ip, count(*) cont
                from http d, captura c, usuario usu
                WHERE nombre_usuario='$nombre'
                AND c.usuario_idusuario = usu.idusuario
                AND c.tipo_serv='HTTP'
                GROUP BY ip
                order by cont desc limit 1,1";

                //SMTP
                $SMTP2 = "SELECT d.ip_host ip, count(*) cont
                from smtp d, captura c, usuario usu
                WHERE nombre_usuario='$nombre'
                AND c.usuario_idusuario = usu.idusuario
                AND c.tipo_serv='SMTP'
                GROUP BY ip_host
                order by cont desc limit 1";

                $result7 = mysqli_query($connection,$DNS2);
                $result8 = mysqli_query($connection,$HTTP2);
                $result9 = mysqli_query($connection,$FTP2);
                $result10 = mysqli_query($connection,$SMTP2);

                $mostrar7 = mysqli_fetch_array($result7);
                $mostrar8 = mysqli_fetch_array($result8);
                $mostrar9 = mysqli_fetch_array($result9);
                $mostrar10 = mysqli_fetch_array($result10);

                /*
                echo 'Número de total de registros 1: ' . $mostrar1['total'];
                echo 'Número de total de registros 1: ' . $mostrar2['total'];
                echo 'Número de total de registros 1: ' . $mostrar3['total'];*/

                ?>

                <canvas id="myChart2" style="height: 40vh; width: 80vw"></canvas>
                <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
                <script>
                    var ctx = document.getElementById('myChart2');
                    
                    var myChart = new Chart(ctx, {
                        type: 'bar',
                        data: {
                            labels: ['DNS', 'HTTP', 'FTP', 'SMTP'],
                            
                            datasets: [{
                                label: 'Ip con mayor envio de Peticiones',
                                labels: ['DNS', 'HTTP', 'FTP', 'SMTP'],

                                data: [<?php echo $mostrar7['cont']; ?>, <?php echo $mostrar8['cont']; ?>, 
                                       <?php echo $mostrar9['cont']; ?>, <?php echo $mostrar10['cont']; ?>],
                                
                                
                                
                                backgroundColor: [
                                    
                                    'rgba(75, 192, 192, 0.2)',
                                    'rgba(255, 99, 132, 0.2)',
                                    
                                    'rgba(153, 102, 255, 0.2)',
                                    'rgba(255, 159, 64, 0.2)'
                                ],
                                borderColor: [
                                    
                                    'rgba(75, 192, 192, 1)',
                                    'rgba(255, 99, 132, 1)',
                                    
                                    'rgba(153, 102, 255, 1)',
                                    'rgba(255, 159, 64, 1)'
                                ],
                                borderWidth: 1
                            }],
                                labels: ["<?php echo $mostrar7['ip']; ?> - DNS"," <?php echo $mostrar8['ip']; ?> - HTTP", 
                                       "<?php echo $mostrar9['ip']; ?> - FTP", "<?php echo $mostrar10['ip']; ?> - SMTP"],
                                
                        },
                        options: {
                            scales: {
                                y: {
                                    beginAtZero: true
                                }
                            }
                        }
                    });



                </script>
            

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