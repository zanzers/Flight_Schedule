import mysql.connector
from mysql.connector import Error
from http import HTTPStatus


config = {
    'user': 'root',  
    'password': 'root',
    'host': 'localhost', 
    'database': 'airlines_schedule'
}


def db_read(query, param=None):
      
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor(dictionary=True)

    try:    
        
        if param != None:
           cursor.execute(query, param)
           conn.commit()

           if query.strip().startswith("DELETE"):
              return cursor.rowcount


           cursor.close()
           conn.close()
           
           return HTTPStatus.OK
           
        else:
            
         cursor.execute(query)

         entries = cursor.fetchall()
         cursor.close()
         conn.close()
         return entries  
    

    except Error as e:
        print(f"Error: {e}")
        return HTTPStatus.INTERNAL_SERVER_ERROR
    
