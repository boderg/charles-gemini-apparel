
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();

var style = {
    base: {
        color: '#555555',
        fontFamily: '"Cuprum", sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#999999',
        }
    },
    invalid: {
        color: '#c83232',
        iconColor: '#c83232',
    }
};

var card = elements.create('card',{style: style});

card.mount('#card-element');

card.addEventListener('change', function (event) {
    var displayError = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" style="color: var(--error-colour);">
                <i class="fas fa-times"></i>
            </span>
            <span class="error" style="color: var(--error-colour);">
                ${event.error.message}
            </span>`
        $(displayError).html(html);
    } else {
        displayError.textContent = '';
    }
});

var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    $('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {
        if (result.error) {
            var displayError = document.getElementById('card-errors');
            var html = `
                <span class="icon" style="color: var(--error-colour);">
                    <i class="fas fa-times"></i>
                </span>
                <span class="error" style="color: var(--error-colour);">
                    ${result.error.message}
                </span>`;
            $(displayError).html(html);
            $('#payment-form').fadeToggle(100);
            $('#loading-overlay').fadeToggle(100);
            card.update({ 'disabled': false});
            $('#submit-button').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});