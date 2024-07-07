const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');
const authRoutes = require('./routes/authRoutes');

const app = express();
const PORT = process.env.PORT || 5000;
const users = [
    { email: 'rahmaaloui3199@gmail.com', password: '1234' }
];
// Middleware
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Serve static files
app.use(express.static(path.join(__dirname, '../../')));

// Routes
app.use('/api', authRoutes);

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, '../../index.html'));
});

app.get('/register', (req, res) => {
    res.sendFile(path.join(__dirname, '../../register.html'));
});

app.get('/forgot', (req, res) => {
    res.sendFile(path.join(__dirname, '../../forgot.html'));
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
