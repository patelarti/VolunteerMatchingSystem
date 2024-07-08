const volunteerList = document.getElementById('volunteer-list');
const infoContent = document.getElementById('info-content');
const eventList = document.getElementById('event-list');
const eventContent = document.getElementById('event-content');

let selectedVolunteerElement = null;
let selectedVolunteer = null;

let selectedEventElement = null;
let selectedEvent = null;

// Test array of volunteers (replace with actual data later)
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
        assigned_event: ""
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
        assigned_event: "Charity Run"
    },
    {
        name: "Carol Williams",
        address1: "789 Oak Avenue",
        address2: "Suite 100",
        city: "Hometown",
        state: "TX",
        zip: "75001",
        skills: ["Writing", "Translation"],
        preferences: "Prefer morning shifts.",
        availability: ["2023-09-01", "2023-09-03", "2023-09-10"],
        email: "carol@example.com",
        phone: "123-456-7892",
        assigned_event: ""
    },
    {
        name: "David Brown",
        address1: "321 Maple Drive",
        address2: "",
        city: "Greenville",
        state: "SC",
        zip: "29601",
        skills: ["Customer Service", "Lifting"],
        preferences: "Prefer events that are physically demanding.",
        availability: ["2023-10-05", "2023-10-12", "2023-10-19"],
        email: "david@example.com",
        phone: "123-456-7893",
        assigned_event: ""
    },
    {
        name: "Emily Clark",
        address1: "654 Pine Lane",
        address2: "",
        city: "Fairview",
        state: "TN",
        zip: "37062",
        skills: ["Mentoring", "Active Listening"],
        preferences: "Prefer working with youth.",
        availability: ["2023-11-20", "2023-11-25", "2023-11-30"],
        email: "emily@example.com",
        phone: "123-456-7894",
        assigned_event: "Youth Mentoring"
    },
    {
        name: "Franklin Green",
        address1: "987 Cedar Court",
        address2: "Floor 2",
        city: "Westfield",
        state: "MA",
        zip: "01085",
        skills: ["Organization", "Creativity"],
        preferences: "I like to work on holiday-related events.",
        availability: ["2023-12-15", "2023-12-20", "2023-12-25"],
        email: "franklin@example.com",
        phone: "123-456-7895",
        assigned_event: "Holiday Toy Drive"
    }
];

// Function to update the volunteer list
function updateVolunteerList() {
    volunteerList.innerHTML = ''; // Clear the list

    for (const volunteer of volunteers) {
        const listItem = document.createElement('li');
        listItem.textContent = `${volunteer.name} - Skills: ${volunteer.skills}`;
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
    showInfo()
}

// Function to show volunteer info
function showInfo() {
 
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
    
}

// Function to update the event list
function updateEventList() {
    eventList.innerHTML = ''; // Clear the list

    for (const event of events) {
        const listItem = document.createElement('li');
        listItem.textContent = `${event.name} - ${event.date}`;
        listItem.addEventListener('click', () => selectEvent(listItem,event));
        eventList.appendChild(listItem);
    }
}

function selectEvent(listItem, event) {
    if (selectedEventElement) {
        selectedEventElement.classList.remove('selected');
    }
    listItem.classList.add('selected');
    selectedEventElement = listItem;
    selectedEvent = event;
    showEventInfo()
}

// Function to show event info
function showEventInfo(event) {
    if (selectedEvent) {
   eventContent.innerHTML = `
        <p><strong>Name:</strong> ${selectedEvent.name}</p>
        <p><strong>Description:</strong> ${selectedEvent.description}</p>
        <p><strong>Location:</strong> ${selectedEvent.location}</p>
        <p><strong>Required Skills:</strong> ${selectedEvent.required_skills.join(', ')}</p>
        <p><strong>Urgency:</strong> ${selectedEvent.urgency}</p>
        <p><strong>Date:</strong> ${selectedEvent.date}</p>
    `;
}
}

// Function to assign event
function assignEvent() {
    if (selectedVolunteer) {
        alert(`Assigning event to ${selectedVolunteer.name}`);
        // Logic to assign event goes here
    } else {
        alert('Please select a volunteer.');
    }
}

// Initial display of volunteers and events
updateVolunteerList();
updateEventList();
