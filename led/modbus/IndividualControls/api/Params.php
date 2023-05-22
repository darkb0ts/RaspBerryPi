<?php

$reg=1;
$param=$_GET['param']; 
$val=$_GET['val'];

$contorl=0;

//------------------------------------MASTER-------------------------------------------//

if ( $Showline=="magdynpwd2015")
{
	$contorl=$contorl+1;
}

else {echo "Master password incorrect. \r\n";}

//-----------------------------------LINE-ID-----------------------------------------//

if ($param=="SR"||$param=="FL"||$param=="BR")
{
	if ( filter_var($val, FILTER_VALIDATE_INT) === false )
	{
		echo "Value must be an integer\r\n";
	}

	else
	{
		if ($val>=1&&$val<=10)
		{
			if (strlen($val)<2){$val=str_pad($val, 2, "0", STR_PAD_LEFT);}
			$contorl=$contorl+1;
		}
		else {echo "Value must be between 1 and 10\r\n";}
	}
	
	$contorl=$contorl+1;
}

else if ($param=="ST"||$param=="CL"){$contorl=$contorl+1;}

else {echo "Invalid parameter\r\n";}

//-----------------------------------------------------------------------------------//

if($contorl==3)
{
	exec('python Params.py '.$param." ".$val, $retval);
	echo'python Params.py '.$param." ".$val."\r\n";	
	exec('python dbinit.py '.$reg, $retval);
	echo'python dbinit.py '.$reg."\r\n";
}

else if($contorl==2)
{
	exec('python Params.py '.$param." ".$param, $retval);
	echo'python Params.py '.$param." ".$param."\r\n";	
	exec('python dbinit.py '.$reg, $retval);
	echo'python dbinit.py '.$reg."\r\n";
}

else {die("Fix above errors");}

?>