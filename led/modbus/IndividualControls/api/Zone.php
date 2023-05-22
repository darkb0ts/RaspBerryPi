<?php

$master=$_GET['master'];
$id=$_GET['id'];
$Showline=$_GET['Showline'];

$contorl=0;

//------------------------------------MASTER-------------------------------------------//

if ( $master=="magdynpwd2015")
{
	$contorl=$contorl+1;
}

else {echo "Master password incorrect. <br/>";}

//-----------------------------------LINE-ID-----------------------------------------//

if ( filter_var($id, FILTER_VALIDATE_INT) === false )
{
	echo "Line ID must be an integer<br/>";
}

else
{
	if ($id>=1&&$id<=128)
	{
	    $contorl=$contorl+1;
	    $reg=100+(($id*40)-39);
	}
	else {echo "Line ID must be between 1 and 128<br/>";}
}

//------------------------------------ZONE-------------------------------------------//

if ( $Showline=="YE"||$Showline=="NO")
{
	$contorl=$contorl+1;
}

else {echo "Showline can only be YE or NO<br/>";}

//-----------------------------------------------------------------------------------//

if($contorl==3)
{
	exec('python Zone.py '.$id." ".$Showline, $retval);
	echo'python Zone.py '.$id." ".$Showline."<br/>";	
	exec('python dbinit.py '.$reg, $retval);
	echo'python dbinit.py '.$reg."<br/>";
}

else {die("Fix above errors");}

?>