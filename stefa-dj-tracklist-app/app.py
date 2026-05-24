import os
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/search')
def search():
    query = request.args.get('q', '')
    if not query:
        return jsonify([])
    
    search_url = f"https://itunes.apple.com/search?term={query}&entity=song&limit=15&country=it"
    try:
        response = requests.get(search_url, timeout=5).json()
        results = []
        if 'results' in response:
            for item in response['results']:
                artwork_low = item.get('artworkUrl100', 'https://via.placeholder.com/150')
                artwork_high = artwork_low.replace('100x100bb', '400x400bb')
                
                results.append({
                    'title': item.get('trackName', 'Unknown Title'),
                    'artist': item.get('artistName', 'Unknown Artist'),
                    'album': item.get('collectionName', 'Single'),
                    'artwork': artwork_high
                })
        return jsonify(results)
    except Exception as e:
        print(f"Errore API Apple: {e}")
        return jsonify([])

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5001)
