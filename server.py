""" Server for LocalSound app """

from model import connect_to_db
from flask import Flask, render_template, request, redirect, jsonify
from crud import get_artists, spotify_info, create_user, create_artist, get_user_by_username, get_artist_by_name
import os
import requests


app = Flask(__name__)


@app.route('/', methods=['GET','POST'])         #The GET is for when / is first loaded b/c not getting a post
def welcome_home():
    """ Landing page """

    if request.method == 'POST':                # Will only hit here when the post request was made
        city = request.form.get('city')
        state = request.form.get('state')

        rec_list = get_artists(city, state) 
        playlist = spotify_info(rec_list)       #Playlist is a dictionary 

        column_headers = [' ','Name','Track','Album','Preview']

        return render_template("home.html", playlist=playlist, column_headers=column_headers)

    return render_template("home.html")


@app.route('/signup/user', methods=['GET','POST'])
def sign_up_user():
    """ Create a new user """


    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        city = request.form.get('city')
        state = request.form.get('state')

        user = get_user_by_username(username)
        
        if not user:
            create_user(username, password, city, state)
            return jsonify({'url':'/login', 'create-status': True})
        else:
            return jsonify({'url':'/signup/user', 'create-status': False})
    
    return render_template("signupuser.html")


@app.route('/signup/artist', methods=['GET','POST'])
def sign_up_artist():
    """ Create an artist through the website """

    if request.method == 'POST':
        aname = request.form.get('aname')
        password = request.form.get('password')
        city = request.form.get('city')
        state = request.form.get('state')
        bc_link = request.form.get('bc_link')
        link_1 = request.form.get('link_1')
        link_2 = request.form.get('link_2')


        artist = get_artist_by_name(aname)

        if not artist:
            create_artist(aname, password, city, state, bc_link, link_1, link_2)
            print('* * * * * * * * * * *')
            print(artist.seed_status)
            print('* * * * * * * * * * *')
            return jsonify({'url':'/login', 'create-status': True})
        else:
            print('* * * * * * * * * * *')
            print(artist.seed_status)
            print('* * * * * * * * * * *')
            return jsonify({'url':'/', 'create-status': False})
            # ^^^^ FIX THIS LATER^^^^
            # ^^^^This needs to update the password^^^
            # Use Seed status to update the password versus redirect to login

    return render_template("signupartist.html")


@app.route('/login')
def show_login():
    """ Show the login """

    return render_template("login.html")


# @app.route('/login', methods=['POST'])
# def process_login():
#     """ Process the login information"""

#     return redirect('/')

# @app.route('/artistinfo')
# def more_on_the_band():
#     """ Search for artists based on locations"""
#     # API for artist information
#     # Bandcamp link etc
#     return render_template("artistinfo.html")

@app.route('/about')
def show_about():
    """ Show the about page """

    return render_template("about.html")

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host = "0.0.0.0", debug = True)
    #DebugToolbarExtension(app)