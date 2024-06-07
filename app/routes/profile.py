from flask import Blueprint, render_template, redirect, url_for, flash, session, request, current_app
from werkzeug.utils import secure_filename
from flask_login import login_required, current_user
from app.extensions import db
from app.routes.misc import get_current_user, allowed_file, get_top_10_movies, get_top_5_directors


import os

from app.database import get_db_connection  
from app.models.models import User, Friendship


profile_bp = Blueprint('profile', __name__)




@profile_bp.route('/profile')
@login_required
def view_profile():
    # Profile view logic
    pass

@profile_bp.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    # Edit profile logic
    pass



@profile_bp.route('/account')
def account():
    return render_template('account.html')




@profile_bp.route('/update_account_settings', methods=['POST'])
def update_account_settings():
    # Check if the user is logged in
    if 'username' not in session:
        flash('Please sign in to update account settings', 'warning')
        return redirect(url_for('signin'))

    # Process the form data and update the user's account settings in the database

    flash('Account settings updated successfully', 'success')
    return redirect(url_for('profile'))

@profile_bp.route('/delete_account', methods=['POST'])
def delete_account():
    if request.method == 'POST':
        # Get the currently logged-in user (you may need to implement this logic)
        # For demonstration purposes, I'm assuming you have a function to get the user
        current_user = get_current_user()  # Implement this function

        # Check if the user is authenticated (you may need to implement this logic)
        if current_user:
            # Confirm that the user wants to delete their account
            confirmed = request.form.get('confirmed', 'false') == 'true'
            if confirmed:
                # Delete the user account from the database
                User.query.filter_by(id=current_user.id).delete()
                db.session.commit()
                # Redirect the user to the homepage after account deletion
                return redirect(url_for('homepage'))
            else:
                # Redirect the user back to the homepage if deletion is not confirmed
                return redirect(url_for('homepage'))
        else:
            # Handle the case where the user is not authenticated (e.g., redirect to sign-in page)
            return redirect(url_for('signin'))
    else:
        # Handle other HTTP methods if necessary
        pass




@profile_bp.route('/update_username', methods=['POST'])
@login_required  # Decorate the route with login_required to ensure the user is authenticated
def update_username():
    new_username = request.form.get('new_username')
    if new_username:
        # Get the current user from the 'user' table
        current_user_db = User.query.get(current_user.id)
        # Update the username
        current_user_db.username = new_username
        # Commit the changes to the database
        db.session.commit()
        flash('Username updated successfully!', 'success')
    else:
        flash('Username cannot be empty', 'error')
    return redirect(url_for('profile'))    



@profile_bp.route('/upload_profile_picture', methods=['GET', 'POST'])
@login_required
def upload_profile_picture():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'profile_picture' not in request.files:
            return redirect(request.url)
        file = request.files['profile_picture']
        # If user does not select file, browser also submits an empty part without filename
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
            # Update user's profile picture URL in the database here
            # Redirect to the profile page or wherever appropriate
            return redirect(url_for('profile', filename=filename))
    # If GET or failed POST, reload the profile edit page or show an error message
    return redirect(url_for('profile'))



@profile_bp.route('/set_default_profile_picture', methods=['POST'])
@login_required
def set_default_profile_picture():
    selected_pic_name = request.form.get('selectedPicName')
    if selected_pic_name:
        if not selected_pic_name.startswith('images/defaults/'):
            full_path = 'images/defaults/' + selected_pic_name
        else:
            full_path = selected_pic_name
        
        current_user.profile_picture = full_path
        db.session.commit()
        
        flash('Profile picture updated successfully.', 'success')
    
    return redirect(url_for('profile'))



@profile_bp.route('/profile')
@login_required
def profile():
    db_connection = get_db_connection()  # Ensure this is called within a request context
    top_10_movies = get_top_10_movies(current_user.id, db_connection)  # Adjust function to accept db_connection
    top_5_directors = get_top_5_directors(current_user.id, db_connection)
    # Assuming '2' is the ID for the 'accepted' status in your Status model
    accepted_status_id = 2

    
    top_10_movies = get_top_10_movies(current_user.id)
    top_5_directors = get_top_5_directors(current_user.id)

    default_pictures = [filename for filename in os.listdir(current_app.config['DEFAULT_PICS_FOLDER'])]

    # Get friends where the current user is either the initiator or the recipient of the accepted friendship
    # This query assumes that 'user_id' and 'friend_id' in Friendship model represent the two users in a friendship
    friends = Friendship.query.filter(
        (Friendship.user_id == current_user.id) | (Friendship.friends_id == current_user.id),
        Friendship.status_id == accepted_status_id
    ).all()

    # Retrieve User objects for each friend relationship
    # Assuming Friendship model has relationships defined to User model (not shown in your model definition)
    friends_info = []
    for friendship in friends:
        # Determine if current user is the user_id or friend_id in this friendship
        friend_id = friendship.friends_id if friendship.user_id == current_user.id else friendship.user_id
        friend = User.query.get(friend_id)
        if friend:  # Just to be safe
            friends_info.append(friend)

    return render_template('profile.html', top_10_movies=top_10_movies, friends=friends_info, default_pictures=default_pictures, top_5_directors=top_5_directors)

def get_top_10_movies(user_id, db_connection):
    cursor = db_connection.cursor()
    cursor.execute("SELECT movie_id FROM user_top_10 WHERE user_id = ?", (user_id,))
    top_10_movies = cursor.fetchall()
    cursor.close()
    return [movie[0] for movie in top_10_movies]

def get_top_5_directors(user_id, db_connection):
    cursor = db_connection.cursor()
    cursor.execute("SELECT director_id FROM user_top_5_dir WHERE user_id = ?", (user_id,))
    top_5_directors = cursor.fetchall()
    cursor.close()
    return [movie[0] for movie in top_5_directors]