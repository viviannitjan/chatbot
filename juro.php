<?php
	if(!isset($_POST['question'])){
		$aResult = 'tidak ada angka terinput';
		echo json_encode($aResult);
	}
	elseif (!isset($_POST['method'])){
		echo json_encode('Tidak ada method terpilih');
	}
	elseif ($_POST['method'] == 'regex'){
		$question = $_POST['question'];
		$temp = exec('python coba.py "'.$question);
		echo $temp;
	}
	elseif ($_POST['method'] == 'kmp'){
		
	}
	elseif ($_POST['method'] == 'bm'){
		
	}
	else {
		echo json_encode('wrong method selection');
	}
	
	
?>