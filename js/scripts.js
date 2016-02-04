

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
  username_element = document.getElementById("username");
  room_element = document.getElementById("room");
  username = username_element.value;
  room = room_element.value;
  socket.emit("join", {username: username, room: room});

  //Hide everything that has to do with room after you've joined
  username_element.style.visibility='hidden';
  room_element.style.visibility='hidden';
  document.getElementById("joinButton").style.visibility='hidden';

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

   //Last roll should be first in the list
   ul.insertBefore(li,ul.firstChild);
   var ul = document.getElementById('rollresult');

   //Make sure that we only show the 10 newest rolls
if (ul.childNodes.length > 10)
  ul.lastChild.parentNode.removeChild(ul.lastChild);
}
