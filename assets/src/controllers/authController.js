const users = [
    { email: 'rahmaaloui3199@gmail.com', password: '1234' }
];

const registerUser = (req, res) => {
    const { email, password, confirmPassword } = req.body;

    // Basic validation
    if (!email || !password || !confirmPassword) {
        return res.status(400).json({ message: 'All fields are required' });
    }

    if (password !== confirmPassword) {
        return res.status(400).json({ message: 'Passwords do not match' });
    }

    // Check if user already exists
    const userExists = users.find(user => user.email === email);
    if (userExists) {
        return res.status(400).json({ message: 'User already exists' });
    }

    // Add new user
    users.push({ email, password });
    res.status(201).json({ message: 'User registered successfully' });
};

const forgotPassword = (req, res) => {
    const { email } = req.body;

    // Basic validation
    if (!email) {
        return res.status(400).json({ message: 'Email is required' });
    }

    // Check if user exists
    const user = users.find(user => user.email === email);
    if (!user) {
        return res.status(400).json({ message: 'User not found' });
    }

    // Simulate sending reset password email
    res.status(200).json({ message: 'Password reset link sent to email' });
};

module.exports = { loginUser, registerUser, forgotPassword };
