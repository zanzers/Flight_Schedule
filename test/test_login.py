import pytest
from unittest.mock import patch
from http import HTTPStatus
from app import app 




@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


@patch('functions.auth.login')
def test_login_as_admin(mock_create_token, client):


    mock_create_token.return_value = "mocked_access_token"

    print(f"Mock Create Token called: {mock_create_token.called}")  

    response = client.post('/api/auth/login', json={
        "username": "admin",
        "password": "admin"
    })

    assert response.status_code == HTTPStatus.OK
    responce_data = response.get_json()
    assert "access_token" in responce_data


@patch('functions.auth.login')
def get_login_username_password(client):

    response = client.post('/api/auth/login', json={
        "username": "user",
        "password": "admin"
    })

    assert response.status_cod == HTTPStatus.UNAUTHORIZED
    responce_data = response.get_json()
    assert "error" in responce_data
    assert responce_data["error"] == "Invalid credentials"


