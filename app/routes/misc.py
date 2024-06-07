from flask import Blueprint, render_template, redirect, url_for, request, flash, current_app, send_from_directory, session
from app.models.models import User, Movies
from app import db

misc_bp = Blueprint('misc', __name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    """ Check if a filename has an allowed extension. """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@misc_bp.route('/about')
def about():
    return render_template('about.html')

@misc_bp.route('/profilelists')
def profilelists():
    return render_template('profilelists.html')

@misc_bp.route('/explore')
def explore():
    return render_template('explore.html')

@misc_bp.route('/profileratings')
def profileratings():
    return render_template('profileratings.html')

@misc_bp.route('/question')
def question():
    return render_template('question.html')

@misc_bp.route('/home')
def storage():
    return render_template('render_lists.html')

@misc_bp.route('/log_route')
def log_function():
    current_app.logger.info('Handling request to /log_route')
    try:
        # Simulating a database operation
        current_app.logger.info('Performing database operation')
    except Exception as e:
        current_app.logger.error(f'An error occurred during database operation: {str(e)}')
    return 'Response for /log_route'

@misc_bp.route('/static/<path:path>')
def static_files(path):
    return send_from_directory('static', path)

def get_current_user():
    """ Retrieve the current user from the session. """
    if 'username' in session:
        return User.query.filter_by(username=session['username']).first()
    else:
        return None  

def get_wishlist(user_id):
    """ Fetch the wishlist for the user. """
    return [movie.wishlist_id for movie in User.query.get(user_id).wish_list]

def get_top_5_directors(user_id):
    """ Fetch top 5 directors for the user. """
    return [movie.director_id for movie in User.query.get(user_id).top_5]

def get_top_10_movies(user_id):
    """ Fetch top 10 movies for the user. """
    return [movie.movie_id for movie in User.query.get(user_id).top_10]

def update_movie_ratings(movie_id):
    """ Update movie ratings. """
    ratings = Movies.query.get(movie_id).ratings
    if ratings:
        total_ratings = sum(rating.rating for rating in ratings)
        num_ratings = len(ratings)
        average_rating = total_ratings / num_ratings
        movie = Movies.query.get(movie_id)
        movie.total_rating = average_rating
        movie.num_ratings = num_ratings
        db.session.commit()

def fetch_movie_details(movie_id):
    """ Fetch movie details including cast and directors. """
    movie = Movies.query.get(movie_id)
    cast_members = [{'image_id': cast.image_id, 'name': cast.name} for cast in movie.cast]
    director_members = [{'image_id': director.image_id, 'name': director.name} for director in movie.directors]
    return movie, cast_members, director_members
