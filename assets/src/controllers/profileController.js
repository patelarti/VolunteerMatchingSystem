const profiles = [];

const createUserProfile = (req, res) => {
    const { email, fullName, address1, address2, city, state, zipCode, skills, preferences, availability } = req.body;

    if (!email || !fullName || !address1 || !city || !state || !zipCode || !skills || !availability) {
        return res.status(400).json({ message: 'All required fields must be filled.' });
    }

    const newProfile = { email, fullName, address1, address2, city, state, zipCode, skills, preferences, availability };
    profiles.push(newProfile);

    res.status(201).json({ message: 'Profile created successfully.' });
};

const getUserProfile = (req, res) => {
    const { email } = req.params;

    const profile = profiles.find(profile => profile.email === email);
    if (!profile) {
        return res.status(404).json({ message: 'Profile not found.' });
    }

    res.json(profile);
};

const updateUserProfile = (req, res) => {
    const { email } = req.params;
    const { fullName, address1, address2, city, state, zipCode, skills, preferences, availability } = req.body;

    if (!fullName || !address1 || !city || !state || !zipCode || !skills || !availability) {
        return res.status(400).json({ message: 'All required fields must be filled.' });
    }

    const profile = profiles.find(profile => profile.email === email);
    if (!profile) {
        return res.status(404).json({ message: 'Profile not found.' });
    }

    profile.fullName = fullName;
    profile.address1 = address1;
    profile.address2 = address2;
    profile.city = city;
    profile.state = state;
    profile.zipCode = zipCode;
    profile.skills = skills;
    profile.preferences = preferences;
    profile.availability = availability;

    res.json({ message: 'Profile updated successfully.' });
};

module.exports = { createUserProfile, getUserProfile, updateUserProfile };
