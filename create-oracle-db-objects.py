import cx_Oracle

# Connection details
username = 'System'
password = 'Admin!23'
dsn = cx_Oracle.makedsn('10.255.255.254', 1521, sid='ORCL')

# Path to the file containing the DDL statement
ddl_file_path = 'run-ddl-oracle.ddl'

try:
    # Read the DDL statement from the file
    with open(ddl_file_path, 'r') as file:
        ddl_statement = file.read()

    # Establish the database connection
    connection = cx_Oracle.connect(user=username, password=password, dsn=dsn)

    # Create a cursor
    cursor = connection.cursor()

    # Execute the DDL statement
    cursor.execute(ddl_statement)

    # Commit the changes
    connection.commit()

    print("DDL statement executed successfully.")

except cx_Oracle.DatabaseError as e:
    error, = e.args
    print("Oracle error message:", error.message)

except FileNotFoundError:
    print(f"File not found: {ddl_file_path}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if connection:
        connection.close()
