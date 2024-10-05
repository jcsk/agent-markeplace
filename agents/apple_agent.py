from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/apple/recommend', methods=['POST'])
def apple_recommend():
    data = request.json
    enriched_request = data.get('enriched_request')
    watched_titles = set(data.get('watched_titles', []))

    # Mock apple movie database
    apple_movies = [
        {"title": "Interstellar1", "genres": ["Sci-Fi", "Adventure"]},
        {"title": "The Dark Knight1", "genres": ["Action", "Thriller"]},
        {"title": "The Notebook1", "genres": ["Romance", "Drama"]}
    ]

    # Filter out already-watched movies
    recommendations = [movie for movie in apple_movies if movie['title'] not in watched_titles]

    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(port=5003, debug=True)
