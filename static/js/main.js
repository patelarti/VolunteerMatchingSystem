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

    fetch('/login', {
        method: 'POST',
        headers: {
            'Accept':'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email, password })
    })
    .then(response => response.json())
    .then(data => {
        if (data.message === 'Login successful') {
            window.location.href = '/base'; // Assuming /base is the correct URL for the base page
        } else {
            alert('Invalid email or password');
        }
    })
    .catch(error => console.error('Error:', error));
});


document.getElementById('reset-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const urlParams = new URLSearchParams(window.location.search);
    const email = urlParams.get('email');
    const newPassword = document.getElementById('new-password').value;
    const confirmNewPassword = document.getElementById('confirm-new-password').value;

    fetch('/reset', {
        method: 'POST',
        headers: {
            'Accept':'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email, newPassword, confirmNewPassword })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        if (data.message === 'Password reset successfully') {
            window.location.href = '/login';
        }
    })
    .catch(error => console.error('Error:', error));
});

// Handle Profile Update
document.getElementById('profile-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const email = document.getElementById('email').value;
    const fullName = document.getElementById('full-name').value;
    const dob = document.getElementById('dob').value;
    const address1 = document.getElementById('address1').value;
    const address2 = document.getElementById('address2').value;
    const city = document.getElementById('city').value;
    const state = document.getElementById('state').value;
    const zip = document.getElementById('zip').value;
    const skills = Array.from(document.getElementById('skills').selectedOptions).map(option => option.value);
    const preferences = document.getElementById('preferences').value;
    const availability = document.getElementById('availability').value;

    fetch('/api/updateProfile', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email, fullName, dob, address1, address2, city, state, zip, skills, preferences, availability })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        if (data.message === 'Profile updated successfully') {
            // Optionally, redirect or update the UI
        }
    })
    .catch(error => console.error('Error:', error));
});


// Toggle Dark Mode
//const themeSwitch = document.getElementById('theme-switch');
//const themeLabel = document.getElementById('theme-label');
//
//themeSwitch.addEventListener('change', () => {
//    document.body.classList.toggle('dark-mode');
//    themeLabel.textContent = themeSwitch.checked ? 'Light Mode' : 'Dark Mode';
//});