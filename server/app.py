# Flask Backend
import os
import string
import random
import json
from flask import Flask, request, jsonify, redirect

app = Flask(__name__)
db_file = "url_shortener.json"

def initialize_database():
    if not os.path.exists(db_file):
        with open(db_file, "w") as f:
            json.dump({}, f)

# Function to generate a random short URL
def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for i in range(6))
    return short_url

# Endpoint to create a short URL
@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    long_url = data.get('long_url')

    if not long_url:
        return jsonify({'error': 'Invalid URL'}), 400

    with open(db_file, 'r+') as f:
        url_map = json.load(f)

        # Check if the long URL already exists in the database
        for short_url, url in url_map.items():
            if url == long_url:
                return jsonify({'short_url': f'http://cloudys.tech/{short_url}'})

        short_url = generate_short_url()
        url_map[short_url] = long_url

        f.seek(0)
        json.dump(url_map, f)
        f.truncate()

    return jsonify({'short_url': f'http://cloudys.tech/{short_url}'}), 201

# Endpoint to redirect to the original URL
@app.route('/<short_url>')
def redirect_to_original_url(short_url):
    with open(db_file, 'r') as f:
        url_map = json.load(f)

    long_url = url_map.get(short_url)
    if not long_url:
        return jsonify({'error': 'URL not found'}), 404

    return redirect(long_url, code=301)

if __name__ == '__main__':
    initialize_database()
    app.run()
