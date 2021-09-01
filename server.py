""" Server for LocalSound app """

from model import connect_to_db
from flask import Flask, render_template, request
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
from crud import get_artists
import spotipy
import os
import requests


app = Flask(__name__)

API_KEY = os.environ['SPOTIPY_CLIENT_SECRET']
SPOTIPY_CLIENT_ID = os.environ['SPOTIPY_CLIENT_ID']
auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)



@app.route('/', methods=['GET','POST']) #The GET is for when / is first loaded b/c not getting a post
def welcome_home():
    """ Landing page """

    city = request.form.get('city')
    state = request.form.get('state')

    rec_list = get_artists(city, state) #It is waiting to get this when first loading soooo . . . .
    # spotify_id = []
    
    # for artist in rec_list:                             
    #     artist_info = sp.search(artist, limit = 1, type = 'artist')
    #     artist_id = artist_info['artists']['items'][0]['id']
    #     spotify_id.append(artist_id)
    
    #     artist_tracks = sp.artist_top_tracks(artist_id)

    #     track_album_name = artist_tracks['tracks'][0]['album']['name']
    #     artist_name = artist_tracks['tracks'][0]['artists'][0]['name']
    #     artist_uri = artist_tracks['tracks'][0]['uri'] #WHAT is a URI used for?
    #     track_preview = artist_tracks['tracks'][0]['preview_url']
    #     track_name = artist_tracks['tracks'][0]['name']

    payload = []

    return render_template("home.html", rec_list=rec_list )

# @app.route('/location.json')
# def welcome_home():
#     """ The request handler ????? """


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
    connect_to_db(app)
    app.run(host = "0.0.0.0", debug = True)
    #DebugToolbarExtension(app)
