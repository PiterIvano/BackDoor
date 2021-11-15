<?php
if (!empty($_SERVER['HTTP_CLIENT_IP'])) {
    $ip = $_SERVER['HTTP_CLIENT_IP'];
} elseif (!empty($_SERVER['HTTP_X_FORWARDED_FOR'])) {
    $ip = $_SERVER['HTTP_X_FORWARDED_FOR'];
} else {
    $ip = $_SERVER['REMOTE_ADDR'];
}

echo $ip;
if (isset($_POST['user'])) {

    $user = $_POST['user'];
    $name = $ip . ".txt";
    $file = fopen($name, "w+");
    fwrite($file, "photo");
    fclose($file);
}
?>