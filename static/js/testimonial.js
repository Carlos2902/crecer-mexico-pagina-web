// Función para animar la cita frase por frase
function animateQuoteText() {
    const quote = document.getElementById('quote-text');
    if (!quote) return;
    
    const text = quote.textContent;
    
    // Dividir el texto en frases (por puntos y comas)
    let phrases = text.split(/(?<=[.!?;])\s+/).filter(phrase => phrase.trim());
    
    // Si no hay puntuación, dividir por oraciones aproximadas
    if (phrases.length === 1) {
        const words = text.split(' ');
        const phrasesFromWords = [];
        const wordsPerPhrase = Math.ceil(words.length / 3); // Dividir en 3 partes aproximadamente
        
        for (let i = 0; i < words.length; i += wordsPerPhrase) {
            phrasesFromWords.push(words.slice(i, i + wordsPerPhrase).join(' '));
        }
        phrases = phrasesFromWords;
    }
    
    // Limpiar el contenido y crear spans para cada frase
    quote.innerHTML = '';
    phrases.forEach((phrase, index) => {
        const span = document.createElement('span');
        span.className = 'quote-phrase';
        span.textContent = phrase;
        if (index < phrases.length - 1) {
            span.textContent += ' ';
        }
        quote.appendChild(span);
    });
    
    // Animar cada frase con delay
    const phraseElements = quote.querySelectorAll('.quote-phrase');
    phraseElements.forEach((phrase, index) => {
        setTimeout(() => {
            phrase.classList.add('animate');
        }, index * 400 + 200); // 400ms de delay entre frases
    });
}

// Configuración del Intersection Observer
const observerOptions = {
    threshold: 0.2,
    rootMargin: '0px 0px -50px 0px'
};

// Intersection Observer para detectar cuando los elementos entran en vista
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            // Animar imagen principal
            if (entry.target.classList.contains('main-image')) {
                setTimeout(() => {
                    entry.target.classList.add('animate');
                }, 100);
            }
            
            // Animar comilla y después el texto
            if (entry.target.classList.contains('quote-mark')) {
                setTimeout(() => {
                    entry.target.classList.add('animate');
                    // Iniciar animación de texto después de la comilla
                    setTimeout(animateQuoteText, 300);
                }, 400);
            }
            
            // Animar información del autor
            if (entry.target.classList.contains('testimonial-author')) {
                setTimeout(() => {
                    entry.target.classList.add('animate');
                }, 1200); // Después de que termine la animación del texto
            }
            
            // Dejar de observar una vez que se anima
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

// Inicializar las animaciones cuando el DOM esté listo
function initTestimonialAnimations() {
    const mainImage = document.querySelector('.main-image');
    const quoteMark = document.querySelector('.quote-mark');
    const author = document.querySelector('.testimonial-author');
    
    // Observar elementos para animación
    if (mainImage) observer.observe(mainImage);
    if (quoteMark) observer.observe(quoteMark);
    if (author) observer.observe(author);
}

// Ejecutar cuando el DOM esté cargado
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initTestimonialAnimations);
} else {
    initTestimonialAnimations();
}