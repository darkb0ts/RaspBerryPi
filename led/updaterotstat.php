<?php
require_once 'inc/connection.inc.php';
$query = "SELECT * FROM `additional_params` WHERE 1" ;
	$query_run = mysqli_query($connection, $query);
	$addlparam=mysqli_fetch_all($query_run,MYSQLI_ASSOC);

$query = "SELECT * FROM `events` WHERE `show_text`=1 AND `Top`=0" ;
	//echo $query; 
	//mysqli_query($connection,"UPDATE `additional_params` SET `blink_speed`='".$_GET['bink_speed']."' WHERE 1"
	$query_run = mysqli_query($connection, $query);
	
	$jsonarr=mysqli_fetch_all($query_run,MYSQLI_ASSOC);
	
	$cnt=count($jsonarr);


if ($cnt>2)
{
	$query = "SELECT * FROM `events` WHERE `show_text`=1 AND `Top`=0 AND `id`>".$addlparam[0]['rotstat'] ;
		//echo $query; 
		//mysqli_query($connection,"UPDATE `additional_params` SET `blink_speed`='".$_GET['bink_speed']."' WHERE 1"
		$query_run = mysqli_query($connection, $query);


		$jsonarr=mysqli_fetch_all($query_run,MYSQLI_ASSOC);
		//echo count($jsonarr);
		if(count($jsonarr)<3)
		{
			for($idx=0;$idx<(3-count($jsonarr));$idx++)
			{
				$data=array();
				$data['id']=99;
				$data['Text']='';
				$data['scroll']="0";
				$data['audio_text']='';
				array_push($jsonarr,$data);
			}
		}
		echo urldecode(json_encode($jsonarr,JSON_UNESCAPED_UNICODE|JSON_UNESCAPED_SLASHES));
}
else
{
	$query = "SELECT * FROM `events` WHERE `show_text`=1 AND `Top`=0";
		//echo $query; 
		//mysqli_query($connection,"UPDATE `additional_params` SET `blink_speed`='".$_GET['bink_speed']."' WHERE 1"
		$query_run = mysqli_query($connection, $query);


		$jsonarr=mysqli_fetch_all($query_run,MYSQLI_ASSOC);
		if(count($jsonarr)<3)
		{
			for($idx=0;$idx<(3-count($jsonarr));$idx++)
			{
				$data=array();
				$data['id']=99;
				$data['Text']='';
				$data['scroll']="0";
				$data['audio_text']='';
				array_push($jsonarr,$data);
			}
		}
		//echo $jsonarr[0]['Text'];
		echo urldecode(json_encode($jsonarr,JSON_UNESCAPED_UNICODE|JSON_UNESCAPED_SLASHES));
}
	?>

