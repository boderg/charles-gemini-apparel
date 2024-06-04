let countrySelected = $('#id_default_country').val();
        if (!countrySelected) {
            $('#id_default_county').css('color', 'var(--secondary-colour-translucent)');
        }
        $('#id_default_country').change(function() {
            countrySelected = $(this).val();
            if (!countrySelected) {
                $(this).css('color', 'var(--secondary-colour-translucent)');
            } else {
                $(this).css('color', 'var(--secondary-colour)');
            }
        });