function afterload(){
        var $Submitbtn=document.getElementById('submitBtn');

	var radios=document.getElementsByName('married');
        $Submitbtn.addEventListener("click",function(event)
        {
            event.preventDefault();
        var Fname=document.getElementById('firstName').value;
            console.log(Fname);

document.body.innerHTML += Fname;
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
