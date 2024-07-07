const express = require('express');
const router = express.Router();
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const testUsers = require('../testData');

// Login route
router.post('/login', (req, res) => {
    const { email, password } = req.body;

    if (!email || !password) {
        return res.status(400).json({ message: 'Email and password are required' });
    }

    const user = testUsers.find(user => user.email === email);
    if (!user) {
        return res.status(401).json({ message: 'Invalid email or password' });
    }

    if (!bcrypt.compareSync(password, user.password)) {
        return res.status(401).json({ message: 'Invalid email or password' });
    }

    const token = jwt.sign({ email: user.email }, 'secretkey', { expiresIn: '1h' });
    res.json({ token });
});

// Register route
router.post('/register', (req, res) => {
    const { email, password, confirmPassword } = req.body;

    if (!email || !password || !confirmPassword) {
        return res.status(400).json({ message: 'All fields are required' });
    }

    if (password !== confirmPassword) {
        return res.status(400).json({ message: 'Passwords do not match' });
    }

    const userExists = testUsers.find(user => user.email === email);
    if (userExists) {
        return res.status(400).json({ message: 'User already exists' });
    }

    const hashedPassword = bcrypt.hashSync(password, 10);
    testUsers.push({ email, password: hashedPassword });

    res.status(201).json({ message: 'User registered successfully' });
});

// Forgot password route
router.post('/forgot', (req, res) => {
    const { email } = req.body;

    if (!email) {
        return res.status(400).json({ message: 'Email is required' });
    }

    const user = testUsers.find(user => user.email === email);
    if (!user) {
        return res.status(404).json({ message: 'Email not found' });
    }

    const resetLink = `http://localhost:5000/reset.html?email=${encodeURIComponent(email)}`;
    console.log(`Password reset link (simulated): ${resetLink}`);

    res.status(200).json({ message: 'Password reset link sent to your email' });
});

// Reset password route
router.post('/reset', (req, res) => {
    const { email, newPassword, confirmNewPassword } = req.body;

    if (!email || !newPassword || !confirmNewPassword) {
        return res.status(400).json({ message: 'All fields are required' });
    }

    if (newPassword !== confirmNewPassword) {
        return res.status(400).json({ message: 'Passwords do not match' });
    }

    const user = testUsers.find(user => user.email === email);
    if (!user) {
        return res.status(404).json({ message: 'Email not found' });
    }

    const hashedPassword = bcrypt.hashSync(newPassword, 10);
    user.password = hashedPassword;

    res.status(200).json({ message: 'Password reset successfully' });
});

// Profile management route
router.post('/updateProfile', (req, res) => {
    const { email, fullName, dob, address1, address2, city, state, zip, skills, preferences, availability } = req.body;

    if (!email || !fullName || !dob || !address1 || !city || !state || !zip || !skills || !availability) {
        return res.status(400).json({ message: 'Required fields are missing' });
    }

    const user = testUsers.find(user => user.email === email);
    if (!user) {
        return res.status(404).json({ message: 'User not found' });
    }

    user.fullName = fullName;
    user.dob = dob;
    user.address1 = address1;
    user.address2 = address2;
    user.city = city;
    user.state = state;
    user.zip = zip;
    user.skills = skills;
    user.preferences = preferences;
    user.availability = availability;

    res.status(200).json({ message: 'Profile updated successfully', user });
});

// Get user data route
router.get('/user', (req, res) => {
    const { email } = req.query;

    if (!email) {
        return res.status(400).json({ message: 'Email is required' });
    }

    const user = testUsers.find(user => user.email === email);
    if (!user) {
        return res.status(404).json({ message: 'User not found' });
    }

    res.status(200).json(user);
});

module.exports = router;
