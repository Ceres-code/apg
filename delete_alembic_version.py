from flask import Flask
from app.extensions import db
from app.config import Config
from sqlalchemy.sql import text

def delete_alembic_version(app, revision_id):
    with app.app_context():
        conn = db.engine.connect()
        conn.execute(text("DELETE FROM alembic_version WHERE version_num = :revision_id"), {'revision_id': revision_id})
        conn.close()

if __name__ == "__main__":
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    
    # Replace this with your revision ID
    revision_id = "6e93d555d8e2"
    delete_alembic_version(app, revision_id)
    print(f"Deleted migration {revision_id} from alembic_version.")
