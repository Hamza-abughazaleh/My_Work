
$(document).ready(function(){
$("#vote").click(function() {
     console.log("You have voted!");
     /*var data = $(this).attr("data-href")
     var id = $(this).attr("id")
     var string = "id=" + id
     console.log(string)
      $.ajax({
               type: "POST",
               url:'127.0.0.0:8000/trip/(?P<pk>\d+)/vote/',
               data: string,

               success: function() {
                      alert('You have voted');
                },*/
          });
   });
});

//var p = document.getElementById("V");
 //  var id = $('input[name="blog_id"]', $(this)).val();
 //console.log("eshi")
  // $.ajax({
    //        type: "POST",
      //      url: "{% url 'vote' pk=trip.pk %}",
        //    data: {'csrfmiddlewaretoken': '{{ csrf_token }}'},
          //  dataType: "json",
            //success: function(response) {
              //     alert(response.message);
                //   alert('Votes count is now ' + );
            // },
    //   });
