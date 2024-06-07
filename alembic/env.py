import os
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

# Add the directory containing your Flask application to the Python path
parent_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
os.sys.path.insert(0, parent_dir)

# Import your Flask application
from app import app
from models.models import db

# Ensure that the Flask application context is pushed
with app.app_context():
    # Configure Alembic to use the SQLAlchemy database URI from the Flask application configuration
    config = context.config
    config.set_main_option('sqlalchemy.url', app.config['SQLALCHEMY_DATABASE_URI'])

    # Run the migrations
    target_metadata = db.metadata

    # Ensure that Alembic uses the appropriate metadata for your database models
    def run_migrations_online():
        connectable = db.engine
        with connectable.connect() as connection:
            context.configure(
                connection=connection,
                target_metadata=target_metadata
            )
            with context.begin_transaction():
                context.run_migrations()

    # Call the function to run migrations online
    run_migrations_online()

