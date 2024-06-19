// countdown timer

var countdown = document.getElementById('countdown');
var seconds = 10;

var intervalId = setInterval(function() {
    seconds--;
    countdown.innerHTML = seconds;
    if (seconds <= 0) clearInterval(intervalId);
    }, 1000);

    setTimeout(function() {
        window.location.href = redirect.dataset.url;
    }, 10000);