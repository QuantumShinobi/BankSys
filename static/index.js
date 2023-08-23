function WarningPopup() {
  document.getElementById("popUp").style.display = "block";
}
function cancel() {
  document.getElementById("popUp").style.display = "none";
  document.getElementById("popUp1").style.display = "none";
  document.getElementById("popUp2").style.display = "none";

  document.getElementById("myPopUp1").style.display = "none";
  document.getElementById("myPopUp2").style.display = "none";
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

document.addEventListener("DOMContentLoaded", () => {
  var adding = document.getElementsByClassName("Add");
  var withdraw = document.getElementsByClassName("Withdraw");
  for (var i = 0; i < adding.length; i++) {
    var element = adding[i];
    element.style.color = "green";
  }
  for (let i = 0, len = withdraw.length; i < len; i++) {
    withdraw[i].style.color = "red";
  }
});

document.addEventListener("DOMContentLoaded", () => {
  var times = document.getElementsByClassName("time");
  for (var i = 0; i < times.length; i++) {
    element = times[i];
    var utcTimeString = element.innerHTML + " UTC";
    utcTimeString = utcTimeString.replace(".", "");
    utcTimeString = utcTimeString.replace(".", "");
    utcTimeString = utcTimeString.replace(".", "");
    const utcDate = new Date(utcTimeString);
    const timezone = Intl.DateTimeFormat().resolvedOptions().timeZone;
    const usertime = Intl.DateTimeFormat("en-US", {
      hour: "numeric",
      minute: "numeric",
      second: "numeric",
      year: "numeric",
      month: "short",
      day: "numeric",
      hour12: true,
      timeZone: timezone,
    });
    element.innerHTML = usertime.format(utcDate);
  }
});

// function time_ago(time) {
//   switch (typeof time) {
//     case "number":
//       break;
//     case "string":
//       time = +new Date(time);
//       break;
//     case "object":
//       if (time.constructor === Date) time = time.getTime();
//       break;
//     default:
//       time = +new Date();
//   }
//   var time_formats = [
//     [60, "seconds", 1], // 60
//     [120, "1 minute ago", "1 minute from now"], // 60*2
//     [3600, "minutes", 60], // 60*60, 60
//     [7200, "1 hour ago", "1 hour from now"], // 60*60*2
//     [86400, "hours", 3600], // 60*60*24, 60*60
//     [172800, "Yesterday", "Tomorrow"], // 60*60*24*2
//     [604800, "days", 86400], // 60*60*24*7, 60*60*24
//     [1209600, "Last week", "Next week"], // 60*60*24*7*4*2
//     [2419200, "weeks", 604800], // 60*60*24*7*4, 60*60*24*7
//     [4838400, "Last month", "Next month"], // 60*60*24*7*4*2
//     [29030400, "months", 2419200], // 60*60*24*7*4*12, 60*60*24*7*4
//     [58060800, "Last year", "Next year"], // 60*60*24*7*4*12*2
//     [2903040000, "years", 29030400], // 60*60*24*7*4*12*100, 60*60*24*7*4*12
//     [5806080000, "Last century", "Next century"], // 60*60*24*7*4*12*100*2
//     [58060800000, "centuries", 2903040000], // 60*60*24*7*4*12*100*20, 60*60*24*7*4*12*100
//   ];
//   var seconds = (+new Date() - time) / 1000,
//     token = "ago",
//     list_choice = 1;

//   if (seconds == 0) {
//     return "Just now";
//   }
//   if (seconds < 0) {
//     seconds = Math.abs(seconds);
//     token = "from now";
//     list_choice = 2;
//   }
//   var i = 0,
//     format;
//   while ((format = time_formats[i++]))
//     if (seconds < format[0]) {
//       if (typeof format[2] == "string") return format[list_choice];
//       else
//         return Math.floor(seconds / format[2]) + " " + format[1] + " " + token;
//     }
//   return time;
// }
// const utcTimeString = "Aug 23, 2023, 4:37 PM UTC";
// const utcDate = new Date(utcTimeString);

// console.log(time_ago(utcDate));
