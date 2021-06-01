document.getElementById("logout-modal").style.opacity=0
document.getElementById("profile-button").style.pointerEvents = "none"
document.getElementById("logout-button").style.pointerEvents = "none"
function showModal(){
    document.getElementById("logout-modal").style.transition = "opacity 0.3s"
    document.getElementById("logout-modal").style.opacity=1;
    document.getElementById("profile-button").style.pointerEvents = "auto"
    document.getElementById("logout-button").style.pointerEvents = "auto"
}
function hideModal(){
    document.getElementById("logout-modal").style.opacity=0;
    document.getElementById("profile-button").style.pointerEvents = "none"
    document.getElementById("logout-button").style.pointerEvents = "none"
}