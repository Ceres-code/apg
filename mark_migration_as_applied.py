from flask import Flask
from app.extensions import db
from app.config import Config
from sqlalchemy.sql import text

def mark_migration_as_applied(app, revision_id):
    with app.app_context():
        conn = db.engine.connect()
        conn.execute(text("INSERT INTO alembic_version (version_num) VALUES (:revision_id)"), {'revision_id': revision_id})
        conn.close()

if __name__ == "__main__":
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    # Replace this with your latest revision ID
    latest_revision_id = "6e93d555d8e2"
    
    mark_migration_as_applied(app, latest_revision_id)
    print(f"Marked migration {latest_revision_id} as applied.")
