var button = document.getElementById('vote_now');
var okay = document.getElementById('okay');
var popup = document.getElementById('popup');

popup.style.transition = "opacity 0.3s"
popup.style.opacity = 0;
okay.style.pointerEvents = "none"
button.addEventListener('click', function(e){
    popup.style.opacity = 1
    okay.style.pointerEvents = "auto"
});

okay.addEventListener('click', function(e){
    popup.style.opacity = 0
    okay.style.pointerEvents = "none"
    e.stopPropagation();
});

