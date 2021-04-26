$(document).ready(function () {
    "use strict";

    /* Enable toast messages */
    $('.toast').toast('show');
    setTimeout(function () {
        $(".toast").toast("dispose");
    }, 8000);

    /* Toggle cart-preview */
    $("#cart-dropdown").click(function () {
        displayCart();
    });

    function displayCart() {
        $("#cart-preview").fadeToggle(200);
    }

    $('#close-btn').on('click', function(){
    $('#cart-dropdown').trigger('click');
    });
  
});

const starRate = document.querySelectorAll('.rate-stars');


    starRate.forEach(rating => {
        const ratingValue = parseInt(rating.getAttribute('data-bs-value'));
        const fullStar = ratingValue;
        const emptyStar = 5 - fullStar;
        let stars = '';

        for (let i = 1; i < 6; i++) {
            if (i <= fullStar) {
                stars += `<i class="fas fa-star"></i>`;
            }
            else {
                stars += `<i class="far fa-star"></i>`;
            }
        }
        rating.innerHTML = stars;
    });
