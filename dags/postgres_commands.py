def create_table():
    import psycopg2
    import csv
    try:
        conn = psycopg2.connect(
            dbname="airflow",
            user="airflow",
            password="airflow",
            host="postgres",
            port="5432"
        )
        cursor = conn.cursor()
        
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS bookings (
            restaurant_id UUID,
            restaurant_name VARCHAR(255),
            country VARCHAR(255),
            month VARCHAR(7),
            amount FLOAT,
            number_of_guests INT,
            number_of_bookings INT
            );
            '''
        cursor.execute(create_table_query)
        conn.commit()

        cursor.close()
        conn.close()
        print("Table created successfully.")
    except Exception as e:
        print("Error creating table:", str(e))

def insert_data_from_csv(filename):
    import psycopg2
    import csv
    try:
        conn = psycopg2.connect(
            dbname="airflow",
            user="airflow",
            password="airflow",
            host="postgres",
            port="5432"
        )
        cursor = conn.cursor()

        with open(filename, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)  # Skip header row
            for row in csvreader:
                restaurant_id, restaurant_name, country, month, amount, num_guests, num_bookings = row
                insert_query = '''
                    INSERT INTO bookings (restaurant_id, restaurant_name, country, month, amount, number_of_guests, number_of_bookings)
                    VALUES (%s, %s, %s, %s, %s, %s, %s);
                '''
                data = (restaurant_id, restaurant_name, country, month, amount, num_guests, num_bookings)
                cursor.execute(insert_query, data)
                conn.commit()

        cursor.close()
        conn.close()
        print("Data inserted successfully into the table.")
    except Exception as e:
        print("Error inserting data:", str(e))


