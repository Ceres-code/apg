import sqlite3
import os
import requests

# Function to fetch movie posters from TMDb API
def fetch_and_save_movie_posters(movie_id, api_key, image_dir):
    # Construct the API request URL
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'

    # Make the API request
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON and extract the poster path
        data = response.json()
        poster_path = data.get('poster_path')
        
        if poster_path:
            # Construct the URL for the poster image
            image_url = f'https://image.tmdb.org/t/p/w500/{poster_path}'
            
            # Get the file extension from the URL
            file_extension = os.path.splitext(poster_path)[-1]

            # Save the image with the movie ID as filename
            image_filename = f"{movie_id}{file_extension}"
            image_path = os.path.join(image_dir, image_filename)
            
            # Download and save the image
            response = requests.get(image_url)
            if response.status_code == 200:
                with open(image_path, 'wb') as f:
                    f.write(response.content)
                print(f"Poster saved for movie ID {movie_id}")
            else:
                print(f"Failed to download poster for movie ID {movie_id}")
        else:
            print(f"No poster found for movie ID {movie_id}")
    else:
        # Handle API request failure
        print(f"Failed to fetch movie data for movie ID {movie_id}: {response.status_code}")

# Connect to SQLite database
conn = sqlite3.connect('movies.db')
c = conn.cursor()

# Retrieve movie IDs from the database
c.execute('SELECT id FROM movies')
movie_ids = c.fetchall()

# Close database connection
conn.close()

# Directory to save images
image_dir = 'static/images/'

# Ensure the directory exists, create if not
if not os.path.exists(image_dir):
    os.makedirs(image_dir)

# API key for TMDb
api_key = '5029b9240ee95f0a236d474fc88c4a49'

# Loop through movie IDs and fetch poster images for each movie
for movie_id_tuple in movie_ids:
    movie_id = movie_id_tuple[0]
    fetch_and_save_movie_posters(movie_id, api_key, image_dir)


