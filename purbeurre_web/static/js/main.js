$(document).ready(function() {

    $(function() {
            $(".auto-complete").autocomplete({
                source: "/api/get_products/",
                select: function (event, ui) { //item selected
                  AutoCompleteSelectHandler(event, ui)
                },
                minLength: 2,
            });
        });

        function AutoCompleteSelectHandler(event, ui)
        {
            var selectedObj = ui.item;
        }

    // using jQuery
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $(".save-button").click(function() {
        var num = this.id;
        var product_code = $('#product_code_'+num).val();
        var product_sub_for = $('#product_sub_for_'+num).val();
        $.ajax({
            url: '/favorite/api/save_favorite/',
            type: 'POST',
            data: { product_code: product_code, product_sub_for: product_sub_for }
        });
        $(this).replaceWith("<span class='btn-sm btn-success'><i class='far fa-check-square'</i> Enregistré</span>");
    });

});