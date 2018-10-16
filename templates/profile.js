
var url = window.location.href
var params = url.split('profile')

let myinputdate = $("#inputdate")

function replaceTables(results){
    var status = results;
    $('#profiletables').html(status)
    console.log("Finished replaceTables")
}

function updateTables(){
    $.get("/profile" + params[1], {inputdate: myinputdate.value}, replaceTables);
    console.log("Finished sending AJAX")
}


$("#inputdate").on('change', updateTables);




