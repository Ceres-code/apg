import sqlite3
import os

instance_path = os.path.join(os.path.dirname(__file__), 'instance')
user_db_path = os.path.join(instance_path, 'user.db')

# Table name you want to drop
table_name = 'topics'

# Connect to the SQLite database
conn = sqlite3.connect(user_db_path)
c = conn.cursor()

# SQL statement to drop a table
drop_table_statement = f'DROP TABLE IF EXISTS {table_name};'

try:
    # Execute the SQL statement to drop the table
    c.execute(drop_table_statement)
    
    # Commit the changes to the database
    conn.commit()
    
    print(f"Table '{table_name}' has been dropped successfully.")
except Exception as e:
    # If there is any error during the process, print the error
    print(f"An error occurred: {e}")
finally:
    # Close the connection to the database
    conn.close()
