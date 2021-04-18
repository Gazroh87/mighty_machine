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