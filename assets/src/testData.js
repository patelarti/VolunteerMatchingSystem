const bcrypt = require('bcryptjs');

const testUsers = [
    { email: 'rahmaaloui3199@gmail.com', password: bcrypt.hashSync('1234', 10) },
    { email: 'john.doe@example.com', password: bcrypt.hashSync('password1', 10) },
    { email: 'jane.smith@example.com', password: bcrypt.hashSync('password2', 10) },
    { email: 'michael.brown@example.com', password: bcrypt.hashSync('password3', 10) },
    { email: 'emily.jones@example.com', password: bcrypt.hashSync('password4', 10) }
];

module.exports = testUsers;
