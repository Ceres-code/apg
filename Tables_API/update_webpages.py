from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
from app.models.models import User
from app.models.models import db
from flask_migrate import Migrate
from sqlalchemy.pool import QueuePool
import os
import sqlite3
from flask import Flask, render_template_string, url_for
from sqlalchemy import func

from app.models.models import UserRating



app = Flask(__name__)
app.secret_key = b'\xa0\xf7b\xc3sw9\x8by\x978:\x8e\xde\xcf\x13'



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['STATIC_URL_PATH'] = '/static'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SERVER_NAME'] = 'localhost:5000'
app.config['APPLICATION_ROOT'] = '/'
app.config['PREFERRED_URL_SCHEME'] = 'http'





db.init_app(app)
migrate = Migrate(app, db)

login_manager = LoginManager(app)
login_manager.login_view = 'signin'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



def generate_html_files():
    with app.app_context():
        # Connect to the movies.db to fetch all movie details
        conn = sqlite3.connect('movies.db')
        c = conn.cursor()

        # Retrieve all movies
        c.execute("""SELECT "id", "title", "release_year", "genre", "cast", "crew", "runtime", "production_company" FROM "movies" """)
        movies = c.fetchall()

        conn.close()  # Close the connection to movies.db

        for movie in movies:
            movie_id, title, release_year, genre, cast, crew, runtime, production_company = movie

            # Use SQLAlchemy to calculate average rating from UserRating model in user.db
            avg_rating_result = db.session.query(func.avg(UserRating.rating)).filter(UserRating.movie_id == movie_id).scalar()
            average_rating = round(avg_rating_result, 1) if avg_rating_result else 'No ratings yet'

            movie_details = {
                'id': movie_id,
                'title': title,
                'release_year': release_year,
                'genre': genre,
                'cast': cast,
                'crew': crew,
                'runtime': runtime,
                'production_company': production_company,
                'average_rating': average_rating,
            }

            # Define the path for the HTML file within the templates directory
            file_path = os.path.join(app.root_path, 'templates', f'{movie_id}.html')
            if os.path.exists(file_path):
                os.remove(file_path)


            template_string = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }} - Movie Details</title>
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style/movie.css') }}">
    <style>
        .stars {
            display: inline-block;
            font-size: 24px;
            color: #ffd700;
        }
    </style>
</head>
<body>
    <div class="movie-container" data-movie-id="{{ id }}">
        <h1>{{ title }}</h1>
        <img src="{{ url_for('static', filename='images/' + id|string + '.jpg') }}" alt="{{ title }} Poster" data-movie-id="{{ id }}">
        

        
        <div id="averageRating">Average Rating: {{ average_rating }}</div>

        <div id="ratingSection">
            <h2>Rate This Movie</h2>
            <form id="ratingForm">
                {% for star in range(5, 0, -1) %}
                <input type="radio" id="star{{ star }}" name="rating" value="{{ star }}" />
                <label for="star{{ star }}">{{ star }} stars</label><br>
                {% endfor %}
                <button type="submit">Submit Rating</button>
            </form>
        </div>

        <p>Release Year: {{ release_year }}</p>
        <p>Genre: {{ genre }}</p>
        <p>Cast: {{ cast }}</p>
        <p>Crew: {{ crew }}</p>
        <p>Runtime: {{ runtime }} minutes</p>
        <p>Production: {{ production_company }}</p>

        <h1>Add Movie to Top 10</h1>
        <button id="addToTop10">Add to Top 10</button>
        <button id="addToWishlist">Add to wishlist</button>

        <script src="{{ url_for('static', filename='js/addtop.js') }}"></script>
    </div>
</body>
</html>
            '''

            html_content = render_template_string(template_string, **movie_details)

            file_path = f'templates/{movie_id}.html'
            if os.path.exists(file_path):
                os.remove(file_path)

            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(html_content)

if __name__ == '__main__':
    # This function call is to generate the HTML files
    generate_html_files()
    # After generating the HTML files, the Flask app is started.
    app.run(debug=True)
