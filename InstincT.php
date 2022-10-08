<?php
    $conn= mysqli_connect('localhost', 'root', '', 'instinct') or die('connection failed' .mysqli_connect_error());
if($_POST['instinct']=='applynowdiv1'){
        echo applynowdiv1();
    }
function applynowdiv1(){
    $conn= mysqli_connect('localhost', 'root', '', 'instinct') or die('connection failed' .mysqli_connect_error());
    $characters = '0123456789abcdefghijklmnopqrstuvwxyz';
    $charactersLength = strlen($characters);
    $phno = '';
    for ($i = 0; $i < 6; $i++)
        $phno .= $characters[rand(0, $charactersLength - 1)];
    $fields=['name','surname','dob','gender'];
    $details1=[];
        array_push($details1,$_POST['fn']);
        array_push($details1,$_POST['ln']);
        array_push($details1,$_POST['dob']);
        array_push($details1,$_POST['gender']);
    for ($x = 0; $x <4; $x++) {
        $sql= "INSERT INTO `application` (`phonenumber`, `fieldname`, `details`) VALUES ('$phno', '$fields[$x]', '$details1[$x]')";
        $query = mysqli_query($conn,$sql);}
    return $phno;}
if($_POST['instinct']=='applynowdiv2'){
    echo applynowdiv2();
}
function applynowdiv2(){
    $conn= mysqli_connect('localhost', 'root', '', 'instinct') or die('connection failed' .mysqli_connect_error());
    $phno=$_POST['phno'];
    $field1=['father','mother','spouse','siblings','child'];
        $details2=[];
        array_push($details2,$_POST['father']);
        array_push($details2,$_POST['mother']);
        array_push($details2,$_POST['spouse']);
        array_push($details2,$_POST['siblings']);
        array_push($details2,$_POST['child']);
        for ($x = 0; $x <5; $x++) {
            $sql= "INSERT INTO `application` (`phonenumber`, `fieldname`, `details`) VALUES ('$phno', '$field1[$x]', '$details2[$x]')";
            $query = mysqli_query($conn,$sql);
            }
}
?>
