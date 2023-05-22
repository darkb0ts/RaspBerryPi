<?php

$id=$_GET['id'];
$Top=$_GET['Top'];

$contorl=0;

//------------------------------------MASTER-------------------------------------------//

if ( $Showline=="magdynpwd2015")
{
	$contorl=$contorl+1;
}

else {echo "Master password incorrect. \r\n";}

//-----------------------------------LINE-ID-----------------------------------------//

if ( filter_var($id, FILTER_VALIDATE_INT) === false )
{
	echo "Line ID must be an integer\r\n";
}

else
{
	if ($id>=1&&$id<=128)
	{
	    $contorl=$contorl+1;
	    $reg=100+(($id*40)-39);
	}
	else {echo "Line ID must be between 1 and 128\r\n";}
}

//-------------------------------------TOP-------------------------------------------//

if ( $Top=="YE"||$Top=="NO")
{
	$contorl=$contorl+1;
}

else {echo "Top can only be YE or NO\r\n";}

//-----------------------------------------------------------------------------------//

if($contorl==3)
{
	exec('python Top.py '.$id." ".$Top, $retval);
	echo'python Top.py '.$id." ".$Top."\r\n";	
	exec('python dbinit.py '.$reg, $retval);
	echo'python dbinit.py '.$reg."\r\n";
}

else {die("Fix above errors");}

?>  
