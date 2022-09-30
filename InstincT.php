<?php
        $conn= mysqli_connect('localhost', 'root', '', 'instinct') or die('connection failed' .mysqli_connect_error());
    $characters = '0123456789abcdefghijklmnopqrstuvwxyz';
    $charactersLength = strlen($characters);
    $phno = '';
    for ($i = 0; $i < 6; $i++)
        $phno .= $characters[rand(0, $charactersLength - 1)];
        $fields=['name','surname','dob','gender'];
        $details1=[];
        echo $phno;
            array_push($details1,$_POST['fn']);
            array_push($details1,$_POST['ln']);
            array_push($details1,$_POST['dob']);
            array_push($details1,$_POST['gender']);
for ($x = 0; $x <4; $x++) {
    $sql= "INSERT INTO `application` (`phonenumber`, `fieldname`, `details`) VALUES ('$phno', '$fields[$x]', '$details1[$x]')";
    $query = mysqli_query($conn,$sql);
 }
?>
