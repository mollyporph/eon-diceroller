var diceInput = document.getElementById("diceinput");
diceInput.addEventListener("keydown", function(e){
    if(e.keyCode === 13){
        sendDiceRoll();
    }
},false);
var r = new XMLHttpRequest();
r.onreadystatechange = function () {
  if (r.readyState != 4 || r.status != 200) return;
  var res = JSON.parse(r.responseText);
  showAndLogDiceRoll(res);
};
function sendDiceRoll(){
  var rollText = diceInput.value;
  //todo: validate rollText
  r.open("get", "/roll/"+rollText, true);
  r.send();
}
function showAndLogDiceRoll(diceresult){
  var resultDiv = document.getElementById("rollresult");
  var resultText = "You rolled " + diceresult.dicesum + " (" + diceresult.dices.join() + "). With a modifier of " +diceresult.modifier + ". You got "+diceresult.obcount+" OB rolls";
  resultDiv.innerHTML = resultText;
}
