function delWarning(id) {
    var delId = id.split("_");
    var delUrl = "/notification/delete/" + delId[1];
    var answer = confirm("warning");
    if (answer) {
        window.location.href = delUrl;
    }
    
    else {
        alert("canceled by user");
    }
}

function showProfile(){
	alert("Haven't figured out how to do this")
}