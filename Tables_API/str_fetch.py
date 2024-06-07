import sqlite3
import requests

# Function to fetch genres for a movie from TMDb API
def fetch_production_companies(movie_id, api_key):
    # Construct the API request URL
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'

    # Make the API request
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON and extract the genres
        data = response.json()
        production_companies = [production_companies['name'] for production_companies in data.get('production_companies', [])]
        return ', '.join(production_companies) if production_companies else None
    else:
        # Handle API request failure
        print(f"Failed to fetch production_company for movie ID {movie_id}: {response.status_code}")
        return None

# Connect to SQLite database
conn = sqlite3.connect('movies.db')
c = conn.cursor()

# Retrieve movie IDs from the database
c.execute('SELECT id FROM movies')
movie_ids = c.fetchall()

# API key for TMDb
api_key = '5029b9240ee95f0a236d474fc88c4a49'

# Loop through movie IDs and fetch genres for each movie
for movie_id_tuple in movie_ids:
    movie_id = movie_id_tuple[0]
    production_company = fetch_production_companies(movie_id, api_key)
    if production_company is not None:
        # Update the genre column in the database
        c.execute('UPDATE movies SET production_company = ? WHERE id = ?', (production_company, movie_id))
        conn.commit()
        print(f"production_company updated for movie ID {movie_id}: {production_company}")
    else:
        print(f"Failed to fetch production_company for movie ID {movie_id}")

# Close database connection
conn.close()




