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
        playlist = spotify_info(rec_list)       #Playlist is a dictionary #TO-DO: use cases for missing information

        column_headers = ['Name','Track','Album','Preview']

        return render_template("home.html", playlist=playlist, column_headers=column_headers)

    return render_template("home.html")


@app.route('/artistinfo')
def more_on_the_band():
    """ Search for artists based on locations"""
    # API for artist information
    # Bandcamp link etc
    return render_template("artistinfo.html")


@app.route('/sign-up', methods=['GET'])
def get_dat_user():
    # selection = request.form.get('user_type')

    # username = request.form.get('username')
    # password = request.form.get('password')
    # city = request.form.get('city')
    # state = request.form.get('state')

    # create_user(username, password, city, state)

    # return render_template("sign-up.html")
    pass

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host = "0.0.0.0", debug = True)
    #DebugToolbarExtension(app)
