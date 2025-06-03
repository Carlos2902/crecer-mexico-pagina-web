// Para las letras verdes en el título del héroe
document.addEventListener('DOMContentLoaded', function () {
    const heroTitles = document.querySelectorAll('.hero-content h1, .hero-content-left h1');
    
    const wordsToHighlight = ['IAP', 'Institución', 'Trabaja', 'Derecho', 'Educación'];

    heroTitles.forEach(heroTitle => {
        let titleText = heroTitle.innerHTML;

        wordsToHighlight.forEach(word => {
            const regex = new RegExp(`\\b${word}\\b`, 'gi');
            titleText = titleText.replace(regex, `<span class="highlight">${word}</span>`);
        });

        heroTitle.innerHTML = titleText;
    });

    // Inicializar carrusel de programas
    initProgramsCarousel();
});

// Función para inicializar el carrusel de programas
function initProgramsCarousel() {
    const carousel = document.querySelector('.programs-grid');
    const cards = document.querySelectorAll('.program-card');
    const prevBtn = document.querySelector('.carousel-nav.prev');
    const nextBtn = document.querySelector('.carousel-nav.next');
    const indicators = document.querySelectorAll('.carousel-indicator');
    
    // Verificar que existan elementos antes de continuar
    if (!carousel || cards.length === 0) return;
    
    let currentIndex = 0;
    const totalCards = cards.length;
    let autoPlayInterval = null;
    const autoPlayDelay = 4000; // 4 segundos
    
    // Variables para touch events
    let startX = 0;
    let startY = 0;
    
    // Función para actualizar el carrusel
    function updateCarousel() {
        cards.forEach((card, index) => {
            card.classList.toggle('active', index === currentIndex);
        });
        
        indicators.forEach((indicator, index) => {
            indicator.classList.toggle('active', index === currentIndex);
        });
    }
    
    // Navegación
    function goToNext() {
        currentIndex = (currentIndex + 1) % totalCards;
        updateCarousel();
    }
    
    function goToPrevious() {
        currentIndex = (currentIndex - 1 + totalCards) % totalCards;
        updateCarousel();
    }
    
    function goToSlide(index) {
        if (index >= 0 && index < totalCards) {
            currentIndex = index;
            updateCarousel();
        }
    }
    
    // Control de autoplay
    function startAutoPlay() {
        pauseAutoPlay();
        if (totalCards > 1) {
            autoPlayInterval = setInterval(goToNext, autoPlayDelay);
        }
    }
    
    function pauseAutoPlay() {
        if (autoPlayInterval) {
            clearInterval(autoPlayInterval);
            autoPlayInterval = null;
        }
    }
    
    // Verificar si el carrusel está visible
    function isCarouselVisible() {
        const rect = carousel.getBoundingClientRect();
        return rect.top < window.innerHeight && rect.bottom > 0;
    }
    
    // Event listeners para botones de navegación
    if (prevBtn) {
        prevBtn.addEventListener('click', (e) => {
            e.preventDefault();
            pauseAutoPlay();
            goToPrevious();
            startAutoPlay();
        });
    }
    
    if (nextBtn) {
        nextBtn.addEventListener('click', (e) => {
            e.preventDefault();
            pauseAutoPlay();
            goToNext();
            startAutoPlay();
        });
    }
    
    // Event listeners para indicadores
    indicators.forEach((indicator, index) => {
        indicator.addEventListener('click', (e) => {
            e.preventDefault();
            pauseAutoPlay();
            goToSlide(index);
            startAutoPlay();
        });
    });
    
    // Navegación con teclado
    document.addEventListener('keydown', (e) => {
        if (!isCarouselVisible()) return;
        
        if (e.key === 'ArrowLeft') {
            pauseAutoPlay();
            goToPrevious();
            startAutoPlay();
        } else if (e.key === 'ArrowRight') {
            pauseAutoPlay();
            goToNext();
            startAutoPlay();
        }
    });
    
    // Touch events para móviles
    carousel.addEventListener('touchstart', (e) => {
        startX = e.touches[0].clientX;
        startY = e.touches[0].clientY;
        pauseAutoPlay();
    }, { passive: true });
    
    carousel.addEventListener('touchmove', (e) => {
        const currentX = e.touches[0].clientX;
        const currentY = e.touches[0].clientY;
        const deltaX = Math.abs(currentX - startX);
        const deltaY = Math.abs(currentY - startY);
        
        // Prevenir scroll vertical durante swipe horizontal
        if (deltaX > deltaY && deltaX > 10) {
            e.preventDefault();
        }
    }, { passive: false });
    
    carousel.addEventListener('touchend', (e) => {
        const endX = e.changedTouches[0].clientX;
        const endY = e.changedTouches[0].clientY;
        
        const deltaX = startX - endX;
        const deltaY = startY - endY;
        
        // Procesar swipe horizontal
        if (Math.abs(deltaX) > Math.abs(deltaY) && Math.abs(deltaX) > 50) {
            if (deltaX > 0) {
                goToNext(); // Swipe left -> siguiente
            } else {
                goToPrevious(); // Swipe right -> anterior
            }
        }
        
        // Reanudar autoplay después de un delay
        setTimeout(startAutoPlay, 500);
    }, { passive: true });
    
    // Pausar/reanudar autoplay con hover
    carousel.addEventListener('mouseenter', pauseAutoPlay);
    carousel.addEventListener('mouseleave', startAutoPlay);
    
    // Iniciar autoplay
    startAutoPlay();
    
    // Retornar objeto con métodos públicos si necesitas control externo
    window.programsCarousel = {
        next: goToNext,
        previous: goToPrevious,
        goTo: goToSlide,
        pause: pauseAutoPlay,
        play: startAutoPlay
    };
}