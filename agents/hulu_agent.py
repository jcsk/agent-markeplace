from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hulu/recommend', methods=['POST'])
def hulu_recommend():
    data = request.json
    enriched_request = data.get('enriched_request')
    watched_titles = set(data.get('watched_titles', []))

    # Mock hulu movie database
    hulu_movies = [
        {"title": "Interstellar222", "genres": ["Sci-Fi", "Adventure"]},
        {"title": "The Dark Knight222", "genres": ["Action", "Thriller"]},
        {"title": "The Notebook2222", "genres": ["Romance", "Drama"]}
    ]

    # Filter out already-watched movies
    recommendations = [movie for movie in hulu_movies if movie['title'] not in watched_titles]

    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(port=5004, debug=True)
