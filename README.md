# VolunteerMatch

VolunteerMatch is a web application designed to facilitate the matching of volunteers to events. The application includes features for user registration, profile management, event management, and volunteer history tracking.

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python, Flask
- **Database**: PostgreSQL
- **Testing**: Pytest, Coverage.py

## Features

- User Registration and Login
- User Profile Management
- Event Creation and Management
- Volunteer Matching to Events
- Volunteer History Tracking
- Notification System

## Endpoints

### User Authentication

- **POST /login**
  - Authenticate user and start session
  - Request: `{ email, password }`
  - Response: `{ message: 'Login successful' }` or `{ message: 'Invalid email or password' }`

- **POST /reset**
  - Reset user password
  - Request: `{ email, newPassword, confirmNewPassword }`
  - Response: `{ message: 'Password reset successfully' }` or appropriate error message

### User Profile

- **POST /api/updateProfile**
  - Update user profile details
  - Request: `{ email, fullName, dob, address1, address2, city, state, zip, skills, preferences, availability }`
  - Response: `{ message: 'Profile updated successfully' }`

### Event Management

- **GET /matching/api/events**
  - Retrieve all events
  - Response: `[{ id, name, description, location, required_skills, urgency, date }]`

- **POST /matching/api/assign_event**
  - Assign a volunteer to an event
  - Request: `{ volunteer_name, event_name }`
  - Response: `{ message: 'Event assigned to volunteer' }` or appropriate error message

### Volunteer Management

- **GET /matching/api/volunteers**
  - Retrieve all volunteers
  - Response: `[{ name, address1, address2, city, state, zip, skills, preferences, availability, email, phone, assigned_event, history }]`

### Volunteer History

- **GET /history/api/volunteer_history**
  - Retrieve volunteer history
  - Response: `[{ volunteer_name, event_name, status, date }]`

## Running the Application

1. **Clone the repository:**
    ```sh
    git clone https://github.com/ayyan67/VolunteerMatch.git
    cd VolunteerMatch
    ```

2. **Set up the virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the database:**
    ```sh
    flask db init
    flask db migrate
    flask db upgrade
    ```

5. **Run the application:**
    ```sh
    flask run
    ```

6. **Access the application:**
    - Open your web browser and navigate to `http://127.0.0.1:5000`

## Testing

To run the tests and generate a coverage report, use the following commands:

1. **Run the tests:**
    ```sh
    pytest --cov=app tests/
    ```

2. **Generate the coverage report:**
    ```sh
    coverage html
    ```

The coverage report will be available in the `htmlcov` directory.

## License

This project is licensed under the MIT License.
