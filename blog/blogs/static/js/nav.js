const nav_btn = document.getElementById("nav-btn");
const mobile_link_div = document.getElementById("mobile-link-div");

nav_btn.addEventListener("click", function(){
    mobile_link_div.classList.toggle('show');
});