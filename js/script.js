$(document).ready(function() {
    $("#regex").click(function(){
		$.ajax({
				type : "POST",
				url : "juro.php",
				dataType : 'json',
				data : {question : $("#terima_pertanyaan").val(), method : 'regex'},
				success : function(data){
					$("#tampil_jawaban").html(data);
				},
				error : function(){$("#tampil_jawaban").html("error occured in the engine or server");}
			})
        //alert($("#terima_pertanyaan").val());
		//$("#tampil_jawaban").html($("#terima_pertanyaan").val());
    });
});

$(document).ready(function() {
    $("#kmp").click(function(){
		$.ajax({
				type : "POST",
				url : "juro.php",
				dataType : 'json',
				data : {question : $("#terima_pertanyaan").val(), method : 'kmp'},
				success : function(data){
					$("#tampil_jawaban").html(data);
				},
				error : function(){$("#tampil_jawaban").html("error occured in the engine or server");}
			})
        //alert($("#terima_pertanyaan").val());
        //$("#tampil_jawaban").html($("#terima_pertanyaan").val());
    });
});

$(document).ready(function() {
    $("#bm").click(function(){
		$.ajax({
				type : "POST",
				url : "juro.php",
				dataType : 'json',
				data : {question : $("#terima_pertanyaan").val(), method : 'bm'},
				success : function(data){
					$("#tampil_jawaban").html(data);
				},
				error : function(){$("#tampil_jawaban").html("error occured in the engine or server");}
			})
        //alert($("#terima_pertanyaan").val());
        //$("#tampil_jawaban").html($("#terima_pertanyaan").val());
    });
});