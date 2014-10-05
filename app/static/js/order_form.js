$(function() {
    'use strict';

    // Make sure we're in order form page.
    if (!$("#js_order_form").length) return;

    // Calculate total price
    $('#div_id_ingredients input[type=checkbox]').on('change', function(e) {
        var ingredient_label = $(e.target).parents('label').text().toString();
        var ingredient_price = parseInt(ingredient_label.match(/^.*\((\d+)\$\)/)[1]);
        var total_price = parseInt($('#id_total_price').val());
        console.log(total_price, ingredient_price)
        if ($(e.target).is(':checked')) {
            $('#id_total_price').val(total_price + ingredient_price);
        } else {
            $('#id_total_price').val(total_price - ingredient_price);
        }
    });
});