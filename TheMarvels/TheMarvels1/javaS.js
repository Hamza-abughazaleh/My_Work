
$(document).ready(function(){
$('textarea').focusin(function(){
   $(this).attr('placeholder','');
});
$("textarea").focusout(function(){
    $(this).attr('placeholder', "Your answer");
});



});
		

$(document).ready(function() {
    $('.toggle-nav').click(function(e) {
        $(this).toggleClass('active');
        e.preventDefault();
    });
});

