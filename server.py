""" Server for LocalSound app """

from model import connect_to_db
from flask import Flask, render_template, request, jsonify
import crud
import json

app = Flask(__name__)
app.secret_key = 'PoTaToS'
app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = True
API_KEY = os.environ['8f49c9011a8b4b078b1e282a748d0cf3']

# Is this the right place????? #
# When would I use get_artists?

@app.route('/')
def welcome_home():
    """ Landing page """

    # tracks = request.arg.get('tracks','')

    url = 'https://api.spotify.com/v1/tracks'
    payload = {'apikey', API_KEY}
    tracks = res.json()

    playlist = []

    return render_template("home.html", results=playlist)


@app.route('/playlist')
def heres_loc_artist():
    """ Search for artists based on locations"""
    music_json = open('music.json').read()
    music_dic = json.loads(music_json)
    print(music_dic)

# Where the API recommendation is



@app.route('/artistinfo')
def more_on_the_band():
    """ Search for artists based on locations"""
    # API for artist information
    # Bandcamp link etc
    return render_template("artistinfo.html")


@app.route('/sign-up')
def get_dat_user():
    # if user == person:
    #     make_new_user()
    # else:
    #     make_new_artist()
    #     Or redirects?????
    pass

if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug = True)
    #DebugToolbarExtension(app)
    connect_to_db(app)