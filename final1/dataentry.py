import psycopg2
import csv

# Define the database connection parameters
db_params = {
    'database': 'h1b',
    'user': 'postgres',
    'password': 'Password',
    'host': 'localhost',
    'port': '5432',
}

# Function to ingest data from a CSV file into the database
def ingest_data(csv_file, conn):
    try:
        cursor = conn.cursor()
        with open(csv_file, 'r') as file:
            cursor.copy_expert(f"COPY final1_table FROM STDIN CSV HEADER", file)
        conn.commit()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    conn = psycopg2.connect(**db_params)

    # Specify the path to your CSV files and ingest them
    csv_files = [r"C:\Users\samar\OneDrive\Desktop\Hackathon\Final\processed.csv"]


    for file in csv_files:
        ingest_data(file, conn)

    conn.close()