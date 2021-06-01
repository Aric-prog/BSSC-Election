

var popup = document.getElementById('popup');
var clicked_candidate = 0;
var no = document.getElementById('no');
var yes = document.getElementById('yes');

no.style.pointerEvents = "none"
yes.style.pointerEvents = "none"
popup.style.transition = "opacity 0.3s"

function setCandidate(arg) {
    // clicked_candidate = this.getAttribute("data-value");
    clicked_candidate = arg.split("-")[1]
    var candidate = document.getElementById("candidate-name-" + clicked_candidate).innerHTML
    var nama = document.getElementById('nama');
    nama.innerHTML = "You choose " + candidate + ".";
    popup.style.opacity = 1
    yes.style.pointerEvents = "auto"
    no.style.pointerEvents = "auto"
}
// vote.addEventListener('click', function(e){
//     var candidates = document.getElementById('candidates').innerText;
//     var nama = document.getElementById('nama');
//     nama.innerHTML = "You choose " + candidates + ".";
//     popup.style.opacity = 1
//     yes.style.pointerEvents = "auto"
//     no.style.pointerEvents = "auto"
// });

no.addEventListener('click', function(e){
    popup.style.opacity = 0
    no.style.pointerEvents = "none"
    yes.style.pointerEvents = "none"
    e.stopPropagation();
});

yes.addEventListener('click', function(e){
    // POST request here with clicked_candidate as value
    console.log(clicked_candidate)
    $.post(("/vote/" + clicked_candidate), {}, function(data){
        window.location = data
    })
    e.stopPropagation();
});