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
document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission
    const email = document.getElementById('input-email').value;
    const password = document.getElementById('input-pass').value;

    fetch('http://localhost:5000/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email, password })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            window.location.href = 'base.html';
        } else {
            alert('Invalid email or password');
        }
    })
    .catch(error => console.error('Error:', error));
});

// Toggle Dark Mode
const themeSwitch = document.getElementById('theme-switch');
const themeLabel = document.getElementById('theme-label');

themeSwitch.addEventListener('change', () => {
    document.body.classList.toggle('dark-mode');
    themeLabel.textContent = themeSwitch.checked ? 'Light Mode' : 'Dark Mode';
});
