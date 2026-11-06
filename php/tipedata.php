<?php
$nim = 'A';
$nama = "Muhammad Encep";
$umur = 36;
$nilai = 82.25;
$status = TRUE;
echo "---Belajar Tipe Data --- <br><br>";
echo "Tipe Data Char : " . $nim . "<br>";
echo "Tipe Data String : $nama<br>";
print "Tipe Data Int : " . $umur;
print "<br>";
printf("Tipe Data Float : %.5f<br><br>", $nilai);
echo "Tipe Data Boolean : <br><br>";
if ($status)
   echo "Status : Aktif";
else
   echo "Status : Tidak Aktif";
?>