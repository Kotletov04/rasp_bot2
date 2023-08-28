
function myFunction() {
    document.getElementById("open_zach").classList.toggle("show");
}

window.onclick = function(event) {
    if (!event.target.matches('.button_zach')) {
      var dropdowns = document.getElementsByClassName("zach_content");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
  }

