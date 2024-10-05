import sqlite3

def init_db():
    conn = sqlite3.connect('movies.db')
    c = conn.cursor()

    # Create movies table if it doesn't already exist
    c.execute('''
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        genre TEXT,
        release_year INTEGER
    )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
