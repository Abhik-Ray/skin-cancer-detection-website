$(document).ready(function(){
  setColor();
  $("#theme-button").click(function(){
      let theme;
      $("html").attr("data-theme") === "light" ? theme="dark" : theme="light";
      $("html").attr("data-theme", theme);

      var img1 = "bi bi-moon-fill",
      img2 = "bi bi-brightness-high-fill";
      var imgElement = document.getElementById("theme-button");
      imgElement.className = imgElement.className === img1 ? img2 : img1;
      imgElement.style = imgElement.className === img1? "font-size: 40px; color: black": "font-size: 40px; color: white";
  });
});

function setColor() {
  var progressBar = document.getElementsByClassName("progress-bar");
  percent = parseFloat(
    document
      .getElementsByClassName("progress-bar")[0]
      .getAttribute("aria-valuenow")
  );
  if (percent < 33.3) {
    progressBar[0].style.backgroundColor = "green";
  } else if (percent < 66.6) {
    progressBar[0].style.backgroundColor = "darkgoldenrod";
  } else progressBar[0].style.backgroundColor = "red";
}
