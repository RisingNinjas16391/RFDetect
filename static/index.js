var log = document.getElementById("log");

            setInterval(() => {
                fetch('logpage')
                .then(response => {
                        response.text().then(t => {log.innerHTML = t})
                    });
                }, 1000);

$(function() {
    $('a#center').on('click', function(e) {
        e.preventDefault();
        fetch('/centeragitator');
        return false;
    });
});
