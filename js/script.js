$(document).ready(function() {
    $("#submit_pertanyaan").click(function(){
        //alert($("#terima_pertanyaan").val());
        $("#tampil_jawaban").html($("#terima_pertanyaan").val());
    });
});