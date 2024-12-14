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





cursor.execute("SELECT flight_schedule_ID FROM flight_schedule")
flight_schedule_ids = [row[0] for row in cursor.fetchall()]

cursor.execute("SELECT airports_ID FROM airports")
airport_ids = [row[0] for row in cursor.fetchall()]
def generate_leg():
    flight_schedule_id = random.choice(flight_schedule_ids)
    airport_id = random.choice(airport_ids)
    
    # Random departure and arrival times
    departure_time = fake.date_this_year().strftime('%Y-%m-%d') + " " + fake.time(pattern="%H:%M:%S")
    arrival_time = (datetime.strptime(departure_time, "%Y-%m-%d %H:%M:%S") + timedelta(hours=random.randint(2, 6))).strftime('%Y-%m-%d %H:%M:%S')

    # Create SQL query
    query = """
    INSERT INTO legs (flight_schedule_ID, Airports_airports_ID, departure_time, arrival_time)
    VALUES (%s, %s, %s, %s)
    """
    
    # Values to insert into the legs table
    values = (flight_schedule_id, airport_id, departure_time, arrival_time)

    return query, values
for _ in range(10):  # Adjust the number of legs you want to generate
    query, values = generate_leg()
    cursor.execute(query, values)





conn.commit()
cursor.close()
conn.close()

print("25 fake airport records inserted.")
