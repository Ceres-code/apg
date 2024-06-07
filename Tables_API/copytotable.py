import os
import sqlite3

# Specify the path to the user.db file in the instance folder
instance_path = os.path.join(os.path.dirname(__file__), 'instance')
user_db_path = os.path.join(instance_path, 'user.db')

# Connect to the user.db database
user_conn = sqlite3.connect(user_db_path)
user_cursor = user_conn.cursor()

user_cursor.execute('ALTER TABLE movie DROP COLUMN title')

# Connect to the movies.db database
movies_db_path = os.path.join(os.path.dirname(__file__), 'movies.db')
movies_conn = sqlite3.connect(movies_db_path)
movies_cursor = movies_conn.cursor()

# Query movie IDs from movies.db
movies_cursor.execute('SELECT id FROM movies')
movie_ids = movies_cursor.fetchall()

# Insert movie IDs into movie table in user.db
for movie_id in movie_ids:
    user_cursor.execute('INSERT INTO movie (id) VALUES (?)', movie_id)

# Commit changes and close connections
user_conn.commit()
user_conn.close()
movies_conn.close()

print("Movie IDs copied successfully.")
