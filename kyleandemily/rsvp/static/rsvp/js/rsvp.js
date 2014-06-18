$(document).ready(function() {
    var $lookup_form = $("form#lookup"),
        $first_name = $("#firstname"),
        $last_name = $("#lastname"),
        $container = $("#container");

    $first_name.focus();

    $lookup_form.submit(function (event) {
        event.preventDefault();
        $.ajax({
            url: 'lookup/',
            cache: false,
            data: {
                'first_name': $first_name.val(),
                'last_name': $last_name.val()
            },
            success: function (data, status, jqXHR) {
                $lookup_form.unbind().submit();
                $lookup_form.submit();

            },
            error: function (jqXHR, status) {
                var $error = $('<p>Sorry, we could not find your invitation</p>');
                if($('div#error_msg').is(':empty')) {
                    $($error).appendTo('#error_msg');
                }
            }
        });
    });
});