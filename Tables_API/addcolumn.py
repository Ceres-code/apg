import sqlite3
import os


instance_path = os.path.join(os.path.dirname(__file__), 'instance')
user_db_path = os.path.join(instance_path, 'user.db')

conn = sqlite3.connect(user_db_path)
c = conn.cursor()


c.execute('''PRAGMA table_info(user_top_10)''')
columns = c.fetchall()
wishlist_id = any('wishlist_id' in col for col in columns)


if not wishlist_id:
    c.execute('''ALTER TABLE user_top_10 ADD COLUMN wishlist_id INTEGER''')
    print("wishlist_id column added to the user_top_10 table.")


conn.commit()


conn.close()