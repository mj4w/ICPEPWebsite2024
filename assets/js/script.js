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


// swiper js
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

// view-more
let loadMoreBtn = document.querySelector('#view-more');
let currentItem = 3;

loadMoreBtn.onclick = () =>{
    let boxes = [...document.querySelectorAll('.events .container .event-list .card')];
    for (var i = currentItem; i < currentItem + 3; i++){
        boxes[i].style.display = 'inline-block';
    }
    currentItem += 3;

    if(currentItem >= boxes.length){
        loadMoreBtn.style.display = 'none';
    }
}