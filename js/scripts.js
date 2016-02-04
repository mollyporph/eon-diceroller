

var username ="";
var room ="";
var socket = io();
socket.on('connect', function () {
    socket.on('dicerollresponse', function(msg){
    console.log(msg);
    showAndLogDiceRoll(msg);
    });
  });
var joinButton = document.getElementById("joinButton");
joinButton.addEventListener("click",function(e){
  username = document.getElementById("username").value;
  room = document.getElementById("room").value;
  socket.emit("join", {username: username, room: room});
});
var diceInput = document.getElementById("diceinput");
diceInput.addEventListener("keydown", function(e){
    if(e.keyCode === 13){
        sendDiceRoll();
    }
},false);
function sendDiceRoll(){
  var rollText = diceInput.value;
  socket.emit("dicerollrequest", {username:username,room:room,roll:rollText });
}
function showAndLogDiceRoll(diceresult){
  var resultText = diceresult.username+" rolled " + diceresult.dicesum + " (" + diceresult.dices.join() + "). With a modifier of " +diceresult.modifier + ". and got "+diceresult.obcount+" OB rolls";
  var ul = document.getElementById("rollresult");
   var li = document.createElement("li");
   li.appendChild(document.createTextNode(resultText));
   ul.appendChild(li);
}
