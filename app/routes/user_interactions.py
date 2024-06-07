from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify
from app.extensions import db
from flask_login import login_required, current_user
from app.models.models import User, Status, FriendRequest, UserWishList, Friendship, Message
from app.database import get_db_connection



user_interactions_bp = Blueprint('user_interactions', __name__)




def get_wishlist(user_id):
    # Assuming user_id is retrieved from authentication
    db = get_db_connection()
    cursor = db.cursor()
    
    cursor.execute("SELECT wishlist_id FROM user_wish_list WHERE user_id=?", (user_id,))
    wishlist = cursor.fetchall()
    cursor.close()
    return [movie[0] for movie in wishlist]



@user_interactions_bp.route('/wishlist')
@login_required
def wishlist():
    
    wishlist = get_wishlist(current_user.id)
    return render_template('wishlist.html', wishlist=wishlist)



@user_interactions_bp.route('/add_to_wishlist', methods=['POST'])
@login_required
def add_to_wishlist():
    data = request.get_json()
    movie_id = data.get('movieId')
    if movie_id:
    # Assuming UserWishlist model exists and is correctly set up
        new_entry = UserWishList(user_id=current_user.id, wishlist_id=movie_id)
        db.session.add(new_entry)
        db.session.commit()
        return jsonify({'success': True, 'message': 'Added to Wishlist successfully'})
    else:
        return jsonify({'success': False, 'message': 'Missing movie ID.'}), 400
    



@user_interactions_bp.route('/add_friend/<int:friends_id>', methods=['POST'])
@login_required
def add_friend(friends_id):
    friend = User.query.get(friends_id)
    if friend:
        # Check if a friendship already exists
        existing_friendship = Friendship.query.filter_by(user_id=current_user.id, friends_id=friends_id).first()
        if existing_friendship:
            flash('You are already friends with this user', 'error')
        else:
            # Create a new friendship
            friendship = Friendship(user_id=current_user.id, friends_id=friends_id, status_id=1)  # Assuming '1' is the ID for 'pending' status
            db.session.add(friendship)
            db.session.commit()
            flash('Friend request sent', 'success')
    else:
        flash('User not found', 'error')
    return redirect(url_for('profile'))



@user_interactions_bp.route('/friends')
@login_required
def friends():
    # Assuming '2' is the ID for 'accepted' status
    friends = Friendship.query.join(Status).filter(
        (Friendship.user_id == current_user.id) |
        (Friendship.friend_id == current_user.id),
        Status.id == 2
    ).all()
    return render_template('friends.html', friends=friends)



@user_interactions_bp.route('/friends')
@login_required
def friends_list():
    # This is a placeholder logic. You'll need to implement the actual logic
    # to fetch the current user's friends.
    friends = User.query.all()  # Example: Fetch all users for demo purposes

    return render_template('friends_list.html', friends=friends)



@user_interactions_bp.route('/accept_friend_request/<request_id>', methods=['POST'])
@login_required
def accept_friend_request(request_id):
    friend_request = FriendRequest.query.filter_by(id=request_id, requestee_id=current_user.id).first()
    if not friend_request:
        return {'error': 'Friend request not found'}, 404

    friend_request.status = 'accepted'
    db.session.commit()

    return {'message': 'Friend request accepted.'}, 200




@user_interactions_bp.route('/send_friend_request/<recipient_id>', methods=['POST'])
@login_required
def send_friend_request(recipient_id):
    # If you need to access data from the JSON payload:
    # data = request.json

    new_request = FriendRequest(
        requester_id=current_user.id,
        requestee_id=recipient_id
    )
    db.session.add(new_request)
    db.session.commit()

    return jsonify({'message': 'Friend request sent successfully.'}), 200



@user_interactions_bp.route('/seek')
@login_required
def search_users():
    query = request.args.get('query', '')
    if query:
        # Perform a case-insensitive search for users. Adjust according to your needs.
        users = User.query.filter(User.username.ilike(f'%{query}%')).all()
    else:
        users = []
    return render_template('seek_results.html', users=users, query=query)



@user_interactions_bp.route('/messages', methods=['GET'])
@login_required
def view_messages():
    received_messages = Message.query.filter_by(recipient_id=current_user.id).all()
    sent_messages = Message.query.filter_by(sender_id=current_user.id).all()

    return jsonify({
        'received': [{'id': msg.id, 'body': msg.body, 'sender_id': msg.sender_id} for msg in received_messages],
        'sent': [{'id': msg.id, 'body': msg.body, 'recipient_id': msg.recipient_id} for msg in sent_messages]
    }), 200



@user_interactions_bp.route('/unread_messages_count')
@login_required
def unread_messages_count():
    count = Message.query.filter_by(recipient_id=current_user.id, read=False).count()  # Assuming you have a 'read' column
    return jsonify({'unreadCount': count})



@user_interactions_bp.route('/unread-messages')
@login_required
def unread_messages_view():
    # Assuming `current_user` is the logged-in user
    unread_messages = Message.query.filter_by(recipient_id=current_user.id, read=False).all()

    return render_template('unread_messages.html', messages=unread_messages)



@user_interactions_bp.route('/send_message/<recipient_id>', methods=['POST'])
@login_required
def send_message(recipient_id):
    data = request.json
    message_body = data.get('body')
    if not message_body:
        return jsonify({'error': 'Message body is required'}), 400

    new_message = Message(
        sender_id=current_user.id,
        recipient_id=recipient_id,
        body=message_body
    )
    db.session.add(new_message)
    db.session.commit()

    return jsonify({'message': 'Message sent successfully.'}), 200