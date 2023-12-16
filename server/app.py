# Flask Backend
import os
import string
import random
import json
import pytube
from flask import Flask, request, jsonify, redirect, send_file, send_from_directory
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()
uri = os.getenv('MONGO_URI')

client = MongoClient(uri)
db = client['tools']
shortener = db['url']

app = Flask(__name__)
CORS(app)


@app.route('/s/<id>', methods=['GET'])
def urlshortener(id):
    if shortener.find_one({'short': id}):
        return redirect(shortener.find_one({'short': id})['url'])
    else:
        return jsonify({'success': False, 'message': 'URL not found'})
    
@app.route('/api/shorten', methods=['POST'])
def shorten():
    data = request.get_json()
    url = data['url']
    if shortener.find_one({'url': url}):
        return jsonify({'success': True, 'url': shortener.find_one({'url': url})['short']})
    else:
        short = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        shortener.insert_one({'url': url, 'short': short})
        return jsonify({'success': True, 'url': short})


@app.route('/api/download', methods=['POST'])
def download():
    data = request.get_json()
    url = data['url']
    print(url)
    print(url)
    yt = pytube.YouTube(url)
    video = yt.streams.first()

    if os.path.exists('./downloads/' + yt.video_id + '.mp4'):
        get_download = 'http://localhost:5000/api/download/' + yt.video_id
        return jsonify({'success': True, 'url': get_download})
    video.download('./downloads/', f"{yt.video_id}.mp4")
    get_download = 'http://localhost:5000/api/download/' + yt.video_id
    
    return jsonify({'success': True, 'url': get_download})
    
@app.route('/api/download/<id>', methods=['GET'])
def get_download(id):
    if os.path.exists('./downloads/' + id + '.mp4'):
        
        return send_from_directory('./downloads/', id + '.mp4')
    else:
        return jsonify({'success': False, 'message': 'File not found'})
    

    


if __name__ == '__main__':
    app.run()
