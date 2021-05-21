function isValidate() {
    document.getElementById("error-subject").style.display="none";
    document.getElementById("error-question").style.display="none";

    var q = document.getElementById("question");
    var s = document.getElementById("subject");
    var invalid = s.value == "--Choose your subject here--";
    var flag = 0;
  
    if (invalid) {
        document.getElementById("error-subject").style.display="block";
        flag=1;
    }
    
    if(q.value==""){
        document.getElementById("error-question").style.display="block";
        flag=1;
    }

    if(flag==0) {
        var modal = document.getElementById("modal");
        var btn = document.getElementById("submitBtn");
        var close = document.getElementById("closeBtn");
        
        btn.onclick = function() {
            modal.style.display = "flex";
            // document.getElementById("error-subject").style.display="none";
            // document.getElementById("error-question").style.display="none";
        }
        
        close.onclick = function() {
            modal.style.display = "none";
            location.reload();
        }
    }
}