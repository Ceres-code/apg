from flask import current_app
from app.extensions import db  # Assuming db is initialized in a separate extensions.py

def validate_director(director_image_id):
    # Accessing the SQLAlchemy bind for 'movies'
    engine = db.get_engine(current_app, bind='movies')
    connection = engine.connect()
    try:
        query = connection.execute("SELECT image_id FROM directors WHERE image_id = :id", {'id': director_image_id})
        result = query.fetchone()
        return result is not None
    finally:
        connection.close()