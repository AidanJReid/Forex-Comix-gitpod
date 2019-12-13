// Initialize materialize elements

function materializeInit() {
            $('.sidenav').sidenav();
            $('.parallax').parallax();
            $('.dropdown-trigger').dropdown();
            $('.collapsible').collapsible();
            $('#modal1').modal();
}
materializeInit();

// Initialize custom elements

$(document).ready(function() {
            $('select').formSelect();
            $("#modbtn").click(function() { 
                $('.toast').toast('show'); 
            }); 
        })

function flashMessage() {
    $("#flash_message").addClass("show");
    setTimeout(function () {
        $("#flash_message").removeClass("show");
    }, 3000);
}
flashMessage();
