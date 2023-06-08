let navbarIcon = document.querySelector(".navbar-hidden");
let navbar = document.querySelector(".navbar-item-hidden");
navbarIcon.addEventListener("click", function (event) {
  event.preventDefault();
  if (navbar.style.display === "none") {
    navbar.style.display = "flex";
  } else {
    navbar.style.display = "none";
  }
});
