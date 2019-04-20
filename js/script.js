		
$(document).ready(function() {
    $("#regex").click(function(){
		var divbot = document.createElement('div');
		divbot.setAttribute('class','chat chatbot');
		var paragraph = document.createElement('P');
		paragraph.setAttribute('class','nama');
		paragraph.innerHTML = "chatbot";
		divbot.appendChild(paragraph);
		var paragraphans = document.createElement('P');
		paragraphans.setAttribute('class','chat-message');
		paragraphans.innerHTML = "";
		paragraphans.id = 'tampil_jawaban';
		divbot.appendChild(paragraphans);
		var divself = document.createElement('div');
		divself.setAttribute('class','chat self');
		paragraph = document.createElement('P');
		paragraph.setAttribute('class','nama');
		paragraph.innerHTML = "kamu";
		divself.appendChild(paragraph);
		paragraph = document.createElement('P');
		paragraph.setAttribute('class','chat-message');
		paragraph.innerHTML = $("#terima_pertanyaan").val();
		divself.appendChild(paragraph);
		var stylechange = document.getElementsByClassName("chatlog");
		stylechange[0].appendChild(divself);
		$.ajax({
				type : "POST",
				url : "juro.php",
				dataType : 'json',
				data : {question : $("#terima_pertanyaan").val(), method : 'regex'},
				success : function(data){
					paragraphans.innerHTML = data;
					stylechange[0].appendChild(divbot);
					stylechange = document.getElementsByClassName("chatlog");
					stylechange[0].scrollTop = stylechange[0].scrollHeight;
					//var stylechange = 
					//	document.getElementsByClassName("Jawaban");
					//stylechange[0].style.visibility = "visible";
				},
				error : function(){
					paragraphans.innerHTML = data;
					stylechange[0].appendChild(divbot);
					stylechange = document.getElementsByClassName("chatlog");
					stylechange[0].scrollTop = stylechange[0].scrollHeight;},
				cache : false
			})
        //alert($("#terima_pertanyaan").val());
		//$("#tampil_jawaban").html($("#terima_pertanyaan").val());
    });
});

$(document).ready(function() {
    $("#kmp").click(function(){
		var divbot = document.createElement('div');
		divbot.setAttribute('class','chat chatbot');
		var paragraph = document.createElement('P');
		paragraph.setAttribute('class','nama');
		paragraph.innerHTML = "chatbot";
		divbot.appendChild(paragraph);
		var paragraphans = document.createElement('P');
		paragraphans.setAttribute('class','chat-message');
		paragraphans.innerHTML = "";
		paragraphans.id = 'tampil_jawaban';
		divbot.appendChild(paragraphans);
		var divself = document.createElement('div');
		divself.setAttribute('class','chat self');
		paragraph = document.createElement('P');
		paragraph.setAttribute('class','nama');
		paragraph.innerHTML = "kamu";
		divself.appendChild(paragraph);
		paragraph = document.createElement('P');
		paragraph.setAttribute('class','chat-message');
		paragraph.innerHTML = $("#terima_pertanyaan").val();
		divself.appendChild(paragraph);
		var stylechange = document.getElementsByClassName("chatlog");
		stylechange[0].appendChild(divself);
		$.ajax({
				type : "POST",
				url : "juro.php",
				dataType : 'json',
				data : {question : $("#terima_pertanyaan").val(), method : 'kmp'},
				success : function(data){
					//$("#tampil_jawaban").html(data);
					if (data.length==1){
						paragraphans.innerHTML = data;
						stylechange[0].appendChild(divbot);
						stylechange = document.getElementsByClassName("chatlog");
						stylechange[0].scrollTop = stylechange[0].scrollHeight;
						//var stylechange = 
						//document.getElementsByClassName("Jawaban");
						//stylechange[0].style.visibility = "visible";
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
						paragraphans.innerHTML = string.join("");
						stylechange[0].appendChild(divbot);
						stylechange = document.getElementsByClassName("chatlog");
						stylechange[0].scrollTop = stylechange[0].scrollHeight;
						//var stylechange = 
						//document.getElementsByClassName("Jawaban");
						//stylechange[0].style.visibility = "visible";
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
		var divbot = document.createElement('div');
		divbot.setAttribute('class','chat chatbot');
		var paragraph = document.createElement('P');
		paragraph.setAttribute('class','nama');
		paragraph.innerHTML = "chatbot";
		divbot.appendChild(paragraph);
		var paragraphans = document.createElement('P');
		paragraphans.setAttribute('class','chat-message');
		paragraphans.innerHTML = "";
		paragraphans.id = 'tampil_jawaban';
		divbot.appendChild(paragraphans);
		var divself = document.createElement('div');
		divself.setAttribute('class','chat self');
		paragraph = document.createElement('P');
		paragraph.setAttribute('class','nama');
		paragraph.innerHTML = "kamu";
		divself.appendChild(paragraph);
		paragraph = document.createElement('P');
		paragraph.setAttribute('class','chat-message');
		paragraph.innerHTML = $("#terima_pertanyaan").val();
		divself.appendChild(paragraph);
		var stylechange = document.getElementsByClassName("chatlog");
		stylechange[0].appendChild(divself);
		$.ajax({
				type : "POST",
				url : "juro.php",
				dataType : 'json',
				data : {question : $("#terima_pertanyaan").val(), method : 'bm'},
				success : function(data){
					//$("#tampil_jawaban").html(data);
					if (data.length==1){
						paragraphans.innerHTML = data;
						stylechange[0].appendChild(divbot);
						stylechange = document.getElementsByClassName("chatlog");
						stylechange[0].scrollTop = stylechange[0].scrollHeight;
					//$("#tampil_jawaban").html(data);
					//var stylechange = 
			//document.getElementsByClassName("Jawaban");
			//stylechange[0].style.visibility = "visible";
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
						paragraphans.innerHTML = string.join("");
						stylechange[0].appendChild(divbot);
						stylechange = document.getElementsByClassName("chatlog");
						stylechange[0].scrollTop = stylechange[0].scrollHeight;//$("#tampil_jawaban").html(string.join(""))
						//var stylechange = 
						//document.getElementsByClassName("Jawaban");
						//stylechange[0].style.visibility = "visible";
					}
				},
				error : function(){$("#tampil_jawaban").html("error occured in the engine or server");},
			})
        //alert($("#terima_pertanyaan").val());
        //$("#tampil_jawaban").html($("#terima_pertanyaan").val());
    });
});