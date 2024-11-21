from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# Dummy data for tracks and artists
artists = [
    {"name": "Eminem", "image": "static/images/eminem.jpg"},
    {"name": "Metro Boomin", "image": "static/images/metroboomin.jpg"},
    {"name": "Metro Boomin", "image": "static/images/metroboomin.jpg"},

]

# Tracks data (ensure files are in the static directory under songs/)
tracks = [
    {"id": 1, "title": "Eminem - Lose Yourself", "file": "songs/Eminem - Lose Yourself [HD].mp3", "image": "images/images6.jpg"},
    {"id": 2, "title": "Eminem - Somebody Save Me (feat. Jelly Roll)", "file": "songs/Eminem - Somebody Save Me (feat. Jelly Roll) [Official Music Video].mp3", "image": "images/images 1.jpeg"},
    {"id": 3, "title": "Future, Metro Boomin - Like That", "file": "songs/Future, Metro Boomin - Like That (Official Audio).mp3", "image": "images/images22.jpg"},
    {"id": 4, "title": "Justin Bieber - Intentions ft. Quavo", "file": "songs/Justin Bieber - Intentions (Official Video (Short Version)) ft. Quavo.mp3", "image": "images/images7.jpg"},
    {"id": 5, "title": "Kendrick Lamar - Not Like Us", "file": "songs/Kendrick Lamar - Not Like Us.mp3", "image": "images/images8.jpeg"},
    {"id": 6, "title": "Kendrick Lamar Euphoria (Drake Diss) (Lyrics).mp3", "file": "songs/Kendrick Lamar Euphoria (Drake Diss) (Lyrics).mp3", "image": "images/images9.png"},
    {"id": 7, "title": "LANY - Malibu Nights", "file": "songs/LANY - Malibu Nights (Official Music Video).mp3", "image": "images/images10.jpg"},
    {"id": 8, "title": "The Emptiness Machine.mp3", "file": "songs/The Emptiness Machine.mp3", "image": "images/images3.jpeg"},
    {"id": 9, "title": "Travis Scott - MO CITY FLEXOLOGIST", "file": "songs/LANY - Malibu Nights (Official Music Video).mp3", "image": "images/images10.jpg"},
    {"id": 10, "title": "Travis_Scott_Fein_ft.Playboi Carti .mp3", "file": "songs/Travis_Scott_Fein_ft.Playboi Carti .mp3", "image": "images/images5.jpg"},
]

# Routes
@app.route('/')
def home():
    return render_template("home.html", tracks=tracks)

@app.route('/musics')
def musics():
    return render_template("musics.html", tracks=tracks)

@app.route('/artist')
def artist():
    return render_template("artist.html", artists=artists)

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

# API route to fetch track data dynamically
@app.route('/api/tracks', methods=['GET'])
def get_tracks():
    return jsonify(tracks)

if __name__ == "__main__":
    app.run(debug=True)
