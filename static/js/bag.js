function increaseQuantity(itemId) {
    var input = document.getElementById('quantity-' + itemId);
    input.value = parseInt(input.value) + 1;
}

function decreaseQuantity(itemId) {
    var input = document.getElementById('quantity-' + itemId);
    if (input.value > 1) {
        input.value = parseInt(input.value) - 1;
    }
}