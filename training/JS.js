var dmJSON = "https://jsonplaceholder.typicode.com/users";
$.getJSON(dmJSON , function(data){
  $.each(data, function(i , f){
    var tblRow = "<tr>"+"<td><img src =http://lorempixel.com/50/50 class= rounded-circle>"+"</td>"+
                  "<td onclick=myFunctionView("+f.id+")>"+f.username + "</td>" + "</tr>"
    $(tblRow).appendTo("#entrydata");
  });
});

function myFunctionSubmit() {
var formData = $("#myForm");
$.ajax({
  type:"POST",
  url:"https://jsonplaceholder.typicode.com/users",
  data:formData,
  success: function(){},
  dataType:"json",
  contentType:"application/json"
});
}

function myFunction() {
  event.preventDefault();
  $('.form').prop("disabled", false);
  $("#view").css("display", "block");
}

function myFunctionView(id) {
  var dmJSON = "https://jsonplaceholder.typicode.com/users/";
  var final = dmJSON+id
  $("#add_user").css("display", "none");
  $.getJSON(final , function(data){
    $('#name').val( data.username);
    $('#email').val( data.email);
    $('#phone').val( data.phone);
    $('#city').val(data.address.city);
    $('#street').val( data.address.street);
    $('#website').val(data.website);
    });
}
