document.addEventListener("DOMContentLoaded", function () {
    const countdownElement = document.createElement("div");
    countdownElement.id = "countdown";
    document.body.appendChild(countdownElement);

    function startCountdown() {
        let countdownStart = localStorage.getItem("countdownStart");
        let remainingTime = 3600; // Время в секундах (1 час по умолчанию)

        if (countdownStart) {
            countdownStart = parseInt(countdownStart);
            const elapsedSeconds = Math.floor((Date.now() - countdownStart) / 1000);
            remainingTime -= elapsedSeconds;
        }

        function updateCountdown() {
            const minutes = Math.floor(remainingTime / 60);
            const seconds = remainingTime % 60;

            countdownElement.textContent = `Time remaining: ${minutes}m ${seconds}s`;

            if (remainingTime <= 0) {
                clearInterval(countdownInterval);
                countdownElement.textContent = "Time's up!";
            }
        }

        updateCountdown();

        const countdownInterval = setInterval(function () {
            remainingTime--;
            updateCountdown();
        }, 1000);
    }

    startCountdown();

    // Сохраняем начальное время в localStorage
    const countdownStart = Date.now();
    localStorage.setItem("countdownStart", countdownStart);
});