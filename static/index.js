function WarningPopup() {
  document.getElementById("popUp").style.display = "block";
}
function cancel() {
  document.getElementById("popUp").style.display = "none";
  document.getElementById("popUp1").style.display = "none";
  document.getElementById("myPopUp1").style.display = "none";
}
window.onclick = function (event) {
  if (event.target == document.getElementById("popUp")) {
    document.getElementById("popUp").style.display = "none";
  }
};
const isEmpty = (str) => !str.trim().length;
function WarningPopup1() {
  document.getElementById("popUp1").style.display = "block";
}
function WarningPopup1() {
  document.getElementById("popUp1").style.display = "block";
}

function WarningPopup2() {
  document.getElementById("popUp2").style.display = "block";
}
