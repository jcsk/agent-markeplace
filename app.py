from flask import Flask, request, jsonify, render_template, redirect, url_for
import sqlite3
from agents.entertainment_agent import EntertainmentAgent

# Initialize Flask app
app = Flask(__name__)

# Initialize EntertainmentAgent
entertainment_agent = EntertainmentAgent()

# Connect to SQLite Database
DATABASE = 'movies.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Route to view and add movies
@app.route('/movies', methods=['GET', 'POST'])
def movies():
    if request.method == 'POST':
        title = request.form['title']
        genre = request.form['genre']
        release_year = request.form['release_year']

        # Insert movie into the database
        conn = get_db_connection()
        conn.execute('INSERT INTO movies (title, genre, release_year) VALUES (?, ?, ?)',
                     (title, genre, release_year))
        conn.commit()
        conn.close()

        return redirect(url_for('movies'))

    # Retrieve movies from the database to display
    conn = get_db_connection()
    movies = conn.execute('SELECT * FROM movies').fetchall()
    conn.close()

    return render_template('movies.html', movies=movies)

# Recommendation route as before
@app.route('/entertainment/recommend', methods=['POST'])
def recommend():
    user_data = request.json
    recommendations = entertainment_agent.get_recommendations(user_data)
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(port=5001, debug=True)
