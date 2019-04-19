
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
				error : function(){$("#tampil_jawaban").html("error occured in the engine or server");},
				cache : false
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
					//$("#tampil_jawaban").html(data);
					if (data.length==1){
						$("#tampil_jawaban").html(data.length);
					}
					else {
						var string = [];
						var i;
						string.push(data[0]);
						string.push("<ul>");
						for(i = 1; i<data.length; i++){
							string.push("<li>");
							string.push(data[i]);
							string.push("</li>");
						}
						string.push("</ul>");
						$("#tampil_jawaban").html(string.join(""))
					}
				},
				error : function(){$("#tampil_jawaban").html("error occured in the engine or server");},
				cache : false
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
					//$("#tampil_jawaban").html(data);
					if (data.length==1){
						$("#tampil_jawaban").html(data.length);
					}
					else {
						var string = [];
						var i;
						string.push(data[0]);
						string.push("<ul>");
						for(i = 1; i<data.length; i++){
							string.push("<li>");
							string.push(data[i]);
							string.push("</li>");
						}
						string.push("</ul>");
						$("#tampil_jawaban").html(string.join(""))
					}
				},
				error : function(){$("#tampil_jawaban").html("error occured in the engine or server");},
			})
        //alert($("#terima_pertanyaan").val());
        //$("#tampil_jawaban").html($("#terima_pertanyaan").val());
    });
});