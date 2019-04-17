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
		$temp = exec('python Regex.py "'.$question);
		echo $temp;
	}
	elseif ($_POST['method'] == 'kmp'){
		$question = $_POST['question'];
		$temp = exec('python KMP.py "'.$question);
		echo $temp;
	}
	elseif ($_POST['method'] == 'bm'){
		$question = $_POST['question'];
		$temp = exec('python Boyer-Moore.py "'.$question);
		echo $temp;
	}
	else {
		echo json_encode('wrong method selection');
	}
	
	
?>