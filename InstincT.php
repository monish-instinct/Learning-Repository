<?php
$con= mysqli_connect('localhost', 'root', '', 'skybase') or die('connection failed' .mysqli_connect_error());
if($_POST['instgame']=='melboru')
{
    $doe=date('Y-m-d');
    date_default_timezone_set('Asia/Kolkata');
    $toe=date( 'H:i:s', time () );
    $ip= getHostByName(getHostName());
    $field=explode("[s~1]",$_POST['fielddata']);
    $values=explode("[s~1]",$_POST['fieldvalues']);
    $phno=$_POST['id'];
    $cpno=$_POST['cid'];
    $phno = str_replace("'",'a',$phno);
    $phno = str_replace('"','h',$phno);
    $cpno = str_replace("'",'a',$cpno);
    $cpno = str_replace('"','h',$cpno);

    for ($x = 0; $x < count($field); $x++){
        $field[$x] = str_replace("'",'>>*7&',$field[$x]);
        $field[$x] = str_replace('"','>>*7&<<',$field[$x]);
        $values[$x] = str_replace("'",'>><<*7&',$values[$x]);
        $values[$x]= str_replace('"','<<>>*7&',$values[$x]);
        $sql= "INSERT INTO `instinct_user_registered_details` (`phonenumber`,`cphno`, `fieldname`, `details`,`doe`,`toe`,`ip`) VALUES ('$phno','$cpno','$field[$x]','$values[$x]', '$doe', '$toe', '$ip')";
        $query = mysqli_query($con,$sql);
    }
}
else
    echo("Trying to Hack ?");
?>
