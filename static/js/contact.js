document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('contactForm');
    const submitBtn = document.getElementById('submitBtn');
    const submitText = document.getElementById('submitText');
    const submitLoader = document.getElementById('submitLoader');
    
    // Form validation
    const inputs = form.querySelectorAll('input[required], textarea[required]');
    
    function validateForm() {
        let isValid = true;
        inputs.forEach(input => {
            if (!input.value.trim()) {
                isValid = false;
                input.style.borderColor = '#e53e3e';
            } else {
                input.style.borderColor = '#69c624';
            }
        });
        
        // Email validation
        const emailInput = document.getElementById('correo');
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(emailInput.value)) {
            isValid = false;
            emailInput.style.borderColor = '#e53e3e';
        }
        
        // Phone validation (basic)
        const phoneInput = document.getElementById('telefono');
        const phoneRegex = /^[\+]?[\d\s\-\(\)]{10,}$/;
        if (!phoneRegex.test(phoneInput.value)) {
            isValid = false;
            phoneInput.style.borderColor = '#e53e3e';
        }
        
        return isValid;
    }
    
    // Real-time validation
    inputs.forEach(input => {
        input.addEventListener('blur', validateForm);
        input.addEventListener('input', function() {
            if (this.value.trim()) {
                this.style.borderColor = '#69c624';
            }
        });
    });
    

form.addEventListener('submit', function(e) {
    if (!validateForm()) {
        return;
    }

    // Solo muestra el "spinner"
    submitBtn.disabled = true;
    submitText.style.display = 'none';
    submitLoader.style.display = 'inline';
});
    
    const phoneInput = document.getElementById('telefono');
    phoneInput.addEventListener('input', function(e) {
        let value = e.target.value.replace(/\D/g, '');
        if (value.length >= 10) {
            value = value.replace(/(\d{2})(\d{3})(\d{3})(\d{4})/, '+$1 $2 $3 $4');
        } else if (value.length >= 7) {
            value = value.replace(/(\d{3})(\d{3})(\d{1,4})/, '$1 $2 $3');
        } else if (value.length >= 4) {
            value = value.replace(/(\d{3})(\d{1,3})/, '$1 $2');
        }
        e.target.value = value;
    });
})