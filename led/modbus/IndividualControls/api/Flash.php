<?php

$id=$_GET['id']; //
$reg=100+(($id*40)-39);
$flash=$_GET['flash'];

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

//------------------------------------FLASH------------------------------------------//

if ( $flash=="YE"||$flash=="NO")
{
	$contorl=$contorl+1;
}

else {echo "flash can only be YE or NO\r\n";}

//-----------------------------------------------------------------------------------//

if($contorl==3)
{
	exec('python Flash.py '.$id." ".$flash, $retval);
	echo'python Flash.py '.$id." ".$flash."\r\n";	
	exec('python dbinit.py '.$reg, $retval);
	echo'python dbinit.py '.$reg."\r\n";
}

else {die("Fix above errors");}

?>