<?php 


    include "conexion.php";
    session_start();
    $nombre = $_SESSION['nombre'];
    
    if(isset($_SESSION['nombre'])){
    
?>


<!DOCTYPE html>
<html lang="en">
<head>
		<meta charset="UTF-8">
        <meta name="Author" content="width=device-width, initial-scale=1">
        <title>Dashboard</title>

        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css" integrity="sha256-eZrrJcwDc/3uDhsdt61sL2oOBY362qM3lon1gyExkL0=" crossorigin="anonymous" />
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="assets/css/estilos_dashboard_admin.css">
        <link rel="stylesheet" href="assets/css/estilo_lista_usuarios.css">
		<h1><a target="_blank" href="http://www.baulphp.com/"></a></h1>
        
        <script src="https://unpkg.com/sweetalert/dist/sweetalert.min.js"></script>
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
                        
                        <a href="dashboard_admin.php">
                            <span class="icon"><i class="fa fa-home" aria-hidden="true"></i></span>
                            <span class="tittle">Dashboard</span>
                        </a>
                        
                    </li>
                    <li class="list active">
                        <b></b>
                        <b></b>
                        <a href="ver_perfiles_admin.php">
                            <span class="icon"><i class="fa fa-rss" aria-hidden="true"></i></span>
                            <span class="tittle">Ver perfiles de usuario</span>
                        </a>
                    </li>
                    <li class="list">
                        <a href="help_admin.php">
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
                    <br><br><br><br><br><br><br>
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

        <div class="texto">
            <h1>Perfiles de Usuario</h1>
            <p class="text">
                Son los perfiles que se encuentran en estado de pendiente.

            </p>
        <br> <br>
        </div>
            

			<section id="container">


				<table>
					<tr>
						<th>ID</th>
						<th>Usuario</th>
						<th>Rol</th>
						<th>Acciones</th>
					</tr>
				<?php 
					//validamos datos del servidor
					include "aceptar_perfil_admin.php";
                    include "conexion.php";

					//Paginador
					$sql_registe = mysqli_query($connection,"SELECT COUNT(*) as total_registro FROM usuario WHERE rol_id_rol = 3 ");
					$result_register = mysqli_fetch_array($sql_registe);
					$total_registro = $result_register['total_registro'];

					$por_pagina = 5;

					if(empty($_GET['pagina']))
					{
						$pagina = 1;
					}else{
						$pagina = $_GET['pagina'];
					}

					$desde = ($pagina-1) * $por_pagina;
					$total_paginas = ceil($total_registro / $por_pagina);

					$query = mysqli_query($connection,"SELECT * FROM usuario
													WHERE rol_id_rol = 3 ORDER BY idusuario ASC LIMIT $desde,$por_pagina 
						");

                    $query2 = mysqli_query($connection,"SELECT * FROM rol r, usuario usu
                    WHERE usu.rol_id_rol = 3
                    AND r.id_rol=usu.rol_id_rol
                    ORDER BY usu.idusuario ASC LIMIT $desde,$por_pagina");

                    

					mysqli_close($connection);

					$result = mysqli_num_rows($query);
                    $result2 = mysqli_num_rows($query2);

                    $data2 = mysqli_fetch_array($query2);
					if($result > 0){
                    
						while ($data = mysqli_fetch_array($query)) {
							
					?>
						<tr>
							<td><?php echo $data["idusuario"]; ?></td>
							<td><?php echo $data["nombre_usuario"]; ?></td>
							
                            <td><?php echo $data2["rol"]; ?></td>
                            <!-- td?php echo $data['rol_id_rol'] ?></td -->
                            
							<td>
								
                                <a class="link_aceptado" style="text-decoration:none" href="aceptar_perfil_admin.php?id1=<?php echo $data["idusuario"]; ?>">Aceptar</a>

							<?php if($data["idusuario"] != 1){ ?>
								|
								<a class="link_delete" style="text-decoration:none" href="eliminar_perfil_admin.php?id2=<?php echo $data["idusuario"]; ?>">Eliminar</a>
							<?php } ?>
								
							</td>
                            
						</tr>
					
				<?php 
						}

					}
				?>

				</table>
				<div class="paginador">
					<ul>
					<?php 
						if($pagina != 1)
						{
					?>
						<li><a href="?pagina=<?php echo 1; ?>">|<</a></li>
						<li><a href="?pagina=<?php echo $pagina-1; ?>"><<</a></li>
					<?php 
						}
						for ($i=1; $i <= $total_paginas; $i++) { 
							# code...
							if($i == $pagina)
							{
								echo '<li class="pageSelected">'.$i.'</li>';
							}else{
								echo '<li><a href="?pagina='.$i.'">'.$i.'</a></li>';
							}
						}

						if($pagina != $total_paginas)
						{
					?>
						<li><a href="?pagina=<?php echo $pagina + 1; ?>">>></a></li>
						<li><a href="?pagina=<?php echo $total_paginas; ?> ">>|</a></li>
					<?php } ?>
					</ul>
				</div>


			</section>
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