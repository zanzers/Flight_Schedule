import pytest
from unittest.mock import patch, MagicMock

class MockDb:
    def __init__(self):
        self.mock_connect = patch("mysql.connector.connect")
        self.mock_conn = None
        self.mock_cursor = None

    def setup_mockdb(self, fetchall_result=None):
      
        self.mock_conn = MagicMock()
        self.mock_cursor = MagicMock()

        self.mock_cursor.fetchall.return_value = fetchall_result if fetchall_result is not None else []
        self.mock_conn.cursor.return_value = self.mock_cursor
        self.mock_connect.start().return_value = self.mock_conn

    def teardown_mock(self):
      
        self.mock_connect.stop()

    def get_default_flight_schedule(self):
        return [
            {
                "flight_schedule_ID": 1,
                "airline_code": "AA",
                "arraval_date_time": "2024-12-12 15:30",
                "departure_date_time": "2024-12-12 16:30",
                "final_airport_code": "JFK",
                "first_airport_code": "LAX",
            },
            {
                "flight_schedule_ID": 2,
                "airline_code": "BB",
                "arraval_date_time": "2024-12-13 10:30",
                "departure_date_time": "2024-12-13 11:30",
                "final_airport_code": "ORD",
                "first_airport_code": "ATL",
            }
        ]

    def get_specific_flight_schedule(self, flight_no):
        return [
            {
                "flight_schedule_ID": flight_no,
                "airline_code": "AA",
                "arraval_date_time": "2024-12-12 15:30",
                "departure_date_time": "2024-12-12 16:30",
                "final_airport_code": "JFK",
                "first_airport_code": "LAX",
            },
            {
                "flight_schedule_ID": 2,
                "airline_code": "BB",
                "arraval_date_time": "2024-12-13 10:30",
                "departure_date_time": "2024-12-13 11:30",
                "final_airport_code": "ORD",
                "first_airport_code": "ATL",
            },
            {
                "ref_Aircraft_Types_ID": 3,
                "ref_airlines_ID": 1,
                "airline_code": "AA",
                "first_airport_code": "LAX",
                "final_airport_code": "JFK",
                "departure_date_time": "2024-12-12 15:30",
                "arraval_date_time": "2024-12-12 16:30"
            }
        ]
    
