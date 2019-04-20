<?php
	if(!isset($_POST['question']) || trim($_POST['question']," ")==''){
		$temp = [];
		array_push($temp,"pertanyaan belum diisi");
		echo json_encode($temp);
	}
	elseif (!isset($_POST['method'])){
		echo json_encode('Tidak ada method terpilih');
	}
	elseif ($_POST['method'] == 'regex'){
		$question = $_POST['question'];
		$temp = exec('python Regex.py "'.trim($_POST['question']," "));
		echo $temp;
	}
	elseif ($_POST['method'] == 'kmp'){
		$question = $_POST['question'];
		$temp = exec('python KMP.py "'.trim($_POST['question']," "));
		echo $temp;
	}
	elseif ($_POST['method'] == 'bm'){
		$question = $_POST['question'];
		$temp = exec('python Boyer-Moore.py "'.trim($_POST['question']," "));
		echo $temp;
	}
	else {
		echo json_encode('wrong method selection');
	}
	
	
?>