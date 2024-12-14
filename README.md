


{
    "ref_Aircraft_Types_ID": 1,
    "ref_airlines_ID": 2,
    "airline_code": "PN121",
    "first_airport_code": "PLN",
    "final_airport_code": "MNL",
    "departure_date_time": "2024-12-25T10:00:00",
    "arraval_date_time": "2024-12-26T13:00:00"
}

{
    "username": "admin",
    "password": "admin"
}








## Project Title: Airport Flight Schedule Management System

**Description:**  
    This system allows users to view flight schedules, including arrival and departure times, as well as airport codes for airlines. Admin users have additional privileges to manage the flight schedules by creating, updating, and deleting entries.

## Installation
1. Install Flask:
    ```bash
    pip install flask
    ```

2. Install MySQL connector for Python:
    ```bash
    pip install mysql-connector-python
    ```

3. Install dependencies from `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

4. Install Pytest for testing:
    ```bash
    pip install pytest
    ```
5. Install Flask-JWT-Extended for authentication :
    ```bash
    pip install Flask-JWT-Extended
    ```
6. Install faker for Populate the table :
    ```bash
    pip install faker
    ```
7. Install pyest-cov for see test coverage :
    ```bash
    pip install pytest pytest-cov
    ```

## Configuration
Environment variables needed:

DATABASE_URL=```mysql://root:root@localhost/airlines_schedule```

SECRET_KEY=```Nowell_T_Saavedra```


---

# API Endpoints

| Endpoint                                    | Method | Description                            |
|---------------------------------------------|--------|----------------------------------------|
| `/api/auth/login`                           | POST   | Admin login                            |
| `/api/flight_schedules`                     | GET    | List all flight schedules              |
| `/api/flight_schedules/<int:flight_no>`     | GET    | Get details for a specific flight      |
| `/api/flight_schedules`                     | POST   | Create a new flight schedule           |
| `/api/flight_schedules/<int:flight_no>`     | PUT    | Update a specific flight schedule      |
| `/api/flight_schedules/<int:flight_no>`     | DELETE | Delete a specific flight schedule      |

---

## Testing
 Instructions for running tests:


1. **Run the Tests**:
       To run the tests and generate a code coverage report for my system, use the following command:
    ```bash
   pytest --cov=functions --cov=app test/
    ```

2. **Check the Missing Coverage**:
       To run the tests and generate a code that coverage and missing line in my system, use the following command:
    ```bash
   pytest --cov=functions --cov=app --cov-report=term-missing test/
    ```





## Git Commit Guidelines

### Conventional Commits
```bash
feat: add user authentication
fix: resolve database connection issue
docs: update API documentation
test: add user registration tests

    