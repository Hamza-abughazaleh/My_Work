/*
			alert('Hello World');
			console.log('Secret Massege');
			console.log('hahahah');
			console.log('mmmmmm');
			document.write('hello Word'); */

/*var $hamza=5;
var $ghaith="Ha HA HA";
var $khaled=true;
var $husam;
var $ibra=null;
alert($hamza+0);
alert($hamza*0);
alert($hamza-0);
alert($hamza/0);
alert($hamza%2);
alert($hamza);						
console.log($hamza);
console.log($hamza);
console.log($ghaith);
console.log($khaled);
console.log($husam);
console.log($ibra);*/
/*var $global="hamza";

function fixed(a,b){
var $net=(a+b).toFixed(2)+"  "+$global;
alert("$"+$net);
}

function fixed2(a,b){
var $net=(a+b).toFixed(2);
return $net;
}

var x=20.1212;
var y=40.56;
fixed(x,y);
alert(fixed2(x,y));*/







/*function loops(){
	var y=9;
	for(var i=1;i<=12;i++)
		if(i!=5)
		{
			var resu=y*i;
			console.log(y+"*"+i+"="+resu);
		}
}
loops();*/

/*function loops(){
	var y=1;
	for(y=1;y<=12;y++)
		{for(var i=1;i<=12;i++)
		{resu=y*i;
		document.write(y+"*"+i+"="+resu+" &nbsp &nbsp &nbsp");}
		document.write("<br>");}
		
}
loops();*/


/*var users=[
	{name:"hamza", age:"23"},
	{name:"ghaith", age:"25"}
];
for (var i=0;i<users.length;i++){
	var user=users[i];
	console.log(user.name+" is"+" "+user.age+" years old.");
}



var users=[
	{name:"hamza", age:"23"},
	{name:"ghaith", age:"25"}
];
for (var i=0;i<users.length;i++){
	var user=users[i];
	console.log(user);
}*/


/*var users=[
	{recipetitle:"lkdfzkld",servings:"23",ingredients:['a','b'] ,directions:"left right"},
	{recipetitle:"dfjnKJ",servings:"23",ingredients:['a','b'] ,directions:"left right"},
];
	for (var i=0;i<users.length;i++){
	var user=users[i];
	console.log(user);
	}*/
/*function afterload () {
	var img1= document.getElementById("vardom");
	
	console.log(img1.src);

	img1.src = 'http://placekitten.com/g/600/500';
	console.log(img1.src);

}

function addElement(){

 	 var newbutton = document.createElement("button"); 
 	 var newContent = document.createTextNode("Hi there and greetings!"); 
 	 newbutton.appendChild(newContent); 

	 document.body.appendChild(newbutton); 

}


window.onload = function(){
afterload();
addElement();

}*/
/*var link1=document.getElementById('a');
link1.addEventListener('click',function(event){
event.preventDefault();
});*/

/*link1.addEventListener('click',function(event){
alert("Hello!");
});*/

/*function afterload () {
var button1=document.getElementById('button');
button1.addEventListener('click',function(event){
var  btn = event.currentTarget;

 	 btn.style.backgroundColor = 'red';
	  btn.innerHTML = 'Clicked!';
});


}*/


$(document).ready(function() {
    $('.toggle-nav').click(function(e) {
        $(this).toggleClass('active');
        $('.menu ul').toggleClass('active');

        e.preventDefault();


    });
$('.dropdown-content').parent().click( function() {

        var sub= $(this).children('.dropdown-content');

         $(sub).toggle();
      
    });   

$('.dropdown-content').parent().focusout( function() {

        var sub= $(this).children('.dropdown-content');

        
            $(sub).hide();
       
    }); 
 
});

alert(123);



window.onload = function(){
alert("onload")

hamza();
};

function hamza(){
alert("zdfas");

}













