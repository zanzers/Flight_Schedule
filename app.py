from flask import Flask, jsonify, request
from functions.conn import db_read
from http import HTTPStatus


app = Flask(__name__)

@app.route('/api/flight_schedules', methods=['POST', 'GET'])
def create_flight_schedule():
   try:
        if request.method == 'GET':
            
            query = "SELECT flight_schedule_ID, airline_code, arraval_date_time, departure_date_time, final_airport_code, first_airport_code FROM flight_schedule"
            flights = db_read(query, param=None)

            processed_flights = [{

            "Flight_No": idx + 1,
            "airline_code": flight["airline_code"],
            "arrival_date_time": flight["arraval_date_time"],
            "departure_date_time": flight["departure_date_time"],
            "final_airport_code": flight["final_airport_code"],
            "first_airport_code": flight["first_airport_code"],
            }
            
            for idx, flight in enumerate(flights)]
            
            return jsonify({
                "Airlines Flight Schedules": processed_flights,
                "total_flights": len(processed_flights)
            })
            
        else:
            
            data = request.get_json() 

            if not data:
                return jsonify({
                    "error": "No data provided"
                    }), HTTPStatus.BAD_REQUEST

            query = (
                    "INSERT INTO flight_schedule "
                    "(ref_Aircraft_Types_ID, ref_airlines_ID, airline_code, "
                    "first_airport_code, final_airport_code, departure_date_time, "
                    "arraval_date_time) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s)"
                )
            values = (
                    data["ref_Aircraft_Types_ID"],
                    data["ref_airlines_ID"],
                    data["airline_code"],
                    data["first_airport_code"],
                    data["final_airport_code"],
                    data["departure_date_time"],
                    data["arraval_date_time"],
                )
            
            create_flights = db_read(query, values)

            if create_flights == HTTPStatus.OK:
                return jsonify({
                    "message": "Flight schedule created successfully"
                }), HTTPStatus.CREATED
            else:
                return jsonify({
                    "error": "Failed to create flight schedule" 
                }), HTTPStatus.INTERNAL_SERVER_ERROR

           
            

   except Exception as e:
        return jsonify({
            "error": f"Failed to create flight schedule: {str(e)}"
            }), HTTPStatus.BAD_REQUEST
      



if __name__ == "__main__":
    app.run(debug=True)

