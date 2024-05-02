function dropdownMenu(){
    var x=document.getElementById("dropdownClick");
    if (x.className==="topnav"){
        x.className +=" responsive";
    }else{
        x.className ="topnav";
    }
}