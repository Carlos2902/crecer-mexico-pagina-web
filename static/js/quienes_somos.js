document.addEventListener('DOMContentLoaded', function() {
    // Script para procesar el título con asteriscos (palabras destacadas)
    const tituloOds = document.getElementById('titulo-ods-configurable');
    if (tituloOds) {
        let contenido = tituloOds.innerHTML;
        // Reemplazar *palabra* con <span class="destacado">palabra</span>
        contenido = contenido.replace(/\*(.*?)\*/g, '<span class="destacado">$1</span>');
        tituloOds.innerHTML = contenido;
    }
});