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

## Configuration

Before running the project, configure the following environment variables:

- **DATABASE_URL**  
  URL for the MySQL database connection.


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

## Git Commit Guidelines

### Conventional Commits
```bash
feat: add user authentication
fix: resolve database connection issue
docs: update API documentation
test: add user registration tests

