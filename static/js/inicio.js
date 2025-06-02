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
});
