from faker import Faker
import mysql.connector
import random
from datetime import datetime, timedelta

fake = Faker()



conn = mysql.connector.connect(
    host='localhost',  
    user='root', 
    password='root',  
    database='airlines_schedule'  
)
cursor = conn.cursor()




cursor.execute("SELECT ref_aircraft_Types_ID FROM ref_aircraft_types")
aircraft_ids = [row[0] for row in cursor.fetchall()]
cursor.execute("SELECT ref_airlines_ID FROM ref_airlines")
airlines_ids = [row[0] for row in cursor.fetchall()]

def generate_flight_schedule():
    ref_aircraft_type = random.choice(aircraft_ids)
    ref_airline = random.choice(airlines_ids)
    airline_code = fake.lexify(text='???', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    first_airport_code = fake.lexify(text='???', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    final_airport_code = fake.lexify(text='???', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    
    # Random departure and arrival times
    departure_time = fake.date_this_year().strftime('%Y-%m-%d') + " " + fake.time(pattern="%H:%M:%S")
    arrival_time = (datetime.strptime(departure_time, "%Y-%m-%d %H:%M:%S") + timedelta(hours=random.randint(2, 6))).strftime('%Y-%m-%d %H:%M:%S')

    # Create SQL query
    query = """
    INSERT INTO flight_schedule (ref_aircraft_Types_ID, ref_airlines_ID, airline_code, 
                                first_airport_code, final_airport_code, departure_date_time, arraval_date_time)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    
    
    values = (ref_aircraft_type, ref_airline, airline_code, first_airport_code, final_airport_code, departure_time, arrival_time)

    return query, values


for _ in range(25):  # Adjust the number as needed
    query, values = generate_flight_schedule()
    cursor.execute(query, values)








conn.commit()
cursor.close()
conn.close()

print("25 fake airport records inserted.")
