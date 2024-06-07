import requests
import sqlite3

def fetch_movie_release_year(movie_id):
    api_key = '5029b9240ee95f0a236d474fc88c4a49'
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US'
    response = requests.get(url)
    data = response.json()
    release_year = int(data.get('release_date', '').split('-')[0]) if 'release_date' in data else None
    return release_year

def update_movie_release_years():
    # Connect to SQLite database
    conn = sqlite3.connect('movies.db')
    c = conn.cursor()

    # Get all movie IDs from the database
    c.execute('SELECT id FROM movies')
    movie_ids = [row[0] for row in c.fetchall()]

    # Update release year for each movie
    for movie_id in movie_ids:
        release_year = fetch_movie_release_year(movie_id)
        if release_year is not None:
            c.execute('UPDATE movies SET release_year = ? WHERE id = ?', (release_year, movie_id))

    # Commit changes and close connection
    conn.commit()
    conn.close()

update_movie_release_years()
print("Release years updated successfully.")
