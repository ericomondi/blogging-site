import psycopg2


 # Here we establish the connection
conn = psycopg2.connect(
    host='127.0.0.1',
    database = "blogs",
    user = "postgres",
    password = "2345"
    
)
# Create a cursor
cursor = conn.cursor() 

def get_data(table_name):

        # here we retrieve data from the table and return them as records
        
        cursor.execute(f"SELECT * FROM {table_name}")
        records = cursor.fetchall()

        return records