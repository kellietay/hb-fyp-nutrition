/// DATE EVENT LISTENER ///
/// updates the table and records when a new date is submitted //
function replaceTables(results){
    var status = results;
    $('#profiletables').html(status);
    console.log("Finished replaceTables");

}

// function updateTables(evt){
//     evt.preventDefault()
//     const formData = {
//             inputdate: $('#inputdate').val(),
//             profileid: $('#profileid').val()
//         }

//     $.get("/profile/retrieve", formData, replaceTables);
//     console.log("ran AJAX");
// }

// function initReload(){
//     console.log("initReload is on");
//     $('#datesubmit').on('click', updateTables);
// }

// initReload();


/// Record Modal Popup: ///
/// 1. Event Listener on button///
/// 2. on click, open modal (automatic), and run AJAX call to display food and its nutrients///
/// 3. Event Listerner on Submit Buttoon to update record in database, followed by AJAX call ///
///    to refresh the relevant sections ///

function initFoodDiary(){
console.log("initFoodDiary is on")
$('.food-diary-buttons').off()
$('.food-diary-buttons').on('click', function(evt){
  var record_id = $(evt.target).data('record_id')
  console.log(record_id)

  /// Update Information in Modal with data in target button///
  /// Tested and confirmed it works ///
  $('#modal-btn-update').val(record_id)
  $('#modal-btn-delete').val(record_id)
  $('#modal-quantity').attr("placeholder",$(evt.target).data("serving_qty"))
  $('#modal-food').text($(evt.target).data('food_name') + ", " 
    + $(evt.target).data('serving_unit')
    + " (" 
    + $(evt.target).data('serving_weight_grams')
    + "g)")
  $('#modal-calories').text($(evt.target).data('calories'))
  $('#modal-carbohydrates').text($(evt.target).data('carbohydrates'))
  $('#modal-fiber').text($(evt.target).data('fiber'))
  $('#modal-fat').text($(evt.target).data('fat'))
  $('#modal-protein').text($(evt.target).data('protein'))
  $('#modal-vitA').text($(evt.target).data('vitA'))
  $('#modal-vitC').text($(evt.target).data('vitC'))
  $('#modal-vitD').text($(evt.target).data('vitD'))
  $('#modal-vitE').text($(evt.target).data('vitE'))
  $('#modal-vitB6').text($(evt.target).data('vitB6'))
  $('#modal-vitB12').text($(evt.target).data('vitB12'))
  $('#modal-thiamin').text($(evt.target).data('thiamin'))
  $('#modal-riboflavin').text($(evt.target).data('riboflavin'))
  $('#modal-niacin').text($(evt.target).data('niacin'))
  $('#modal-folate').text($(evt.target).data('folate'))
  $('#modal-calcium').text($(evt.target).data('calcium'))
  $('#modal-iodine').text($(evt.target).data('iodine'))
  $('#modal-iron').text($(evt.target).data('iron'))
  $('#modal-magnesium').text($(evt.target).data('magnesium'))
  $('#modal-phosphorus').text($(evt.target).data('phosphorus'))
  $('#modal-selenium').text($(evt.target).data('selenium'))
  $('#modal-zinc').text($(evt.target).data('zinc'))
  $('#modal-potassium').text($(evt.target).data('potassium'))
  $('#modal-sodium').text($(evt.target).data('sodium'))
  $('#modal-chloride').text($(evt.target).data('chloride'))
  $('#modal-copper').text($(evt.target).data('copper'))

  /// Create event listener for Update Quantiy Button ///

  $('#modal-btn-update').on('click', function(event) {
    event.preventDefault();
    console.log('modal-btn-update is clicked')
    console.log('recordid is ' + event.target.value)
    const formData = {
      recordid: event.target.value,
      newquantity: $('#modal-quantity').val(),
      inputdate: $('#inputdate').val(),
      profileid: $('#profileid').val(),
      type: 'update'
    }
    console.log(formData)
    $('#quantity1-' + record_id).text($('#modal-quantity').val() 
      + ".0 - " 
      + $(evt.target).data('food_name') 
      + ", " 
      + $(evt.target).data('serving_unit')
      + " (" 
    + $(evt.target).data('serving_weight_grams')
    + "g)")
    
    $.post("/profile/updaterecords", formData, function(data){
      replaceTables(data);
      $('#modal-btn-update').off()
      $('#modal-btn-close').off();;
    })
  }) /// End event listener for #modal-btn-update ///

  $('#modal-btn-delete').on('click', function(event) {
    event.preventDefault();
    console.log('modal-btn-delete is clicked')
    const formData = {
      recordid: event.target.value,
      newquantity: $('#modal-quantity').val(),
      inputdate: $('#inputdate').val(),
      profileid: $('#profileid').val(),
      type: 'delete'
    }
    console.log(formData)
    $('#button-' + record_id).hide()

    $.post("/profile/updaterecords", formData, function(data){
      replaceTables(data); 
      $('#button-' + record_id).hide(); 
      $('#modal-btn-delete').off();
      $('#modal-btn-close').off(); })
    }) // End event listener for #modal-btn-delete ///

  $('#modal-btn-delete').on('click', function (event){
    $('#modal-btn-delete').off();
    $('#modal-btn-close').off();
    $('#modal-btn-update').off()
  })
  }) // End event lister for food-button//

} // End Function initFoodDiary() //

initFoodDiary();

/// Records: Edit, Submit, Cancel Event Listeners ///

// function initButtons(){
// console.log("initButtons is on")
// $('.editbuttons').on('click', function(evt){
//     evt.preventDefault();
//     console.log(evt.target.value);
//     var recordvalue;
//     recordvalue = evt.target.value;
//     var quantity1 = "#food-form-quantity1-"+recordvalue;
//     var quantity2 = "#food-form-quantity2-"+recordvalue;
//     $(quantity1).hide();
//     $(quantity2).show();
//     var submitbutton = "#food-form-button-submit-"+recordvalue;
//     var cancelbutton = "#food-form-button-cancel-"+recordvalue;
//     var editbutton = "#food-form-button-edit-"+recordvalue;
//     var deletebutton = "#food-form-button-delete-"+recordvalue;
//     $(submitbutton).show();
//     $(cancelbutton).show();
//     $(deletebutton).show();
//     $(editbutton).hide();

//     function hideButtons(){
//         $(submitbutton).hide();
//         $(cancelbutton).hide();
//         $(deletebutton).hide();
//         $(editbutton).show();
//         $(".editquantity").hide();
//         $(".quantity").show();
//         $(submitbutton).off();
//         $(cancelbutton).off();
//     }

//     $(submitbutton).on('click',function(event){
//         event.preventDefault();
//         console.log("submit button is clicked");
//         $(quantity1).text($(quantity2).children().val());
//         hideButtons();
//         const formData = {
//         recordid: event.target.value,
//         newquantity: $(quantity2).children().val(),
//         inputdate: $('#inputdate').val(),
//         profileid: $('#profileid').val(),
//         type: "update"
//         }
//         console.log(formData)

//         $.post("/profile/updaterecords", formData, replaceTables);
        
//     })

//     $(cancelbutton).on('click',function(event){
//         event.preventDefault();
//         console.log("cancel button is clicked")
//         hideButtons()
//     })

//     $(deletebutton).on('click', function(event){
//       event.preventDefault();
//       console.log("delete button is clicked");

//       const formData = {
//         recordid: event.target.value,
//         newquantity: $(quantity2).children().val(),
//         inputdate: $('#inputdate').val(),
//         profileid: $('#profileid').val(),
//         type: "delete"
//         }

//       $.post("/profile/updaterecords", formData, replaceTables);
//     })

// });}

// initButtons()

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
    $("#records-button").append(status);
    initFoodDiary();
    console.log("re-updated Foods Table");
}

submitFoods();

//////////////////////

// var ctx = document.getElementById('myChart').getContext('2d');
// var chart = new Chart(ctx, {
//     // The type of chart we want to create
//     type: 'line',

//     // The data for our dataset
//     data: {
//         labels: ["January", "February", "March", "April", "May", "June", "July"],
//         datasets: [{
//             label: "My First dataset",
//             backgroundColor: 'rgb(255, 99, 132)',
//             borderColor: 'rgb(255, 99, 132)',
//             data: [0, 10, 5, 2, 20, 30, 45],
//         }]
//     },
//     // Configuration options go here
//     options: {}
// });



// var atx = document.getElementById('myPieChart').getContext('2d');
// var chart = new Chart(atx, {
//     // The type of chart we want to create
//     type: 'doughnut',

//     // The data for our dataset
//     data: {
//         labels: ['Calories', "remaining"],
//         datasets: [{
//             label: "My First dataset",
//             backgroundColor: ['rgb(255, 99, 132)', 'rgb(255,200,200)'],
//             data: [1000, 1200]
//         }]
//     },
//     options: {
//       // tooltipEvents: [],
//       //   showTooltips: true,
//       //   onAnimationComplete: function() {
//       //       this.showTooltip(this.segments, true);
//       //   },
//       //   tooltipTemplate: "<%= label %> - <%= data %>"
//     }
// });



// Display Modal Information //
