var vote = document.getElementById('candidate1');
vote.addEventListener('click', function(e){
    var popup = document.getElementById('popup');
    var candidates1 = document.getElementById('candidates1').innerText;
    var nama = document.getElementById('nama');
    nama.innerHTML = "You choose " + candidates1 + ".";
    popup.style.display = "flex"
});

var vote = document.getElementById('candidate2');
vote.addEventListener('click', function(e){
    var popup = document.getElementById('popup');
    var candidates2 = document.getElementById('candidates2').innerText;
    var nama = document.getElementById('nama');
    nama.innerHTML = "You choose " + candidates2 + ".";
    popup.style.display = "flex"
});

var vote = document.getElementById('candidate3');
vote.addEventListener('click', function(e){
    var popup = document.getElementById('popup');
    var candidates3 = document.getElementById('candidates3').innerText;
    var nama = document.getElementById('nama');
    nama.innerHTML = "You choose " + candidates3 + ".";
    popup.style.display = "flex"
});

var no = document.getElementById('no');
no.addEventListener('click', function(e){
    var popup = document.getElementById('popup');
    popup.style.display = "none"
    e.stopPropagation();
});

var yes = document.getElementById('yes');
yes.addEventListener('click', function(e){
    // halaman yg di tuju
    e.stopPropagation();
});