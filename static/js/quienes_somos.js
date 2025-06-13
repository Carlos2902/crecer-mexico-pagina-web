document.addEventListener('DOMContentLoaded', function() {
    // Script para procesar el título con asteriscos (palabras destacadas)
    const tituloOds = document.getElementById('titulo-ods-configurable');
    if (tituloOds) {
        let contenido = tituloOds.innerHTML;
        // Reemplazar *palabra* con <span class="destacado">palabra</span>
        contenido = contenido.replace(/\*(.*?)\*/g, '<span class="destacado">$1</span>');
        tituloOds.innerHTML = contenido;
    }


    // Función para activar las animaciones de las imágenes
function animarImagenesCollage() {
    const imagenes = document.querySelectorAll('.imagen-collage');
    
    // Usar Intersection Observer para activar las animaciones cuando las imágenes entren en el viewport
    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                // Una vez que la animación se activa, ya no necesitamos observar este elemento
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1, // Activar cuando el 10% del elemento sea visible
        rootMargin: '0px 0px -50px 0px' // Activar un poco antes de que sea completamente visible
    });
    
    // Observar todas las imágenes del collage
    imagenes.forEach((imagen) => {
        observer.observe(imagen);
    });
}

// Función alternativa para activar las animaciones inmediatamente al cargar la página
function animarImagenesInmediato() {
    const imagenes = document.querySelectorAll('.imagen-collage');
    
    imagenes.forEach((imagen, index) => {
        setTimeout(() => {
            imagen.classList.add('visible');
        }, index * 100); // Retraso escalonado de 100ms entre cada imagen
    });
}

    animarImagenesCollage();
    
// Si usas navegación SPA (Single Page Application), también puedes llamar la función cuando cambies de página
function inicializarAnimacionesMision() {
    // Resetear las clases visible antes de animar
    const imagenes = document.querySelectorAll('.imagen-collage');
    imagenes.forEach(imagen => {
        imagen.classList.remove('visible');
    });
    
    // Activar las animaciones después de un pequeño retraso
    setTimeout(() => {
        animarImagenesCollage();
    }, 100);
}
});