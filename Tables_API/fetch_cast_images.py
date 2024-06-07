import sqlite3
import os
import requests

def fetch_and_save_top_billed_cast_images(movie_id, api_key, image_dir, conn):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={api_key}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        cast_members = data.get('cast', [])[:5]  # Limit to top 5 billed cast members
        
        for cast_member in cast_members:
            profile_path = cast_member.get('profile_path')
            if profile_path:
                image_url = f'https://image.tmdb.org/t/p/w500/{profile_path}'
                file_extension = os.path.splitext(profile_path)[-1]
                image_filename = f"{cast_member['id']}{file_extension}"
                image_path = os.path.join(image_dir, image_filename)
                
                response = requests.get(image_url)
                if response.status_code == 200:
                    with open(image_path, 'wb') as f:
                        f.write(response.content)
                    
                    # Insert into the database
                    c = conn.cursor()
                    c.execute("INSERT INTO cast (image_id, name, movie_id) VALUES (?, ?, ?)",
                              (cast_member['id'], cast_member['name'], movie_id))
                    conn.commit()
                    
                    print(f"Image saved and info added for {cast_member['name']} in movie ID {movie_id}")
                else:
                    print(f"Failed to download image for cast member {cast_member['name']}")
            else:
                print(f"No image found for cast member {cast_member['name']}")
    else:
        print(f"Failed to fetch cast data for movie ID {movie_id}: {response.status_code}")

# Your API key for TMDb
api_key = '5029b9240ee95f0a236d474fc88c4a49'

# Directory where images will be saved
image_dir = 'cast_images/'

# Ensure the directory exists, create if not
if not os.path.exists(image_dir):
    os.makedirs(image_dir)

# Connect to SQLite database
conn = sqlite3.connect('movies.db')

# Create a cursor object using the cursor() method
cursor = conn.cursor()

# Creating the 'cast' table (if it doesn't already exist)
cursor.execute('''CREATE TABLE IF NOT EXISTS cast (
                    image_id TEXT,
                    name TEXT,
                    movie_id INTEGER)''')

# Retrieve movie IDs from the database
cursor.execute('SELECT id FROM movies')
movie_ids = cursor.fetchall()

# Fetch images for the top 5 billed cast members for each movie
for movie_id_tuple in movie_ids:
    movie_id = movie_id_tuple[0]
    fetch_and_save_top_billed_cast_images(movie_id, api_key, image_dir, conn)

# Close the database connection
conn.close()
