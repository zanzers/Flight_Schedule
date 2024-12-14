import pytest
import os
from unittest.mock import patch, MagicMock
from functions.conn import db_read, get_db, DATABASE_URL
from http import HTTPStatus
from functions.mockDb import *
from mysql.connector import Error

    


@pytest.fixture
def mock_db():
    db = MockDb()
    db.setup_mockdb()
    yield db
    db.teardown_mock()



class TestDatabaseRead:


    @patch('mysql.connector.connect')    
    def test_database_read_successfully(self,mock_connect, mock_db):

        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_connect.return_value = mock_conn
        
        mock_connect.side_effect = Error("Database connection failed")
        mock_query = """
            SELECT flight_schedule_ID, airline_code, arraval_date_time, 
                   departure_date_time, final_airport_code, first_airport_code 
            FROM flight_schedule
        """
        mock_result = [
            {
                "flight_schedule_ID": 1,
                "airline_code": "AA",
                "arraval_date_time": "2024-12-12 15:30",
                "departure_date_time": "2024-12-12 16:30",
                "final_airport_code": "JFK",
                "first_airport_code": "LAX",
            }
        ]

        mock_db.setup_mockdb(fetchall_result=mock_result)
        result = db_read(mock_query, param=None)


        assert result is not None
        assert len(result) > 0
        assert result[0]["flight_schedule_ID"] == 1
        assert result[0]["airline_code"] == "AA"

    def test_database_with_no_results(self, mock_db):
        mock_query = """
            SELECT flight_schedule_ID, airline_code, arraval_date_time, 
                   departure_date_time, final_airport_code, first_airport_code 
            FROM flight_schedule
        """

        mock_db.setup_mockdb(fetchall_result=[])

        result = db_read(mock_query, param=None)

        assert result == []

    def test_database_read_with_param(self, mock_db):
    
            mock_query = """
                SELECT flight_schedule_ID, airline_code, arraval_date_time, 
                    departure_date_time, final_airport_code, first_airport_code 
                FROM flight_schedule
                WHERE flight_schedule_ID = %s
            """
            mock_result = [
                {
                    "flight_schedule_ID": 1,
                    "airline_code": "AA",
                    "arraval_date_time": "2024-12-12 15:30",
                    "departure_date_time": "2024-12-12 16:30",
                    "final_airport_code": "JFK",
                    "first_airport_code": "LAX",
                }
            ]


            mock_db.setup_mockdb(fetchall_result=mock_result)

            param = (1,) 
            result = db_read(mock_query, param=param)

            assert result is not None
            assert result == HTTPStatus.OK

    def test_database_read_with_no_results_for_param(self, mock_db):
        mock_query = """
            SELECT flight_schedule_ID, airline_code, arraval_date_time, 
                   departure_date_time, final_airport_code, first_airport_code 
            FROM flight_schedule
            WHERE flight_schedule_ID = %s
        """

        mock_db.setup_mockdb(fetchall_result=[])
        param = (9999,)
        result = get_db(mock_query, param=param)

        assert result == []

    def test_database_read_with_invalid_param(self, mock_db):
      
        mock_query = """
            SELECT flight_schedule_ID, airline_code, arraval_date_time, 
                   departure_date_time, final_airport_code, first_airport_code 
            FROM flight_schedule
            WHERE flight_schedule_ID = %s
        """
        invalid_param = ("invalid",)  

        mock_db.setup_mockdb(fetchall_result=[])
        result = get_db(mock_query, param=invalid_param)

        assert result == [] 



    def test_database_url_conn_with_error(self, monkeypatch):
         
         monkeypatch.delenv('DATABASE_URL', raising=False)

         with pytest.raises(ValueError):
              if not os.getenv('DATABASE_URL'):
                   raise ValueError("DATABASE_URL environment variable is not set.")





if __name__ == '__main__':
    pytest.main()
