# BackDoor

<h2>Public_html</h2>
  
  <p>este archivo sera el que este en la web, no cambiar</p>
  
<h2>hacked_1.1.py</h2>

<p>Este archivo es el backdoor, este archivo da acceso completo a la cmd de la victima.</p>

<h2>Keylogger.py</h2>

<p>Este archivo se ejecuta en segundo plano por si mismo, el se copia en la carpeta, para iniciarse con el sistema. esto nos servira para que nuestro exe no tengamos que ejecutarlo cada vez.</p>

<h2>Login.php</h2>

<p>Este archivo es para poder ejecutar comandos en cada maquina victima, esto nos servira mucho a la hora de querer mandar comandos a cada maquina</p>



<h2>IMPORTANTE</h2>

<p>todo esto se puede convertir a windows con pyinstaller, pero lo tienes que compilar de esta manera
<pre><code>
pyinstaller --clean  --icon=icon.ico  [tufichero].py
</code></pre>

Los demas archivos los puedes compilar de esta manera 
<pre><code>
pyinstaller --clean --onefile --icon=icon.ico --windowed [tufichero].py
</code></pre>

luego subes lo que hay en el archivo zip a tu servidor OJO TIENE QUE ESTAR EN LA PAGINA PRINCIPAL OSEA PUBLIC_HTML luego de esto solo queda modificar el hacked_1.1.py
Este le pones tu url y compilas, al igual que el keylogger

podeis modificar un poco el archivo ejecutar, ya que en ese esta diseñado para un unico tipo de personas
