function countDownLoop(index){
    var i;
    var buttonExecuted = false;
    var now = new Date().getTime();
    var output = ''
    for (i =1; i < index ; i++){
        if(document.getElementById("counter"+i.toString()).innerHTML == "Completed"){
            continue;
        }
        var myTime = document.getElementById("targetTime"+ i.toString()).innerHTML;
        var countDownDate = new Date(myTime).getTime();
        var diff = countDownDate - now;
        if (diff < 0 || pushedList[i-1] == 'True' ){
            output = "Completed"
            pushNotiButton(i, pushedList)
            //document.getElementById("pushB"+i.toString()).click();    
        } else{
            var days = Math.floor(diff / (1000 * 60 * 60 * 24));
            var hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            var minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
            var seconds = Math.floor((diff % (1000 * 60)) / 1000);
            output = days + "d " + hours + "h "+ minutes + "m " + seconds + "s ";
            
            if (days < 2 && days >= 0){
            document.getElementById("counter"+i.toString()).style.color = "red";
            }
         
        }
        
        document.getElementById("counter"+i.toString()).innerHTML = output;      
        //console.log(diff);
    }
}

function pushNotiButton(index, pushedList){
    if(pushedList[index-1] == "False"){
        console.log("need to push this")
        
        //document.getElementById("pushB"+index.toString()).click()
        
        // AJAX to not reload the page
        
        var xhttp = new XMLHttpRequest();
        xhttp.open("GET", document.getElementById("pushB"+index.toString()).href, false);
        xhttp.send();
    }
    else{
        console.log("My noti has been pushed" + index.toString())
    }
}
