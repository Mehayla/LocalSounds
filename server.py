""" Server for LocalSound app """

from flask import Flask

app = Flask(__name__)


## INSERT ROUTES HERE ##


if __name__ = '__main__':
    #DebugToolbarExtension(app)
    app.run(host = "0.0.0.0", debug = True)