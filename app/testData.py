import bcrypt

testUsers = [
    { 'email': 'rahmaaloui3199@gmail.com', 'password': bcrypt.hashpw('1234'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8') },
    { 'email': 'john.doe@example.com', 'password': bcrypt.hashpw('password1'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8') },
    { 'email': 'jane.smith@example.com', 'password': bcrypt.hashpw('password2'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8') },
    { 'email': 'michael.brown@example.com', 'password': bcrypt.hashpw('password3'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8') },
    { 'email': 'emily.jones@example.com', 'password': bcrypt.hashpw('password4'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8') }
]
