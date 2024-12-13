import pytest
from app import app
from unittest.mock import patch
from http import HTTPStatus
from functions.mockDb import MockDb


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


@pytest.fixture
def mock_db():
    mock_db = MockDb()
    yield mock_db
    mock_db.teardown_mock()


class TestFlightsGet:
    def test_get_all_flight_schedules(self, mock_db, client):

        mock_db.setup_mockdb(fetchall_result=mock_db.get_default_flight_schedule())

        response = client.get('/api/flight_schedules')

        assert response.status_code == HTTPStatus.OK
        responce_data = response.get_json()
        assert "Airlines Flight Schedules" in responce_data
        assert len(responce_data["Airlines Flight Schedules"]) > 0

    def test_get_specific_flight_schedule(self, mock_db, client):

        mock_db.setup_mockdb(fetchall_result=mock_db.get_specific_flight_schedule(1))
        
        response = client.get('/api/flight_schedules/1')
        
        assert response.status_code == HTTPStatus.OK
        responce_data = response.get_json()
        assert "Flight Details" in responce_data
        assert responce_data["Flight Details"]["flight_no"] == 1
        assert responce_data["Flight Details"]["airline_code"] == "AA"

    def test_get_non_existent_flight_schedule(self, mock_db, client):
       
        mock_db.setup_mockdb(fetchall_result=[])

        response = client.get('/api/flight_schedules/999')
        assert response.status_code == HTTPStatus.NOT_FOUND
        responce_data = response.get_json()
        assert "error" in responce_data
        assert responce_data["error"] == "Flight with flight_no 999 not found."

    def test_get_flights_error(self,client):

        with patch('mysql.connector.connect', side_effect=Exception("Database connection failed")):
            response = client.get('/api/flight_schedules')
    
        assert response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR
        responce_data = response.get_json()
        assert "error" in responce_data
        assert isinstance(responce_data["error"], str)  
        assert "An error appeared" in responce_data["error"]

    