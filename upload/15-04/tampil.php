<html> 
<head>
<title> </title>
 </head>
 <body>
 <form action="pola.php" method="POST">
 Masukkan Angka
<input type="text" name="isi"> <input type="submit" name="submit" value="submit">
 </form>
 </body>
</html>

<?php

if (isset($_POST['submit'])){
	$bin = $_POST['isi'];
	
for ($i=1;$i<=$bin;$i++){
	
    for ($j=$i;$j>=1;$j--){
        echo $j;
    }
    echo "<br>";

}
}
	

?>