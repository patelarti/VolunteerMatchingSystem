const volunteerList = document.getElementById('volunteer-list');
const infoContent = document.getElementById('info-content');
const historyTbody = document.getElementById('history-tbody');

let selectedVolunteerElement = null;
let selectedVolunteer = null;

const events = [
    {
        name: "Community Cleanup",
        description: "Join us for a community-wide cleanup event to help keep our neighborhood beautiful. Volunteers will pick up litter, plant trees, and more.",
        location: "Central Park, Main Street",
        required_skills: ["Environmental Awareness", "Physical Fitness", "Teamwork"],
        urgency: "Medium",
        date: "2023-07-10"
    },
    {
        name: "Charity Run",
        description: "A charity run to raise funds for local schools. Volunteers are needed to help with registration, handing out water, and cheering on participants.",
        location: "Riverfront Park, Riverside Drive",
        required_skills: ["Event Planning", "Public Speaking", "First Aid"],
        urgency: "High",
        date: "2023-08-15"
    },
    {
        name: "Food Drive",
        description: "Help us organize and distribute food to families in need. Volunteers will sort donations, pack food boxes, and assist with distribution.",
        location: "Community Center, 5th Avenue",
        required_skills: ["Organization", "Customer Service", "Lifting"],
        urgency: "Low",
        date: "2023-09-01"
    },
    {
        name: "Senior Care Visit",
        description: "Spend time with seniors at the local nursing home. Volunteers will engage in activities, assist with meals, and provide companionship.",
        location: "Sunset Nursing Home, Oak Street",
        required_skills: ["Compassion", "Patience", "Communication"],
        urgency: "Medium",
        date: "2023-10-05"
    },
    {
        name: "Youth Mentoring",
        description: "Mentor at-risk youth and help them develop essential life skills. Volunteers will participate in one-on-one mentoring and group activities.",
        location: "Youth Center, Elm Street",
        required_skills: ["Mentoring", "Active Listening", "Conflict Resolution"],
        urgency: "High",
        date: "2023-11-20"
    },
    {
        name: "Holiday Toy Drive",
        description: "Collect and distribute toys to children in need during the holiday season. Volunteers will organize toy donations and assist with gift wrapping.",
        location: "Community Hall, Maple Avenue",
        required_skills: ["Organization", "Creativity", "Customer Service"],
        urgency: "Medium",
        date: "2023-12-15"
    }
];

const volunteers = [
    {
        name: "Alice Johnson",
        address1: "123 Main Street",
        address2: "Apt 4B",
        city: "Springfield",
        state: "IL",
        zip: "62704",
        skills: ["Event Planning", "Fundraising"],
        preferences: "I prefer weekend events.",
        availability: ["2023-07-10", "2023-07-11", "2023-07-17"],
        email: "alice@example.com",
        phone: "123-456-7890",
        assigned_event: "",
        history: [
            { event: events[0], status: "Completed" },
            { event: events[1], status: "Completed" }
        ]
    },
    {
        name: "Bob Smith",
        address1: "456 Elm Street",
        address2: "",
        city: "Riverside",
        state: "CA",
        zip: "92501",
        skills: ["Social Media", "Graphic Design"],
        preferences: "No preferences.",
        availability: ["2023-08-15", "2023-08-20", "2023-08-25"],
        email: "bob@example.com",
        phone: "123-456-7891",
        assigned_event: "Charity Run",
        history: [
            { event: events[2], status: "Completed" },
            { event: events[3], status: "Pending" }
        ]
    },
    // Add more volunteers as needed
];

// Function to update the volunteer list
function updateVolunteerList() {
    volunteerList.innerHTML = ''; // Clear the list

    for (const volunteer of volunteers) {
        const listItem = document.createElement('li');
        listItem.textContent = `${volunteer.name} - Skills: ${volunteer.skills.join(', ')}`;
        listItem.addEventListener('click', () => selectVolunteer(listItem, volunteer));
        volunteerList.appendChild(listItem);
    }
}

function selectVolunteer(listItem, volunteer) {
    if (selectedVolunteerElement) {
        selectedVolunteerElement.classList.remove('selected');
    }
    listItem.classList.add('selected');
    selectedVolunteerElement = listItem;
    selectedVolunteer = volunteer;
    showVolunteerInfo();
    updateVolunteerHistory();
}

// Function to show volunteer info
function showVolunteerInfo() {
    if (selectedVolunteer) {
        infoContent.innerHTML = `
            <p><strong>Name:</strong> ${selectedVolunteer.name}</p>
            <p><strong>Address:</strong> ${selectedVolunteer.address1} ${selectedVolunteer.address2}</p>
            <p><strong>City:</strong> ${selectedVolunteer.city}</p>
            <p><strong>State:</strong> ${selectedVolunteer.state}</p>
            <p><strong>Zip:</strong> ${selectedVolunteer.zip}</p>
            <p><strong>Skills:</strong> ${selectedVolunteer.skills.join(', ')}</p>
            <p><strong>Preferences:</strong> ${selectedVolunteer.preferences}</p>
            <p><strong>Availability:</strong> ${selectedVolunteer.availability.join(', ')}</p>
            <p><strong>Email:</strong> ${selectedVolunteer.email}</p>
            <p><strong>Phone:</strong> ${selectedVolunteer.phone}</p>
            ${selectedVolunteer.assigned_event ? `<p><strong>Assigned Event:</strong> ${selectedVolunteer.assigned_event}</p>` : `<p><strong>Assigned Event: </strong> None</p>`}
        `;
    } else {
        infoContent.innerHTML = '<p>Please select a volunteer.</p>';
    }
}

// Function to update the volunteer history
function updateVolunteerHistory() {
    historyTbody.innerHTML = ''; // Clear the table body

    if (selectedVolunteer && selectedVolunteer.history) {
        for (const entry of selectedVolunteer.history) {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${entry.event.name}</td>
                <td>${entry.event.description}</td>
                <td>${entry.event.location}</td>
                <td>${entry.event.required_skills.join(', ')}</td>
                <td>${entry.event.urgency}</td>
                <td>${entry.event.date}</td>
                <td>${entry.status}</td>
            `;
            historyTbody.appendChild(row);
        }
    }
}

// Initial display of volunteers
updateVolunteerList();
