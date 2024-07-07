// Show/Hide Password
const showHiddenPass = (inputPass, inputIcon) => {
    const input = document.getElementById(inputPass),
          iconEye = document.getElementById(inputIcon);
          
    iconEye.addEventListener('click', () => {
        if (input.type === 'password') {
            input.type = 'text';
            iconEye.classList.add('ri-eye-line');
            iconEye.classList.remove('ri-eye-off-line');
        } else {
            input.type = 'password';
            iconEye.classList.remove('ri-eye-line');
            iconEye.classList.add('ri-eye-off-line');
        }
    });
};

showHiddenPass('input-pass', 'input-icon');

// Handle Login
document.getElementById('login-form').addEventListener('submit', async function(event) {
    event.preventDefault(); // Prevent the default form submission
    const email = document.getElementById('input-email').value;
    const password = document.getElementById('input-pass').value;

    try {
        const response = await fetch('/api/auth/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email, password })
        });

        const data = await response.json();
        if (response.ok) {
            localStorage.setItem('token', data.token);
            window.location.href = 'base.html';
        } else {
            alert(data.message);
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred. Please try again.');
    }
});

// Toggle Dark Mode
const themeSwitch = document.getElementById('theme-switch');
const themeLabel = document.getElementById('theme-label');

themeSwitch.addEventListener('change', () => {
    document.body.classList.toggle('dark-mode');
    themeLabel.textContent = themeSwitch.checked ? 'Light Mode' : 'Dark Mode';
});
