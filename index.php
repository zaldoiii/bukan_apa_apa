<?php

require_once('./line_class.php');

$channelAccessToken = 'oV1G0/52nBWW/xRdzTCrrGumF2BJy1xR1CIspX8PRdrMSrFYXXYjkAN9t8Mau5yvpOcCiWL44U4fXcqbjw/6Xkrx8ZwxsCZgpfwVrYP4H+V0EfQ99nl0LkmAMAJg6Kt9qonVvXDqw6X2r1XQt4G8nAdB04t89/1O/w1cDnyilFU='; //sesuaikan 
$channelSecret = 'e6f653879f4b7225b5554ecb1c430329';//sesuaikan

$client = new LINEBotTiny($channelAccessToken, $channelSecret);

$userId 	= $client->parseEvents()[0]['source']['userId'];
$replyToken = $client->parseEvents()[0]['replyToken'];
$timestamp	= $client->parseEvents()[0]['timestamp'];

$message 	= $client->parseEvents()[0]['message'];
$messageid 	= $client->parseEvents()[0]['message']['id'];

$profil = $client->profil($userId);

$pesan_datang = $message['text'];

if($message['type'] == 'text')
{
	$cmd_1 = 'python ccd.py ' . $pesan_datang;
	$cmd_2 = shell_exec($cmd_1);
	$balas = array (
		'replyToken' => $replyToken,
		'messages' => array(
			array (
				'type' => 'text',
				'text' => $cmd_2
			)
		)
	);
}

else if($message['type']=='sticker')
{
	$balas = array (
		'replyToken' => $replyToken,
		'messages' => array (
			array (
				'type' => 'text',
				'text' => "Terimakasih stikernya!"
			)
		)
	);
}
 
$result =  json_encode($balas);

file_put_contents('./balasan.json',$result);

$client->replyMessage($balas);

?>
