""" Server for LocalSound app """

from model import connect_to_db
from flask import Flask, render_template, request
from crud import get_artists, spotify_info
import os
import requests


app = Flask(__name__)


@app.route('/', methods=['GET','POST']) #The GET is for when / is first loaded b/c not getting a post
def welcome_home():
    """ Landing page """

    if request.method == 'POST':                # Will only hit here when the post request was made
        city = request.form.get('city')
        state = request.form.get('state')

        rec_list = get_artists(city, state) 

        playlist = spotify_info(rec_list)

        # payload = []
        return render_template("home.html", playlist=playlist)


    return render_template("home.html")

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
