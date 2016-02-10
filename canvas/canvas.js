var c = document.getElementById("c");
var ctx = c.getContext("2d");
ctx.fillStyle = "#000000";
ctx.fillRect(60,50,50,500);

ctx.strokeStyle = "#00ff00";
ctx.strokeRect(60,50,50,500);

var d = document.getElementById("d");
var dtx = c.getContext("2d");
dtx.fillStyle = "#ff0000";
dtx.fillRect(600,50,50,500);

dtx.strokeStyle= "#0000ff";
dtx.strokeRect(600,50,50,500);
