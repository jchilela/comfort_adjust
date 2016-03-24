<?php

$text1 = $_POST['ftemp'];
$text2 = $_POST['fquarto'];
$text3 = $_POST['fpassw'];





// This is the data you want to pass to Python
$data = array($text1, $text2, $text3);

// Execute the python script with the JSON data
$result = shell_exec('python MyScript.py ' . escapeshellarg(json_encode($data)));

// Decode the result
$resultData = json_decode($result, true);

// This will contain: array('status' => 'Yes!')
var_dump($resultData);


?>
