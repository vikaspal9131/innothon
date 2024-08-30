import sqlite3

def create_table():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS uploads (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        gender TEXT,
        file_path TEXT,
        selected_ecg TEXT,
        drive_link TEXT
    );
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_table()
