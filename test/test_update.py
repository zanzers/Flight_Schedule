import pytest
from flask import jsonify
from app import app
from unittest.mock import patch
from http import HTTPStatus
from functions.mockDb import MockDb




@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():  
            yield client

@pytest.fixture
def mock_db():
    mock_db = MockDb()
    yield mock_db
    mock_db.teardown_mock()

class TestUpdate:

    @patch('functions.auth.validation') 
    def test_update_flight_schedule_success_for_admin(self, mock_validation, client, mock_db):

        mock_db.setup_mockdb(fetchall_result=mock_db.get_specific_flight_schedule(1))
        mock_validation.return_value = None

        data = {
            "ref_Aircraft_Types_ID": 2,
            "ref_airlines_ID": 1,
            "airline_code": "AA",
            "first_airport_code": "LAX",
            "final_airport_code": "JFK",
            "departure_date_time": "2024-12-12 15:30",
            "arraval_date_time": "2024-12-12 16:30"
        }        

        response = client.put('/api/flight_schedules/2', json=data)
        assert response.status_code == HTTPStatus.OK
        response_data = response.get_json()

        assert "message" in response_data
        assert "Flight schedule with flight No: 2 updated successfully" in response_data["message"]
    
    @patch('functions.auth.validation') 
    def test_update_flight_schedule_success_for_user(self, mock_validation, client, mock_db):

        mock_db.setup_mockdb(fetchall_result=mock_db.get_specific_flight_schedule(1))
        mock_validation.return_value = jsonify({
            "error": "Permission denied"
            }), HTTPStatus.FORBIDDEN 
        
        data = {
            "ref_Aircraft_Types_ID": 2,
            "ref_airlines_ID": 1,
            "airline_code": "AA",
            "first_airport_code": "LAX",
            "final_airport_code": "JFK",
            "departure_date_time": "2024-12-12 15:30",
            "arraval_date_time": "2024-12-12 16:30"
        }         

        response = client.post('/api/flight_schedules', json=data)
        assert response.status_code == HTTPStatus.FORBIDDEN
        response_data = response.get_json()
        assert "error" in response_data
        assert response_data ["error"] == "Permission denied"

    @patch('functions.auth.validation') 
    def test_update_flight_schedule_success_for_admin_no_data(self, mock_validation, client, mock_db):

        mock_db.setup_mockdb(fetchall_result=mock_db.get_specific_flight_schedule(1))
        mock_validation.return_value = None

        data = {} 

        response = client.put('/api/flight_schedules/2', json=data)
        assert response.status_code == HTTPStatus.BAD_REQUEST
        response_data = response.get_json()

        assert "error" in response_data
        assert response_data ["error"] == "No data provided"       

    @patch('functions.auth.validation') 
    def test_update_flight_schedule_validation_fail(self, mock_validation, client):
        

        mock_validation.return_value = jsonify({
            "error": "An unexpected error occurred",
            "message": "No valid token provided. Please log in to access this resource."
        }), HTTPStatus.UNAUTHORIZED

        data = {
            "ref_Aircraft_Types_ID": 1,
            "ref_airlines_ID": 1,
            "airline_code": "AA",
            "first_airport_code": "LAX",
            "final_airport_code": "JFK",
            "departure_date_time": "2024-12-12 15:30",
            "arraval_date_time": "2024-12-12 16:30"
        }

        response = client.put('/api/flight_schedules/1', json=data)
        
        assert response.status_code == HTTPStatus.UNAUTHORIZED
        response_data = response.get_json()
        assert "error" in response_data
        assert response_data["error"] == "An unexpected error occurred"


import pytest
from unittest.mock import patch
from http import HTTPStatus
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            yield client


class TestUpdateFlightSchedule:

    @patch('functions.conn.db_read') 
    @patch('functions.auth.validation')  
    def test_update_flight_schedule_failed_for_admin(self, mock_validation, mock_db, client):

        mock_validation.return_value = None

        mock_db.setup_mockdb(fetchall_result=mock_db.get_specific_flight_schedule(90))
        mock_db.mock_cursor.fetchone.return_value = None 


        data = {
            "airline_code": "AA",
            "first_airport_code": "LAX",
            "final_airport_code": "JFK",
            "departure_date_time": "2024-12-12 15:30",
            "arraval_date_time": "2024-12-12 16:30"
        }

        response = client.put('/api/flight_schedules/2', json=data)
        assert response.status_code == HTTPStatus.BAD_REQUEST

        response_data = response.get_json()
        assert "error" in response_data
        assert response_data["error"] == "Failed to procees the request"
