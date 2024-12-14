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


for _ in range(25):
    airport_name = fake.company()  
    airport_location = fake.city()  
    airport_latitude = round(random.uniform(-90, 90), 6)  
    airport_longtitude = round(random.uniform(-180, 180), 6) 
    airport_elevation = random.randint(0, 5000) 


    cursor.execute("""
        INSERT INTO airports (
            airport_name,
            airport_location,
            airport_latitude,
            airport_longtitude,
            airport_elevation
        ) VALUES (%s, %s, %s, %s, %s)
    """, (airport_name, airport_location, airport_latitude, airport_longtitude, airport_elevation))
    
conn.commit()
cursor.close()
conn.close()

print("25 fake airport records inserted.")
