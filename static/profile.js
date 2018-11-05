/// DATE EVENT LISTENER ///
/// updates the table and records when a new date is submitted //
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

    $.post("/profile/retrieve", formData, replaceTables);
    console.log("ran AJAX");
}

function initReload(){
    console.log("initReload is on");
    $('#datesubmit').on('click', updateTables);
}

initReload();


/// Records: Edit, Submit, Cancel Event Listeners ///

function initButtons(){
console.log("initButtons is on")
$('.editbuttons').on('click', function(evt){
    evt.preventDefault();
    console.log(evt.target.value);
    var recordvalue;
    recordvalue = evt.target.value;
    var quantity1 = "#food-form-quantity1-"+recordvalue;
    var quantity2 = "#food-form-quantity2-"+recordvalue;
    $(quantity1).hide();
    $(quantity2).show();
    var submitbutton = "#food-form-button-submit-"+recordvalue;
    var cancelbutton = "#food-form-button-cancel-"+recordvalue;
    var editbutton = "#food-form-button-edit-"+recordvalue;
    var deletebutton = "#food-form-button-delete-"+recordvalue;
    $(submitbutton).show();
    $(cancelbutton).show();
    $(deletebutton).show();
    $(editbutton).hide();

    function hideButtons(){
        $(submitbutton).hide();
        $(cancelbutton).hide();
        $(deletebutton).hide();
        $(editbutton).show();
        $(".editquantity").hide();
        $(".quantity").show();
        $(submitbutton).off();
        $(cancelbutton).off();
    }

    $(submitbutton).on('click',function(event){
        event.preventDefault();
        console.log("submit button is clicked");
        $(quantity1).text($(quantity2).children().val());
        hideButtons();
        const formData = {
        recordid: event.target.value,
        newquantity: $(quantity2).children().val(),
        inputdate: $('#inputdate').val(),
        profileid: $('#profileid').val(),
        type: "update"
        }
        console.log(formData)

        $.post("/profile/updaterecords", formData, replaceTables);
        
    })

    $(cancelbutton).on('click',function(event){
        event.preventDefault();
        console.log("cancel button is clicked")
        hideButtons()
    })

    $(deletebutton).on('click', function(event){
      event.preventDefault();
      console.log("delete button is clicked");

      const formData = {
        recordid: event.target.value,
        newquantity: $(quantity2).children().val(),
        inputdate: $('#inputdate').val(),
        profileid: $('#profileid').val(),
        type: "delete"
        }

      $.post("/profile/updaterecords", formData, replaceTables);
    })

});}

initButtons()

/////////////////////////////////////////
// Adding AUTOCOMPLETE
/////////////////////////////////////////

function autocomplete(inp, arr) {
  /*the autocomplete function takes two arguments,
  the text field element and an array of possible autocompleted values:*/
  var currentFocus;
  /*execute a function when someone writes in the text field:*/
  inp.addEventListener("input", function(e) {
      var a, b, i, val = this.value;
      /*close any already open lists of autocompleted values*/
      closeAllLists();
      if (!val) { return false;}
      currentFocus = -1;
      /*create a DIV element that will contain the items (values):*/
      a = document.createElement("DIV");
      a.setAttribute("id", this.id + "autocomplete-list");
      a.setAttribute("class", "autocomplete-items");
      /*append the DIV element as a child of the autocomplete container:*/
      this.parentNode.appendChild(a);
      /*for each item in the array...*/

      var happylist;

      $.get('/profile/getfoodlistfromapi',{addfood: inp.value}, lstofresults)

      function lstofresults(results){
        const lstResults = results
        console.log(lstResults);

        happylist = lstResults; 

            for (i = 0; i < happylist.length; i++) {
                /*check if the item starts with the same letters as the text field value:*/
                if (happylist[i].substr(0, val.length).toUpperCase() == val.toUpperCase()) {
                  /*create a DIV element for each matching element:*/
                  b = document.createElement("DIV");
                  /*make the matching letters bold:*/
                  b.innerHTML = "<strong>" + happylist[i].substr(0, val.length) + "</strong>";
                  b.innerHTML += happylist[i].substr(val.length);
                  /*insert a input field that will hold the current array item's value:*/
                  b.innerHTML += "<input type='hidden' value='" + happylist[i] + "'>";
                  /*execute a function when someone clicks on the item value (DIV element):*/
                  b.addEventListener("click", function(e) {
                      /*insert the value for the autocomplete text field:*/
                      inp.value = this.getElementsByTagName("input")[0].value;
                      /*close the list of autocompleted values,
                      (or any other open lists of autocompleted values:*/
                      closeAllLists();
                  });
                  a.appendChild(b);
                }

            }
      }
  });
  /*execute a function presses a key on the keyboard:*/
  inp.addEventListener("keydown", function(e) {
      var x = document.getElementById(this.id + "autocomplete-list");
      if (x) x = x.getElementsByTagName("div");
      if (e.keyCode == 40) {
        /*If the arrow DOWN key is pressed,
        increase the currentFocus variable:*/
        currentFocus++;
        /*and and make the current item more visible:*/
        addActive(x);
      } else if (e.keyCode == 38) { //up
        /*If the arrow UP key is pressed,
        decrease the currentFocus variable:*/
        currentFocus--;
        /*and and make the current item more visible:*/
        addActive(x);
      } else if (e.keyCode == 13) {
        /*If the ENTER key is pressed, prevent the form from being submitted,*/
        e.preventDefault();
        if (currentFocus > -1) {
          /*and simulate a click on the "active" item:*/
          if (x) x[currentFocus].click();
        }
      }
  });
  function addActive(x) {
    /*a function to classify an item as "active":*/
    if (!x) return false;
    /*start by removing the "active" class on all items:*/
    removeActive(x);
    if (currentFocus >= x.length) currentFocus = 0;
    if (currentFocus < 0) currentFocus = (x.length - 1);
    /*add class "autocomplete-active":*/
    x[currentFocus].classList.add("autocomplete-active");
  }
  function removeActive(x) {
    /*a function to remove the "active" class from all autocomplete items:*/
    for (var i = 0; i < x.length; i++) {
      x[i].classList.remove("autocomplete-active");
    }
  }
  function closeAllLists(elmnt) {
    /*close all autocomplete lists in the document,
    except the one passed as an argument:*/
    var x = document.getElementsByClassName("autocomplete-items");
    for (var i = 0; i < x.length; i++) {
      if (elmnt != x[i] && elmnt != inp) {
      x[i].parentNode.removeChild(x[i]);
        }
      }
    }
/*execute a function when someone clicks in the document:*/
document.addEventListener("click", function (e) {
    closeAllLists(e.target);
});
}

autocomplete(document.getElementById("myInput"), ['a','b','c','cat','caterpillar'])


//*execute a function when the selection has been made in $('#myInput')*/
function submitFoods(){
    $('#addfoodsubmit').on('click', function(e) {
        e.preventDefault();
        const formData = {
            inputfood: $('#myInput').val(),
            profileid: $('#profileid').val(),
            inputdate: $('#inputdate').val()
        };
        $.post("/profile/addfood", formData, updateFoodsTable);
        console.log("ran AJAX POST to Foods")

    });
}

function updateFoodsTable(results){
    var status = results;
    // $(status).insertBefore($("#update-food-AJAX"));
    $("#records-table").append(status)
    console.log("re-updated Foods Table");
}

submitFoods();