

function afterload () {

var radios=document.getElementsByName('married');
        
        

        var $Submitbtn=document.getElementById('submitBtn');
        
        $Submitbtn.addEventListener("click",function(event)
        {
            event.preventDefault();
            var Fname=document.getElementById('firstName').value;
            console.log(Fname);
            for(var i=0;i<radios.length;i++)
            {
                if(radios[i].checked)
                {
                    var radioValue=radios[i].value;
                    console.log(radioValue);
                    break;
                }
            }
        });
}
