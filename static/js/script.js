// Initialize materialize elements

function materializeInit() {
            $('.sidenav').sidenav();
            $('.parallax').parallax();
            $('.dropdown-trigger').dropdown();
            $('.collapsible').collapsible();
            $('#modal1').modal();
}
materializeInit();

// CUSTOM ELEMENTS

// Modal for event in Learner section

$(document).ready(function() {
            $('select').formSelect();
            $("#modbtn").click(function() { 
                $('.toast').toast('show'); 
            }); 
        })

// Flash message for no filter applied (Database page)

function flashMessage() {
    $("#flash_message").addClass("show");
    setTimeout(function () {
        $("#flash_message").removeClass("show");
    }, 3000);
}
flashMessage();
