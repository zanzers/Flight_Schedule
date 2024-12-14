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



countries = [
    "USA", "UK", "Canada", "Australia", "Germany", "France", "Italy", 
    "Brazil", "India", "Japan", "China", "Mexico", "Spain", "South Korea",
    "Russia", "South Africa", "United Arab Emirates", "Egypt", "Turkey", "Argentina"
]


for _ in range(25):
    airline_name = fake.company()  
    airline_country = random.choice(countries)  

    cursor.execute("""
        INSERT INTO ref_airlines (
            airlines_name,
            airlines_country
        ) VALUES (%s, %s)
    """, (airline_name, airline_country))

aircraft_types = [
    "Boeing 737", "Airbus A320", "Boeing 777", "Airbus A350", "Boeing 787",
    "Airbus A380", "Bombardier Q400", "Embraer E175", "Cessna 172", "Pilatus PC-12"
]

aircraft_capacities = [
    "150", "180", "200", "220", "250", "300", "350", "400", "500"
]


for _ in range(25):
    aircraft_name = random.choice(aircraft_types)  
    aircraft_capacity = random.choice(aircraft_capacities)  


    cursor.execute("""
        INSERT INTO ref_aircraft_types (
            aircraft_type_name,
            aircraft_type_capacity
        ) VALUES (%s, %s)
    """, (aircraft_name, aircraft_capacity))


conn.commit()
cursor.close()
conn.close()

print("25 fake airport records inserted.")
