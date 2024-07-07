const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');

// Dummy user for demonstration purposes
const user = {
  email: 'testuser@example.com',
  password: bcrypt.hashSync('password123', 8) // Storing hashed password
};

exports.login = (req, res) => {
  const { email, password } = req.body;

  if (email !== user.email) {
    return res.status(401).json({ message: 'Invalid email or password' });
  }

  const passwordIsValid = bcrypt.compareSync(password, user.password);

  if (!passwordIsValid) {
    return res.status(401).json({ message: 'Invalid email or password' });
  }

  const token = jwt.sign({ id: user.email }, 'secret', {
    expiresIn: 86400 // 24 hours
  });

  res.status(200).json({ token });
};
