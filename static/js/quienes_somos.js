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


// Carrusel de Equipo por Batches
const equipoContainer = document.querySelector('#seccion-equipo .contenedor-equipo');
const gridEquipo = document.querySelector('.grid-equipo');
const prevButton = document.querySelector('#seccion-equipo .prev');
const nextButton = document.querySelector('#seccion-equipo .next');

// Salir si no se encuentran los elementos necesarios
if (!gridEquipo || !prevButton || !nextButton) {
    console.warn('Elementos del carrusel de equipo no encontrados.');
} else {
    initCarousel();
}

function initCarousel() {
    const tarjetas = gridEquipo.querySelectorAll('.tarjeta-miembro');
    
    if (tarjetas.length <= 1) {
        prevButton.style.display = 'none';
        nextButton.style.display = 'none';
        return;
    }

    let currentBatch = 0;
    let autoScrollInterval;
    const SCROLL_INTERVAL = 5000; // 5 segundos
    let isTransitioning = false;

    // Función para obtener el número de tarjetas visibles según el tamaño de pantalla
    const getVisibleCards = () => {
        const windowWidth = window.innerWidth;
        if (windowWidth >= 1024) return 4; // Desktop: 4 tarjetas
        if (windowWidth >= 768) return 2;  // Tablet: 2 tarjetas
        return 1; // Móvil: 1 tarjeta
    };

    // Función para calcular el número total de batches
    const getTotalBatches = () => {
        const visibleCards = getVisibleCards();
        return Math.ceil(tarjetas.length / visibleCards);
    };

    // Función para deslizar a un batch específico
    const scrollToBatch = (batchIndex) => {
        if (isTransitioning) return;
        
        isTransitioning = true;
        const visibleCards = getVisibleCards();
        const totalBatches = getTotalBatches();
        
        // Normalizar el índice del batch
        if (batchIndex < 0) {
            batchIndex = totalBatches - 1;
        } else if (batchIndex >= totalBatches) {
            batchIndex = 0;
        }
        
        currentBatch = batchIndex;
        
        // Calcular la posición de scroll
        const startCardIndex = currentBatch * visibleCards;
        const targetCard = tarjetas[startCardIndex];
        
        if (targetCard) {
            // Calcular el scroll left para centrar el batch
            let scrollLeft;
            
            if (window.innerWidth >= 768) {
                // Para tablet y desktop, alinear al inicio del contenedor
                scrollLeft = targetCard.offsetLeft - gridEquipo.offsetLeft;
            } else {
                // Para móvil, centrar la tarjeta
                scrollLeft = targetCard.offsetLeft - (gridEquipo.offsetWidth - targetCard.offsetWidth) / 2;
            }
            
            gridEquipo.scrollTo({
                left: scrollLeft,
                behavior: 'smooth'
            });
        }
        
        // Actualizar indicadores si existen
        updateIndicators();
        
        // Resetear la bandera después de la animación
        setTimeout(() => {
            isTransitioning = false;
        }, 600);
    };

    // Función para crear indicadores de paginación
    const createIndicators = () => {
        const totalBatches = getTotalBatches();
        if (totalBatches <= 1) return; // No mostrar indicadores si solo hay un batch
        
        // Buscar contenedor existente o crear uno nuevo
        let indicatorsContainer = equipoContainer.querySelector('.carousel-indicators');
        if (!indicatorsContainer) {
            indicatorsContainer = document.createElement('div');
            indicatorsContainer.className = 'carousel-indicators';
            equipoContainer.appendChild(indicatorsContainer);
        }
        
        // Limpiar indicadores existentes
        indicatorsContainer.innerHTML = '';
        
        // Crear indicadores
        for (let i = 0; i < totalBatches; i++) {
            const indicator = document.createElement('button');
            indicator.className = 'carousel-indicator';
            indicator.setAttribute('aria-label', `Ir al grupo ${i + 1}`);
            if (i === currentBatch) {
                indicator.classList.add('active');
            }
            
            indicator.addEventListener('click', () => {
                scrollToBatch(i);
                resetAutoScroll();
            });
            
            indicatorsContainer.appendChild(indicator);
        }
    };

    // Función para actualizar los indicadores
    const updateIndicators = () => {
        const indicators = equipoContainer.querySelectorAll('.carousel-indicator');
        indicators.forEach((indicator, index) => {
            indicator.classList.toggle('active', index === currentBatch);
        });
    };

    // Función para actualizar el estado del carrusel cuando cambia el tamaño de pantalla
    const handleResize = () => {
        const totalBatches = getTotalBatches();
        
        // Ajustar currentBatch si es necesario
        if (currentBatch >= totalBatches) {
            currentBatch = totalBatches - 1;
        }
        
        // Recrear indicadores
        createIndicators();
        
        // Ir al batch actual (recalculado)
        setTimeout(() => {
            scrollToBatch(currentBatch);
        }, 100);
    };

    // Auto-scroll
    const startAutoScroll = () => {
        clearInterval(autoScrollInterval);
        autoScrollInterval = setInterval(() => {
            const totalBatches = getTotalBatches();
            const nextBatch = (currentBatch + 1) % totalBatches;
            scrollToBatch(nextBatch);
        }, SCROLL_INTERVAL);
    };

    const resetAutoScroll = () => {
        clearInterval(autoScrollInterval);
        startAutoScroll();
    };

    // Event listeners para los botones
    nextButton.addEventListener('click', (e) => {
        e.preventDefault();
        scrollToBatch(currentBatch + 1);
        resetAutoScroll();
    });

    prevButton.addEventListener('click', (e) => {
        e.preventDefault();
        scrollToBatch(currentBatch - 1);
        resetAutoScroll();
    });

    // Pausar auto-scroll en hover
    if (equipoContainer) {
        equipoContainer.addEventListener('mouseenter', () => {
            clearInterval(autoScrollInterval);
        });
        
        equipoContainer.addEventListener('mouseleave', () => {
            startAutoScroll();
        });
    }

    // Manejar cambios de tamaño de pantalla
    let resizeTimeout;
    window.addEventListener('resize', () => {
        clearTimeout(resizeTimeout);
        resizeTimeout = setTimeout(handleResize, 250);
    });

    // Sincronización con scroll manual (para dispositivos táctiles)
    let scrollTimeout;
    const handleManualScroll = () => {
        if (isTransitioning) return;
        
        const containerScrollLeft = gridEquipo.scrollLeft;
        const visibleCards = getVisibleCards();
        const cardWidth = tarjetas[0].offsetWidth;
        const gap = parseFloat(getComputedStyle(gridEquipo).gap) || 0;
        
        // Calcular qué batch debería estar visible
        const estimatedBatch = Math.round(containerScrollLeft / ((cardWidth + gap) * visibleCards));
        const totalBatches = getTotalBatches();
        const newBatch = Math.max(0, Math.min(estimatedBatch, totalBatches - 1));
        
        if (newBatch !== currentBatch) {
            currentBatch = newBatch;
            updateIndicators();
            resetAutoScroll();
        }
    };

    gridEquipo.addEventListener('scroll', () => {
        clearTimeout(scrollTimeout);
        scrollTimeout = setTimeout(handleManualScroll, 150);
    });

    // Inicialización
    createIndicators();
    startAutoScroll();
    
    // Keyboard navigation
    equipoContainer.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowLeft') {
            e.preventDefault();
            scrollToBatch(currentBatch - 1);
            resetAutoScroll();
        } else if (e.key === 'ArrowRight') {
            e.preventDefault();
            scrollToBatch(currentBatch + 1);
            resetAutoScroll();
        }
    });
}
});