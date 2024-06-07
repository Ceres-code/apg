from flask import Blueprint, jsonify, request, render_template, abort
from flask_login import login_user, login_required, logout_user, current_user, UserMixin
from app.extensions import db
from app.routes.misc import fetch_movie_details
from app.models.models import Movies, UserTop10, UserRating, UserWishList, UserTop5
import requests
from app.services.services import validate_director



movies_bp = Blueprint('movies', __name__)

@movies_bp.route('/movies')
def list_movies():
    # List movies logic
    pass




@movies_bp.route('/movie_pages/<int:movie_id>')
def movie_pages(movie_id):
    try:
        
        return render_template(f'{movie_id}.html')
    except Exception as e:
        
        print(e)  
        
        
        abort(404)



@movies_bp.route('/movie_details/<int:movie_id>')
def movie_details(movie_id):
    movie = Movies.query.get_or_404(movie_id)
    ratings = UserRating.query.filter_by(movie_id=movie_id).all()
    
    if ratings:
        average_rating = sum(rating.rating for rating in ratings) / len(ratings)
    else:
        average_rating = 'No ratings yet'

    return render_template(f'{movie_id}.html', movie=movie, average_rating=average_rating)        



@movies_bp.route('/rate_movie/<int:movie_id>', methods=['POST'])
@login_required
def rate_movie(movie_id):
    data = request.get_json()
    rating_value = data.get('rating')
    if rating_value:
        rating = UserRating.query.filter_by(user_id=current_user.id, movie_id=movie_id).first()
        if rating:
            rating.rating = rating_value
        else:
            new_rating = UserRating(user_id=current_user.id, movie_id=movie_id, rating=rating_value)
            db.session.add(new_rating)
        db.session.commit()
        
        return jsonify({'success': True, 'message': 'Your rating has been submitted.', 'new_average': 'New average (if calculated)'})
    else:
        return jsonify({'success': False, 'message': 'Rating not provided.'}), 400
    


@movies_bp.route('/add_to_top_10', methods=['POST'])
@login_required
def add_to_top_10():
    data = request.get_json()
    movie_id = data.get('movieId')
    if movie_id:
        
        new_entry = UserTop10(user_id=current_user.id, movie_id=movie_id)
        db.session.add(new_entry)
        db.session.commit()
        return jsonify({'success': True, 'message': 'Movie added to your Top 10 list.'})
    else:
        return jsonify({'success': False, 'message': 'Missing movie ID.'}), 400




@movies_bp.route('/add_to_wishlist', methods=['POST'])
@login_required
def add_to_wishlist():
    data = request.get_json()
    movie_id = data.get('movieId')
    if movie_id:
    
        new_entry = UserWishList(user_id=current_user.id, wishlist_id=movie_id)
        db.session.add(new_entry)
        db.session.commit()
        return jsonify({'success': True, 'message': 'Added to Wishlist successfully'})
    else:
        return jsonify({'success': False, 'message': 'Missing movie ID.'}), 400
    

@movies_bp.route('/add_top_dir', methods=['POST'])
@login_required
def add_top_dir():
    data = request.get_json()
    movie_id = data.get('movieId')
    if movie_id:
        
        new_entry = UserTop5(user_id=current_user.id, movie_id=movie_id)
        db.session.add(new_entry)
        db.session.commit()
        return jsonify({'success': True, 'message': 'Director added to favorites.'})
    else:
        return jsonify({'success': False, 'message': 'Missing movie ID.'}), 400
    


def get_popular_movies(api_key):
    response = requests.get(f"https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=en-US&page=1")
    if response.status_code == 200:
        return response.json()['results']  
    else:
        return []


def get_upcoming_movies(api_key):
    response = requests.get(f"https://api.themoviedb.org/3/movie/upcoming?api_key={api_key}&language=en-US&page=1")
    if response.status_code == 200:
        return response.json()['results']  
    else:
        return []   
    

def get_now_playing_movies(api_key):
    response = requests.get(f"https://api.themoviedb.org/3/movie/now_playing?api_key={api_key}&language=en-US&page=1")
    if response.status_code == 200:
        return response.json()['results']  
    else:
        return []  



@movies_bp.route('/homepage')
@login_required
def homepage():
    api_key = '5029b9240ee95f0a236d474fc88c4a49'
    movies = get_popular_movies(api_key)
    

    return render_template('homepage.html', user=current_user, movies=movies)


@movies_bp.route('/hp_upcoming')
@login_required
def hp_upcoming():
    api_key = '5029b9240ee95f0a236d474fc88c4a49'
    
    upcoming = get_upcoming_movies(api_key)

    return render_template('hp_upcoming.html', user=current_user, upcoming=upcoming)


@movies_bp.route('/hp_now_playing')
@login_required
def hp_now_playing():
    api_key = '5029b9240ee95f0a236d474fc88c4a49'
    
    playing = get_now_playing_movies(api_key)
    

    return render_template('hp_now_playing.html', user=current_user, playing=playing)



@movies_bp.route('/movie/<int:movie_id>')
def show_movie_details(movie_id):
    return render_template(f'{movie_id}.html')




@movies_bp.route('/api/cast/<int:movie_id>')
def get_cast_api(movie_id):
    _, cast_members, _ = fetch_movie_details(movie_id)
    if cast_members:
        # Structure the response as a list of dicts to ensure correct JSON format
        cast_list = [{'image_id': image_id, 'name': name} for image_id, name in cast_members]
        return jsonify(cast_list)
    else:
        return jsonify([]), 404



@movies_bp.route('/api/director/<int:movie_id>')
def get_director_api(movie_id):
    _, _, director_members = fetch_movie_details(movie_id)
    if director_members:
        # Structure the response as a list of dicts to ensure correct JSON format
        director_list = [{'image_id': image_id, 'name': name} for image_id, name in director_members]
        return jsonify(director_list)
    else:
        return jsonify([]), 404   
    


@movies_bp.route('/search_movies', methods=['POST'])
@login_required
def search_movies():
    query = request.form['query']

    movies = Movies.query.filter(Movies.title.ilike(f'%{query}%')).all()
    return render_template('movie_search_results.html', movies=movies)    






def add_user_top5(user_id, director_image_id):
    if validate_director(director_image_id):
        new_record = UserTop5(user_id=user_id, director_image_id=director_image_id)
        db.session.add(new_record)
        db.session.commit()
        return True
    else:
        return False 
