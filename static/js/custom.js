document.addEventListener('DOMContentLoaded', function() {
    // Toggle the visibility of the profile dropdown menu
    const userMenuButton = document.getElementById('user-menu-button');
    const userMenu = document.getElementById('user-menu');

    if (userMenuButton && userMenu) {
        userMenuButton.addEventListener('click', function() {
            userMenu.classList.toggle('hidden');
        });
    }

    // Toggle the visibility of the password input
    function togglePasswordVisibility(passwordFieldClass) {
        const passwordInput = document.querySelector(`.${passwordFieldClass}`);
        const passwordEyeIcon = document.querySelector(`#${passwordFieldClass}-eye-icon`);
        
        if (passwordInput && passwordEyeIcon) {
            if (passwordInput.type === 'password') {
                passwordInput.type = 'text';
                passwordEyeIcon.textContent = 'visibility_off';
            } else {
                passwordInput.type = 'password';
                passwordEyeIcon.textContent = 'visibility';
            }
        } else {
            console.warn(`Element with class ${passwordFieldClass} or ID ${passwordFieldClass}-eye-icon not found.`);
        }
    }

    // Sprawdź, czy na stronie znajdują się elementy z klasą .password-input
    const passwordInputs = document.querySelectorAll('.password-input');
    if (passwordInputs.length > 0) {
        passwordInputs.forEach(function(passwordInput) {
            passwordInput.addEventListener('input', function() {
                passwordInput.classList.add('ring-2', 'ring-indigo-500');
            });
        });

        // Ustawienie funkcji togglePasswordVisibility jako globalnie dostępnej
        window.togglePasswordVisibility = togglePasswordVisibility;
    } 
});
