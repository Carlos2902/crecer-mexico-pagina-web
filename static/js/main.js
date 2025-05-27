// static/js/main.js
document.addEventListener('DOMContentLoaded', function () {
    const hamburgerButton = document.getElementById('hamburger-button');
    const mobileMenuOverlay = document.getElementById('mobile-menu-overlay');
    const closeMenuButton = document.getElementById('close-menu-button');

    if (hamburgerButton && mobileMenuOverlay) {
        hamburgerButton.addEventListener('click', function () {
            mobileMenuOverlay.classList.toggle('open');
            hamburgerButton.classList.toggle('open');
            // Controlar el aria-expanded
            const isExpanded = hamburgerButton.getAttribute('aria-expanded') === 'true' || false;
            hamburgerButton.setAttribute('aria-expanded', !isExpanded);
        });
    }

    if (closeMenuButton && mobileMenuOverlay) {
        closeMenuButton.addEventListener('click', function () {
            mobileMenuOverlay.classList.remove('open');
            hamburgerButton.classList.remove('open');
            hamburgerButton.setAttribute('aria-expanded', 'false');
        });
    }
});