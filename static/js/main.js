$(document).ready(function() {

    // Initialize AOS, AOS does not seem to work with Safari, maybe Jquery is the issue
    AOS.init();
    console.log('AOS ', AOS)

    $('#solutions').click(function() {

        // apply dropdown slide effect
        $('#dropdown').slideToggle(300);

        // rotate chevron icon
        $('#chevron-down').addClass('rotate');

        // If we click anywhere on the page except the solutions and dropdown, close the dropdown
        $(document).click(function(e) {
            if (!$(e.target).closest('#solutions').length && !$(e.target).closest('#dropdown').length) {
                $('#dropdown').slideUp(300);
                $('#chevron-down').removeClass('rotate');
            }
        });
    });

    // close mobile menu for smaller screens
    $('#close-mobile-menu').click(function() {
        $('#mobile-menu').fadeOut(300, "linear");
    });

    // open mobile menu for smaller screens
    $('#open-mobile-menu').click(function() {
        $('#mobile-menu').fadeIn(300, "linear");
    });

    // If we click anywhere on the page except the mobile menu, close the mobile menu
    $(document).click(function(e) {
        if (!$(e.target).closest('#mobile-menu').length && !$(e.target).closest('#open-mobile-menu').length) {
            $('#mobile-menu').fadeOut(300, "linear");
        }
    });
});
