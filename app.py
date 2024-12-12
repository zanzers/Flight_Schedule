from flask import Flask, jsonify, request
from functions.conn import db_read
from http import HTTPStatus



app = Flask(__name__)


@app.route('/api/flight_schedules', methods=['POST', 'GET'])
def flight_schedule():
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
            } for idx, flight in enumerate(flights)]

            return jsonify({
                "Airlines Flight Schedules": processed_flights,
                "total_flights": len(processed_flights)
            })

        else:
            return create_flight_schedule()  

    except Exception as e:
        return jsonify({
            "error": f"An error appeared: {str(e)}"
        }), HTTPStatus.INTERNAL_SERVER_ERROR
      



def create_flight_schedule():
   try:
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
      

@app.route('/api/flight_schedules/<int:Flight_No>', methods=['PUT'])
def update_flight_schedule(Flight_No):
    
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "No data provided"}), HTTPStatus.BAD_REQUEST


        query = """
            UPDATE flight_schedule
            SET
                ref_Aircraft_Types_ID = %s,
                ref_airlines_ID = %s,
                airline_code = %s,
                first_airport_code = %s,
                final_airport_code = %s,
                departure_date_time = %s,
                arraval_date_time = %s
            WHERE flight_schedule_ID = %s
        """
        
        values = (
            data.get("ref_Aircraft_Types_ID"),
            data.get("ref_airlines_ID"),
            data.get("airline_code"),
            data.get("first_airport_code"),
            data.get("final_airport_code"),
            data.get("departure_date_time"),
            data.get("arraval_date_time"),
            Flight_No  
        )

        result = db_read(query, values)

        if result == HTTPStatus.OK:
            return jsonify({"message": f"Flight schedule with No {Flight_No} updated successfully"}), HTTPStatus.OK
        else:
            return jsonify({"error": "Failed to update flight schedule"
                            }), HTTPStatus.INTERNAL_SERVER_ERROR

    except Exception as e:
        return jsonify({
            "error": f"An error occurred: {str(e)}"
            }), HTTPStatus.INTERNAL_SERVER_ERROR


@app.route('/api/flight_schedules/<int:Flight_No>', methods=['DELETE'])
def delete_flight_schedule(Flight_No):

    try:
    
        query = "DELETE FROM flight_schedule WHERE flight_schedule_ID = %s"
        
        result = db_read(query, (Flight_No,))

        if result == 0:
            return jsonify({
                "error": f"Flight schedule with No {Flight_No} not found"
            }), HTTPStatus.NOT_FOUND
        
      
        return jsonify({
            "message": f"Flight schedule with No {Flight_No} deleted successfully"
        }), HTTPStatus.OK

    except Exception as e:
        return jsonify({
            "error": f"An error occurred: {str(e)}"
            }), HTTPStatus.INTERNAL_SERVER_ERROR



if __name__ == "__main__":
    app.run(debug=True)

