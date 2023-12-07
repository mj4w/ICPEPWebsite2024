var userFunc = document.getElementById("user");

userFunc.addEventListener("click", function() {

document.getElementById("user-function").style.display = "block";
document.getElementById("close-user").style.display = "block";
this.style.display = "none";
});

let subMenu = document.getElementById("subMenu");

function toggleMenu(){
    subMenu.classList.toggle("open-menu");
}

var swiper = new Swiper(".tools-slider", {
    breakpoints: {
        0: {
            slidesPerView: 2,
        },
        768: {
            slidesPerView: 3,
        },
        991: {
            slidesPerView: 4,
        },
    },
    spaceBetween: 30,
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
});