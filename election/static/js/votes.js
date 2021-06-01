var button = document.getElementById('vote_now');
button.addEventListener('click', function(e){
    var popup = document.getElementById('popup');
    popup.style.display = "flex"
});

var okay = document.getElementById('okay');
okay.addEventListener('click', function(e){
    var popup = document.getElementById('popup');
    popup.style.display = "none"
    e.stopPropagation();
});

