from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()  # Declare migrate but don't initialize it yet

def init_app(app):
    global migrate
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)  # Initialize Flask-Migrate with the app and database




@login_manager.user_loader
def load_user(user_id):
    from app.models.models import User  # Import here to avoid circular dependency
    return User.query.get(int(user_id))
