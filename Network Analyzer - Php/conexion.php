<?php

    $user = "root";
    $pass = "root";
    $host = "localhost";
    $datab = "proyecto1";


    //conectamos al base datos
    $connection = mysqli_connect($host, $user, $pass, $datab);
    
    if(!$connection){
		  echo "Error en la conexión";
	}



?>