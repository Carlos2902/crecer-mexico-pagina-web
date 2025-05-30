// para las letras verdes en el título del héroe
document.addEventListener('DOMContentLoaded', function() {

    const heroTitle = document.querySelector('.hero-content h1');
    if (heroTitle) {
            let titleText = heroTitle.innerHTML;
            
            // Palabras que deben ir en verde según tu screenshot
            const wordsToHighlight = ['IAP', 'Institución', 'Trabaja', 'Derecho', 'Educación'];
            
            wordsToHighlight.forEach(word => {
                const regex = new RegExp(`\\b${word}\\b`, 'gi');
                titleText = titleText.replace(regex, `<span class="highlight">${word}</span>`);
            });
            
            heroTitle.innerHTML = titleText;
    }
    
});