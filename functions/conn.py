import mysql.connector
from flask import jsonify
from mysql.connector import Error
from http import HTTPStatus

config = {
    'user': 'root',  
    'password': 'root',
    'host': 'localhost', 
    'database': 'airlines_schedule'
}

def db_read(query):
    try:    
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor(dictionary=True)


        cursor.execute(query)


        entries = cursor.fetchall()
        cursor.close()
        conn.close()
        return entries  
    
    except Error as e:
        print(f"Error: {e}")
        return HTTPStatus.INTERNAL_SERVER_ERROR
    

    except Exception as e:
        print(f"Database error: {str(e)}")
        return HTTPStatus.INTERNAL_SERVER_ERROR