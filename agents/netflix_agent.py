from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/netflix/recommend', methods=['POST'])
def netflix_recommend():
    data = request.json
    enriched_request = data.get('enriched_request')
    watched_titles = set(data.get('watched_titles', []))

    # Mock Netflix movie database
    netflix_movies = [
        {"title": "Interstellar", "genres": ["Sci-Fi", "Adventure"]},
        {"title": "The Dark Knight", "genres": ["Action", "Thriller"]},
        {"title": "The Notebook", "genres": ["Romance", "Drama"]}
    ]

    # Filter out already-watched movies
    recommendations = [movie for movie in netflix_movies if movie['title'] not in watched_titles]

    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(port=5002, debug=True)
