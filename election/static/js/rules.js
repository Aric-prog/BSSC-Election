var button = document.getElementById('agree');
button.addEventListener('click', function(e){
    e.preventDefault();
    var agree_rules = document.getElementById('agree_rules');
    var error = document.getElementById('error');
    error.innerHTML="";
    if(agree_rules.checked == false){
        error.innerHTML = "Please centang check box ini"
    }
    if(error.innerHTML != ""){
        error.style.display = 'block';
    }else{
        // lokasi tujuan href
        document.location.href = 'votes_now.html'
    }
});