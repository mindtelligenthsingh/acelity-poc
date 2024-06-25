import psycopg2

# Database connection parameters
db_params = {
    'dbname': 'postgres',
    'user': 'patient',
    'password': 'patient',
    'host': '73.220.64.180/80',
    'port': '5432'
}

# Read the DDL script from the file
with open('run-ddl-poc.ddl', 'r') as file:
    ddl_script = file.read()

# Function to execute the DDL script
def execute_ddl_script(ddl_script, db_params):
    try:
        # Connect to the PostgreSQL database
        connection = psycopg2.connect(**db_params)
        cursor = connection.cursor()

        # Execute the DDL script
        cursor.execute(ddl_script)

        # Commit the changes
        connection.commit()

        print("DDL script executed successfully.")

    except Exception as error:
        print(f"Error executing DDL script: {error}")

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# Execute the DDL script
execute_ddl_script(ddl_script, db_params)
