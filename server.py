""" Server for LocalSound app """

from flask import Flask, render_template, request
import crud

app = Flask(__name__)


## INSERT ROUTES HERE ##
# JSON zipcode/city - 


@app.route('/')
def welcome_home():
    """ Landing page """

    return render_template("home.html")

@app.route('/search')
def find_scene():
    """ Search for artists based on locations"""


@app.route('/playlist')
def heres_loc_artist():
    """ Search for artists based on locations"""

# Where the API recommendation is


@app.route('/artistinfo')
def more_on_the_band():
    """ Search for artists based on locations"""
# API for artist information
# Bandcamp link etc
    return render_template("artistinfo")


@app.route('/sign-up')
def get_dat_user():
    if user == person:
        make_new_user()
    else:
        make_new_artist()
        Or redirects?????


if __name__ == "__main__":
    #DebugToolbarExtension(app)
    app.run(host = "0.0.0.0", debug = True)