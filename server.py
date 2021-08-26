""" Server for LocalSound app """

from flask import Flask
import crud

app = Flask(__name__)


## INSERT ROUTES HERE ##
# JSON zipcode/city - 

# @app.route('/sign-up')
# def user_type():
#     if user == person:
#         make_new_user()
#     else:
#         make_new_artist()
#         Or redirects?????


# @app.route('/')
# def find_scene():
#     """ Landing page """


# @app.route('/search')
# def find_scene():
#     """ Search for artists based on locations"""


# @app.route('/playlist')
# def find_scene():
#     """ Search for artists based on locations"""

# Where the API recommendation is


# @app.route('/artistinfo')
# def find_scene():
#     """ Search for artists based on locations"""
# API for artist information
# Bandcamp link etc


if __name__ == "__main__":
    #DebugToolbarExtension(app)
    app.run(host = "0.0.0.0", debug = True)