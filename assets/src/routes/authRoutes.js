const express = require('express');
const router = express.Router();
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const testUsers = require('../testData');

router.post('/login', (req, res) => {
    const { email, password } = req.body;

    // Find user by email
    const user = testUsers.find(user => user.email === email);
    if (!user) {
        return res.status(401).json({ message: 'Invalid email or password' });
    }

    // Check password
    if (user.password !== password) {
        return res.status(401).json({ message: 'Invalid email or password' });
    }

    // Create token
    const token = jwt.sign({ email: user.email }, 'secretkey', { expiresIn: '1h' });
    res.json({ token });
});

module.exports = router;
