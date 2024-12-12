from flask import Flask, jsonify, request
from functions.conn import db_read, db_write
from http import HTTPStatus

app = Flask(__name__)

@app.route('/api/flight_schedules', methods=['GET'])
def flight_schedules():
    query = "SELECT * FROM flight_schedule" 
    flights = db_read(query)
    return jsonify({
        "Airlines Flight Schedules": flights,
        "total_flights": len(flights)
    })




if __name__ == "__main__":
    app.run(debug=True)
