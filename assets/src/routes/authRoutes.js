const express = require('express');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');

const router = express.Router();

const users = [
    {
        email: 'rahmaaloui3199@gmail.com',
        password: '$2a$10$X9t8hl8h8w8t8h' // Example hashed password
    }
];

router.post('/login', (req, res) => {
    const { email, password } = req.body;
    const user = users.find(u => u.email === email);
    if (!user) {
        return res.status(400).json({ success: false, message: 'Invalid email or password' });
    }
    const isMatch = bcrypt.compareSync(password, user.password);
    if (!isMatch) {
        return res.status(400).json({ success: false, message: 'Invalid email or password' });
    }
    const token = jwt.sign({ email: user.email }, 'secret', { expiresIn: '1h' });
    res.json({ success: true, token });
});

module.exports = router;
