from flask import Blueprint, render_template, redirect, url_for, request, flash

from app.routes.profile import current_user


from flask_login import login_required

from app.extensions import db
from app.models.models import Topics, Reply

forum_bp = Blueprint('forum', __name__)





@forum_bp.route('/forum')
def view_forum():
    topics = Topics.query.order_by(Topics.created_at.desc()).all()  # Assuming you have a created_at field
    return render_template('forum.html', topics=topics)



@forum_bp.route('/forum/new', methods=['GET', 'POST'])
@login_required
def new_topic():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        user_id = current_user.id  # Assuming Flask-Login integration

        new_topic = Topics(title=title, content=content, user_id=user_id)
        db.session.add(new_topic)
        db.session.commit()
        
        flash('Your topic has been posted.', 'success')
        return redirect(url_for('forum.forum'))
    
    return render_template('new_topic.html')



@forum_bp.route('/forum/topic/<int:topic_id>', methods=['GET', 'POST'])
def view_topic(topic_id):
    topic = Topics.query.get_or_404(topic_id)
    replies = Reply.query.filter_by(topic_id=topic.id).order_by(Reply.created_at.asc())

    if request.method == 'POST':
        content = request.form['content']
        reply = Reply(content=content, topic_id=topic_id, user_id=current_user.id)  # Assuming Flask-Login for user_id
        db.session.add(reply)
        db.session.commit()
        flash('Your reply has been added.', 'success')
        return redirect(url_for('forum.view_topic', topic_id=topic_id))
    
    return render_template('view_topic.html', topic=topic, replies=replies)






@forum_bp.route('/forum/delete/<int:topic_id>', methods=['POST'])
@login_required
def delete_topic(topic_id):
    topic = Topics.query.get_or_404(topic_id)
    if topic.user_id != current_user.id:
        flash('You can only delete your own topics.', 'error')
        return redirect(url_for('forum.forum'))
    
    db.session.delete(topic)
    db.session.commit()
    flash('Topic has been deleted.', 'success')
    return redirect(url_for('forum.forum'))