import sqlite3
from flask import current_app

def get_db():
    conn = sqlite3.connect(current_app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute('''CREATE TABLE users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    password TEXT,
                    role TEXT NOT NULL DEFAULT 'registered_user',
                    is_verified INTEGER NOT NULL DEFAULT 0
                    )''')
    conn.close()
