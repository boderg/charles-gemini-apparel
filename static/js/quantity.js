    // Script for increasing and decreasing quantity in the garment page
    // when the plus and minus buttons are clicked

    // Increase the quantity

    $(document).ready(function() {
        $('.increase-qty').click(function (e) {
            e.preventDefault();
            var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
            var currentValue = parseInt($(closestInput).val());
            if (currentValue != 99) { 
                $(closestInput).val(currentValue + 1);
            }
            if (currentValue +1 == 99) {
                $(this).addClass('no-hover');
            } else {
                $('.decrease-qty').removeClass('no-hover');
            }
        });

        // Decrease the quantity

        $('.decrease-qty').click(function (e) {
            e.preventDefault();
            var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
            var currentValue = parseInt($(closestInput).val());
            if (currentValue > 1) {
                $(closestInput).val(currentValue - 1);
            }
            if (currentValue -1 == 1) {
                $(this).addClass('no-hover');
            } else {
                $('.increase-qty').removeClass('no-hover');
            }
        });

        // Check when the input is changed 

        $('.qty_input').change(function() {
            var currentValue = parseInt($(this).val());
            if (currentValue >= 99) {
                $('.increase-qty').addClass('no-hover');
            } else {
                $('.increase-qty').removeClass('no-hover');
            }
            if (currentValue <= 1) {
                $('.decrease-qty').addClass('no-hover');
            } else {
                $('.decrease-qty').removeClass('no-hover');
            }
        });

        // Check when the page loads and when the quantity changes
        // to check if the plus and minus buttons should be disabled

        function checkQuantity() {
            $('.qty_input').each(function() {
                var currentValue = parseInt($(this).val());
                if (currentValue >= 99) {
                    $(this).closest('.input-group').find('.increase-qty').addClass('no-hover');
                } else {
                    $(this).closest('.input-group').find('.increase-qty').removeClass('no-hover');
                }
                if (currentValue <= 1) {
                    $(this).closest('.input-group').find('.decrease-qty').addClass('no-hover');
                } else {
                    $(this).closest('.input-group').find('.decrease-qty').removeClass('no-hover');
                }
            });
        }
    
        // Call the function on page load
        checkQuantity();
    
        // Call the function when the quantity changes
        $('.qty_input').change(checkQuantity);
    });