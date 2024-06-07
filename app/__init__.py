# app/__init__.py

from flask import Flask, redirect, url_for, render_template
from app.extensions import db, login_manager, migrate, init_app
from app.config import Config
from app.routes.auth import auth_bp
from app.routes.profile import profile_bp
from app.routes.media import media_bp
from app.routes.forum import forum_bp
from app.routes.user_interactions import user_interactions_bp
from app.routes.movie import movies_bp
from app.routes.misc import misc_bp
import os
import logging
from logging.handlers import RotatingFileHandler

def setup_logging(app):
    if not app.debug:
        file_handler = RotatingFileHandler('app.log', maxBytes=10240, backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
        ))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    ))
    logging.getLogger().addHandler(console_handler)
    logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

def create_app():
    app = Flask(__name__, instance_relative_config=True, template_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'))
    app.config.from_object(Config)

    setup_logging(app)

    init_app(app)

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(profile_bp, url_prefix='/profile')
    app.register_blueprint(movies_bp, url_prefix='/movies')
    app.register_blueprint(forum_bp, url_prefix='/forum')
    app.register_blueprint(misc_bp, url_prefix='/misc')
    app.register_blueprint(user_interactions_bp, url_prefix='/user_interactions')
    app.register_blueprint(media_bp, url_prefix='/media')

    @app.route('/')
    def root():
        return redirect(url_for('auth.signin'))

    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('_404_.html'), 404

    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()
        return render_template('_500_.html'), 500

    with app.app_context():
        # Import models here to ensure they are registered
        from app.models.models import User, Movies, Cast, Directors, UserRating, UserTop5, UserTop10, UserWishList, Friendship, Status, Topics, Reply, List, ListItem, Message, FriendRequest
        db.create_all()
        if 'movies' in app.config['SQLALCHEMY_BINDS']:
            movie_engine = db.get_engine(app, bind='movies')
            db.metadata.create_all(bind=movie_engine)

    return app
