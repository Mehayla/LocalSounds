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


# @app.route('')
# def find_scene():
#     """ Search for artists based on locations"""

#     postalcode = request.args.get('zipcode', '')

#     url = ''

if __name__ == "__main__":
    #DebugToolbarExtension(app)
    app.run(host = "0.0.0.0", debug = True)