(function () {
    "use strict";

    /* Toggle cart-preview */
    $("#cart-dropdown").click(function () {
        displayCart();
    });

    function displayCart() {
        $("#cart-preview").fadeToggle(200);
    }
})();