
from flask import Flask, jsonify, request
from functions.conn import db_read,get_db
from http import HTTPStatus
from flask_jwt_extended import create_access_token, jwt_required

import functions.auth

app = Flask(__name__)


app.config['JWT_SECRET_KEY'] = 'Nowell'
functions.auth.initialition_jwt(app)


@app.route('/api/auth/login', methods=['POST'])
def login():
    identity = "admin"
    role =  "admin"
    access_token = create_access_token(identity=identity, additional_claims={"role": role})
    return jsonify(access_token=access_token)



@app.route('/api/flight_schedules', methods=['GET'])
@app.route('/api/flight_schedules/<int:flight_no>', methods=['GET']) 
def flight_schedule(flight_no=None):
    try:
        
        if flight_no is None:
            query = """
                SELECT flight_schedule_ID, airline_code, arraval_date_time, 
                       departure_date_time, final_airport_code, first_airport_code 
                FROM flight_schedule
            """
            flights = db_read(query, param=None)

            processed_flights = [{
                "flight_no": flight["flight_schedule_ID"], 
                "airline_code": flight["airline_code"],
                "arrival_date_time": flight["arraval_date_time"],
                "departure_date_time": flight["departure_date_time"],
                "final_airport_code": flight["final_airport_code"],
                "first_airport_code": flight["first_airport_code"],
            } for flight in flights]

            return jsonify({
                "Airlines Flight Schedules": processed_flights,
                "total_flights": len(processed_flights)
            })

        else:
            
            query = """
                SELECT flight_schedule_ID, airline_code, arraval_date_time, 
                       departure_date_time, final_airport_code, first_airport_code 
                FROM flight_schedule
                WHERE flight_schedule_ID = %s
            """
            
            flights = get_db(query, (flight_no,))
            

            if not flights:
                return jsonify({
                    "error": f"Flight with flight_no {flight_no} not found."
                }), HTTPStatus.NOT_FOUND
     
            

            return jsonify({
                "Flight Details": {
                    "flight_no": flights[0]["flight_schedule_ID"],
                    "airline_code": flights[0]["airline_code"],
                    "arrival_date_time": flights[0]["arraval_date_time"],
                    "departure_date_time": flights[0]["departure_date_time"],
                    "final_airport_code": flights[0]["final_airport_code"],
                    "first_airport_code": flights[0]["first_airport_code"],
                }
            })
        
    except Exception as e:
        return jsonify({
            "error": f"An error appeared: {str(e)}"
        }), HTTPStatus.INTERNAL_SERVER_ERROR

@app.route('/api/flight_schedules', methods=['POST'])
def create_flight_schedule():
   try:
            validation_response = functions.auth.validation()
            if validation_response:
                return validation_response


            data = request.get_json() 

            if not data:
                return no_data()

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
      

@app.route('/api/flight_schedules/<int:flight_no>', methods=['PUT'])
def update_flight_schedule(flight_no):
    


    validation_response = functions.auth.validation()
    if validation_response:
        return validation_response
    
    try:
        data = request.get_json()

        if not data:
            return no_data()


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
            flight_no
        )

        result = db_read(query, values)

        if result == HTTPStatus.OK:
            return jsonify({"message": f"Flight schedule with flight No: {flight_no} updated successfully"}), HTTPStatus.OK
        else:
            return jsonify({"error": "Failed to update flight schedule"
                            }), HTTPStatus.INTERNAL_SERVER_ERROR

    except Exception as e:
        return jsonify({
            "error": f"An error occurred: {str(e)}"
            }), HTTPStatus.INTERNAL_SERVER_ERROR


@app.route('/api/flight_schedules/<int:flight_no>', methods=['DELETE'])
def delete_flight_schedule(flight_no):
    
    validation_response = functions.auth.validation()
    if validation_response:
        return validation_response

    try:
    
        query = "DELETE FROM flight_schedule WHERE flight_schedule_ID = %s"
        
        if flight_no == '':
            return no_data()
     
        
        result = db_read(query, (flight_no,))

        if result == 0:
            return jsonify({
                "error": f"Flight schedule with flight No: {flight_no} not found"
            }), HTTPStatus.NOT_FOUND
        
      
        return jsonify({
            "message": f"Flight schedule with flight No: {flight_no} deleted successfully"
        }), HTTPStatus.OK

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), HTTPStatus.INTERNAL_SERVER_ERROR





def no_data():

    return jsonify({
        "error": "No data provided"
        }), HTTPStatus.BAD_REQUEST



if __name__ == "__main__":
    app.run(debug=True)
