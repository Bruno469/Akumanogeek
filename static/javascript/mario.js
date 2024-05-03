document.addEventListener('DOMContentLoaded', function() {
    console.log("DOMContentLoaded event fired");

    const mario = document.querySelector('.mario');

    // Adiciona a classe 'mario-run' para iniciar a animação de corrida
    mario.classList.add('mario-run');

    document.addEventListener('keydown', function(event) {
        if (event.code === 'Space') {
            console.log("It's working");
            const marioRect = mario.getBoundingClientRect(); 
            const initialLeft = marioRect.left; 
            mario.style.left = initialLeft + 'px';
            mario.classList.remove('mario'); // Remove a classe 'mario' para que ele pule
            mario.classList.add('jump'); // Adiciona a classe 'jump' para iniciar a animação de pulo
            setTimeout(function() {
                mario.classList.remove('jump'); // Remove a classe 'jump' para encerrar a animação de pulo
                mario.style.left = initialLeft + 'px';
                mario.classList.add('mario'); // Adiciona a classe 'mario' de volta após o pulo
            }, 500); // Tempo da animação de pulo
        }
    });
});
