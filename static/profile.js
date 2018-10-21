function replaceTables(results){
    var status = results;
    $('#profiletables').html(status);
    console.log("Finished replaceTables");
}

function updateTables(evt){
    evt.preventDefault()
    const formData = {
            inputdate: $('#inputdate').val(),
            profileid: $('#profileid').val()
        }

    $.get("/profile/retrieve", formData, replaceTables);
    console.log("ran AJAX");
}

function initReload(){
    console.log("initReload is on");
    $('#date-form').on('submit', updateTables);
}

initReload();
console.log("please run");