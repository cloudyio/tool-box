from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from pytube import YouTube
import os

app = Flask(__name__)
CORS(app)

@app.route('/download', methods=['POST', 'OPTIONS'])
def download_video():
    if request.method == 'OPTIONS':
        response = jsonify({'message': 'Preflight request allowed.'})
        response.headers.add('Access-Control-Allow-Methods', 'POST')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        return response
    
    video_link = request.json.get('video_link')
    resolution = request.json.get('resolution')
    
    try:
        video = YouTube(video_link)
        
        # Find the stream with the specified resolution
        stream = None
        for strm in video.streams:
            if strm.resolution == resolution:
                stream = strm
                break
        
        if stream is None:
            response = {'error': f'No stream found for resolution: {resolution}'}
            return jsonify(response), 400
        
        # Get the video ID
        video_id = video.video_id
        
        # Construct the file path with the video ID and mp4 extension
        file_path = os.path.join('./downloads', f'{video_id}.mp4')
        
        # Download the video using the video ID as the filename with the .mp4 extension
        stream.download('./downloads/', filename=video_id + '.mp4')
        
        response = {'file_path': file_path}
        return jsonify(response)
    except Exception as e:
        response = {'error': str(e)}
        return jsonify(response), 400

@app.route('/downloads/<path:filename>', methods=['GET'])
def serve_video(filename):
    directory = os.path.join(app.root_path, 'downloads')
    return send_from_directory(directory, filename)

if __name__ == '__main__':
    app.run()
