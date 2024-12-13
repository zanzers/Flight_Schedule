import pytest
from unittest.mock import patch
from flask import jsonify
from http import HTTPStatus
from app import app
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


class Testdelete:

    @patch('functions.auth.validation')
    def test_delete_flight_schedule_success(self, mock_validation, mock_db, client):

        mock_validation.return_value = None 
        mock_db.setup_mockdb(fetchall_result=mock_db.get_specific_flight_schedule(2))

        response = client.delete('/api/flight_schedules/2')  
        
        assert response.status_code == HTTPStatus.OK 
        response_data = response.get_json()
        assert "message" in response_data
        assert "Flight schedule with flight No: 2 deleted successfully" in response_data["message"]
   