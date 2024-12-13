import pytest
from flask import jsonify
from unittest.mock import patch
from http import HTTPStatus
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():  
            yield client

class TestAdmin:

    @patch('functions.auth.validation')
    def test_create_flight_schedule_as_admin(self, mock_validation, client):

        mock_validation.return_value = None

        data = {
            "ref_Aircraft_Types_ID": 1,
            "ref_airlines_ID": 1,
            "airline_code": "AA",
            "first_airport_code": "LAX",
            "final_airport_code": "JFK",
            "departure_date_time": "2024-12-12 15:30",
            "arraval_date_time": "2024-12-12 16:30"
        }

        response = client.post('/api/flight_schedules', json=data)

        assert response.status_code == HTTPStatus.CREATED
        responce_data = response.get_json()
        assert "message" in responce_data
        assert responce_data['message'] ==  "Flight schedule created successfully"


    @patch('functions.auth.validation')
    def test_create_flight_schedule_as_users(self, mock_validation, client):

        mock_validation.return_value = jsonify({
            "error": "Permission denied"
            }), HTTPStatus.FORBIDDEN

        data = {
            "ref_Aircraft_Types_ID": 1,
            "ref_airlines_ID": 1,
            "airline_code": "AA",
            "first_airport_code": "LAX",
            "final_airport_code": "JFK",
            "departure_date_time": "2024-12-12 15:30",
            "arraval_date_time": "2024-12-12 16:30"            
        }

        response = client.post('/api/flight_schedules', json=data)
        assert response.status_code == HTTPStatus.FORBIDDEN
        responce_data = response.get_json()
        assert "error" in responce_data
        assert responce_data["error"] == "Permission denied"        


    @patch('functions.auth.validation')
    def test_create_flight_schedule_validation_failure(self,mock_validation, client ):

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

        response = client.post('/api/flight_schedules', json=data)

        assert response.status_code == HTTPStatus.UNAUTHORIZED
        responce_data = response.get_json()
        assert "error" in responce_data
        assert responce_data["error"] == "An unexpected error occurred"



    @patch('functions.auth.validation')
    def test_create_flight_schedule_as_admin_if_no_data(self, mock_validation, client):

        mock_validation.return_value = None

        data = {}

        response = client.post('/api/flight_schedules', json=data)

        assert response.status_code == HTTPStatus.BAD_REQUEST
        responce_data = response.get_json()
        assert "error" in responce_data
        assert responce_data['error'] ==  "No data provided"


    @patch('functions.auth.validation')
    def test_create_flight_schedule_as_admin_incase_error(mock_validation, mock_db_read, client):
    
        mock_validation.return_value = None
        mock_db_read.side_effect = Exception("Database connection failed")

        data = {
            "ref_Aircraft_Types_ID": 1,
            "ref_airlines_ID": 1,
            "airline_code": "AA",
            "first_airport_code": "LAX",
            "final_airport_code": "JFK",
            "departure_date_time": "2024-12-12 15:30",
            "arraval_date_time": "2024-12-12 16:30"            
        }

       
        response = client.post('/api/flight_schedules', json=data)
        assert response.status_code == HTTPStatus.BAD_REQUEST
        
        responce_data = response.get_json()
        assert "error" in responce_data
        assert isinstance(responce_data["error"], str)  
        assert "Failed to create flight schedule" in responce_data["error"]