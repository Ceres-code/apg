from flask import Flask
from app.extensions import db
from app.config import Config
from sqlalchemy.sql import text

def check_alembic_version(app):
    with app.app_context():
        conn = db.engine.connect()
        result = conn.execute(text("SELECT * FROM alembic_version"))
        for row in result:
            print(row)
        conn.close()

if __name__ == "__main__":
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    
    check_alembic_version(app)
