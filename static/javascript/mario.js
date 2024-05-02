document.addEventListener('DOMContentLoaded', function() {
    const mario = document.querySelector('.mario');

    document.addEventListener('keydown', function(event) {
        if (event.code === 'Space') {
            mario.classList.add('jump');
            setTimeout(function() {
                mario.classList.remove('jump');
            }, 500); // Tempo da animação de pulo
        }
    });
});
