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
        <title>Capturar Servicios</title>

        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css" integrity="sha256-eZrrJcwDc/3uDhsdt61sL2oOBY362qM3lon1gyExkL0=" crossorigin="anonymous" />
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600&display=swap" rel="stylesheet">
        <script src="https://unpkg.com/sweetalert/dist/sweetalert.min.js"></script>
        <script src="//cdn.jsdelivr.net/npm/sweetalert2@11"></script>
        <link rel="stylesheet" href="assets/css/estilos_dashboard.css">
        <link rel="stylesheet" href="assets/css/estilos_lista_servicios.css">

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
                    <li class="list active">
                        <b></b>
                        <b></b>
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
            <h1>Capturar Servicios</h1>
            <p class="text">
                Se capturan los servicios de la red.

            </p>
            <br><br>
           
            <body>
                <form method="post">
                <input type="submit" name="capturar" value="Capturar Servicios">
                

                <br><br>
                <h2>Servicios Capturados</h2>
                <br><br>
                <table>
                    <tr>
                        <th>ID</th>
                        <th>Servicio</th>
                        <th>Ip Cliente</th>
                        <th>Ip fisica</th>
                        <th>Ip Servidor</th>
                        <th>Nombre Pagina</th>
                        <th>Puerto origen</th>
                        <th>Puerto final</th>
                        
                    </tr>
                    <?php

                        

                        include "conexion.php";

                        $sql1 = mysqli_query($connection,"SELECT COUNT(*) as total_registro 
                                               FROM dhcp d, usuario u
                                               WHERE nombre_usuario='camilo'");

                        $result_register1 = mysqli_fetch_array($sql1);
                        $total_registro1 = $result_register1['total_registro'];


                        $sql2 = mysqli_query($connection,"SELECT COUNT(*) as total_registro 
                                               FROM dns d, usuario u
                                               WHERE nombre_usuario='camilo'");

                        $result_register2 = mysqli_fetch_array($sql2);
                        $total_registro2 = $result_register2['total_registro'];


                        $sql3 = mysqli_query($connection,"SELECT COUNT(*) as total_registro 
                                               FROM http d, usuario u
                                               WHERE nombre_usuario='camilo'");

                        $result_register3 = mysqli_fetch_array($sql3);
                        $total_registro3 = $result_register3['total_registro'];


                       
                        $por_pagina = 10;

                        if(empty($_GET['pagina']))
                        {
                            $pagina = 1;
                        }else{
                            $pagina = $_GET['pagina'];
                        }
    
                        $desde = ($pagina-1) * $por_pagina;
                        $total_paginas = ceil(($total_registro1+$total_registro2+$total_registro3) / $por_pagina);
                        
                        $DHCP="SELECT id_dhcp, nombre_servicio, ip_cliente, ip_pc_fisic, ip_server,puerto,puerto_src
                        FROM captura c, usuario usu, dhcp d
                        WHERE nombre_usuario='$nombre'
                        AND c.usuario_idusuario = usu.idusuario
                        AND c.idcaptura = d.captura_idcaptura LIMIT $desde,$por_pagina";

                        $result1=mysqli_query($connection,$DHCP);
                        
                        while($mostrar1=mysqli_fetch_array($result1)){
                    ?>
                    <tr>
                        <td><?php echo $mostrar1['id_dhcp']; ?></td>
                        <td><?php echo $mostrar1['nombre_servicio']; ?></td>
                        <td><?php echo $mostrar1['ip_cliente']; ?></td>
                        <td><?php echo $mostrar1['ip_pc_fisic']; ?></td>
                        <td><?php echo $mostrar1['ip_server']; ?></td>
                        <td>-</td>
                        <td><?php echo $mostrar1['puerto_src']; ?></td>
                        <td><?php echo $mostrar1['puerto']; ?></td>
                        

                        
                    </tr>
                    <?php
                    
                        }
                    ?>


                    <?php
                        include "conexion.php";
                        
                        $SMTP="SELECT idsmtp, nombre_servicio, puertoinicio, puertofinal
                        FROM captura c, usuario usu, smtp d
                        WHERE nombre_usuario='$nombre'
                        AND c.usuario_idusuario = usu.idusuario
                        AND c.idcaptura = d.captura_idcaptura
                        LIMIT $desde,$por_pagina";

                        $result2=mysqli_query($connection,$SMTP);
                        
                        while($mostrar2=mysqli_fetch_array($result2)){
                    ?>
                    <tr>
                        <td><?php echo $mostrar2['idsmtp']; ?></td>
                        <td><?php echo $mostrar2['nombre_servicio']; ?></td>
                        <td>-</td>
                        <td>-</td>
                        <td>-</td>
                        <td>-</td>
                        <td><?php echo $mostrar2['puertoinicio']; ?></td>
                        <td><?php echo $mostrar2['puertofinal']; ?></td>
                    </tr>
                    <?php
                    
                        }
                    ?>


                    <?php
                        include "conexion.php";
                        
                        $DNS="SELECT id_dns, nombre_servicio, ip_dns, query_name, puerto
                        FROM captura c, usuario usu, dns d
                        WHERE nombre_usuario='$nombre'
                        AND c.usuario_idusuario = usu.idusuario
                        AND c.idcaptura = d.captura_idcaptura
                        LIMIT $desde,$por_pagina";

                        $result2=mysqli_query($connection,$DNS);
                        
                        while($mostrar2=mysqli_fetch_array($result2)){
                    ?>
                    <tr>
                        <td><?php echo $mostrar2['id_dns']; ?></td>
                        <td><?php echo $mostrar2['nombre_servicio']; ?></td>
                        <td><?php echo $mostrar2['ip_dns']; ?></td>
                        <td>-</td>
                        <td>-</td>
                        <td><?php echo $mostrar2['query_name']; ?></td>
                        <td>-</td>
                        <td><?php echo $mostrar2['puerto']; ?></td>
                    </tr>
                    <?php
                    
                        }
                    ?>

                    <?php

                        include "conexion.php";
                        
                        $HTTP="SELECT idhttp, nombre_servicio, puerto
                        FROM captura c, usuario usu, http d
                        WHERE nombre_usuario='$nombre'
                        AND c.usuario_idusuario = usu.idusuario
                        AND c.idcaptura = d.captura_idcaptura LIMIT $desde,$por_pagina";

                        $result3=mysqli_query($connection,$HTTP);
                        while($mostrar3=mysqli_fetch_array($result3)){
                        
                    ?>
                    <tr>
                        <td><?php echo $mostrar3['idhttp']; ?></td>
                        <td><?php echo $mostrar3['nombre_servicio']; ?></td>
                        <td>-</td>
                        <td>-</td>
                        <td>-</td>
                        <td>-</td>
                        <td>-</td>
                        <td><?php echo $mostrar3['puerto']; ?></td>
                    </tr>
                    <?php
                    
                        }
                    ?>   
                    
                   

                    <?php
                        include "conexion.php";
                        
                        $FTP="SELECT idftp, nombre_servicio, puerto
                        FROM captura c, usuario usu, ftp d
                        WHERE nombre_usuario='$nombre'
                        AND c.usuario_idusuario = usu.idusuario
                        AND c.idcaptura = d.captura_idcaptura
                        LIMIT $desde,$por_pagina";

                        $result2=mysqli_query($connection,$FTP);
                        
                        while($mostrar2=mysqli_fetch_array($result2)){
                    ?>
                    <tr>
                        <td><?php echo $mostrar2['idftp']; ?></td>
                        <td><?php echo $mostrar2['nombre_servicio']; ?></td>
                        <td>-</td>
                        <td>-</td>
                        <td>-</td>
                        <td>-</td>
                        <td>-</td>
                        <td><?php echo $mostrar2['puerto']; ?></td>
                    </tr>
                    <?php
                    
                        }
                    ?>

                </table>

                <div class="paginador">
					<ul>
					<?php 
                        $primera = $pagina - ($pagina % 5) + 1;
                        if ($primera > $pagina) { $primera = $primera - 5; }
                        $ultima = $primera + 4 > $total_paginas ? $total_paginas : $primera + 4; 
                        
                        if ($total_paginas > 1) {
                            // comprobamos $primera en lugar de $pagina
                            if ($primera != 1){
                                ?>
                                <li><a href="?pagina=<?php echo 1; ?>">|<</a></li>
						        <li><a href="?pagina=<?php echo $pagina-1; ?>"><<</a></li>
                                <?php
                            }
                                //echo '<li><a href="?pagina='.($primera-1).'" aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>';
                
                            // mostramos de la primera a la última
                            for ($i = $primera; $i <=$ultima; $i++){
                                if ($pagina == $i){
                                    echo '<li class="pageSelected">'.$i.'</li>';
                                }else{
                                    echo '<li><a href="?pagina='.$i.'">'.$i.'</a></li>';
                                }
                            }
                
                            if ($i <= $total_paginas){
                                //echo '<li><a href="?pagina='.($i).'"></a></li>';
                                ?>
                                
                                
                                <li><a href="?pagina=<?php echo $pagina + 1; ?>">>></a></li>
                                <li><a href="?pagina=<?php echo $total_paginas; ?> ">>|</a></li>
                                <?php
                            }
                        }

					?>
                    
					</ul>
				</div>



                <!--<input type="submit" name="BDHCP" value="DHCP" href=>
                <input type="submit" name="BDNS" value="DNS">
                <input type="submit" name="BHTPP" value="HTTP">-->
                </form>
                <?php
                $capturar="";
                
                if (isset($_POST["capturar"]))$capturar=$_POST["capturar"];

                if($capturar){
                    
                    
                    $tmp = exec("python holis.py $nombre");
                        ?> 
                    <script>
                        Swal.fire({
                            icon: 'success',
                            title: 'Enhorabuena!',
                            confirmButtonText: 'Okay',
                            text: 'Protocolos Capturados Correctamente',
                            footer: '',
                            showCloseButton: true
                        })
                        .then(function (result) {
                            if (result.value) {
                                window.location = "captura_de_servicios.php";
                            }
                        })     

                    </script>
                    
                    
                    <?php
                    
                }
                ?>  
                    
            </body>
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