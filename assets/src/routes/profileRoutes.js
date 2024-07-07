const express = require('express');
const { createUserProfile, getUserProfile, updateUserProfile } = require('../controllers/profileController');
const router = express.Router();

router.post('/profile', createUserProfile);
router.get('/profile/:email', getUserProfile);
router.put('/profile/:email', updateUserProfile);

module.exports = router;
