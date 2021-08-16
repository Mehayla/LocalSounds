""" Model for my local sound app"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """ A user for the app """

    __tablename__ = "users"

    user_id = db.Column(db.Integer, 
                        primary_key = True,
                        autoincrement = True)
    u_name = db.Column(db.String(30), unique = True)
    u_password = db.Column(db.String(30))
    location_id = db.Column(db.Integer, db.ForeignKey('Locations.location_id'))

    location = db.relationship("Locations", backref = "users")


    def __repr__(self):
        return f"User {self.u_name} has been created! Their primary location in {self.location_id}"


class Artist(db.Model):
    """ The arts and location I am scrapping from a csv"""

    __tablename__ = "artist"

    artist_id = db.Column(db.Integer, 
                        primary_key = True,
                        autoincrement = True)
    artist_name = db.Column(db.String)
    artist_URI = db.Column(db.String, unique = True) #Is URL even a column input type? Double chek this
    location_id = db.Column(db.Integer, db.ForeignKey('Locations.location_id'))

    location = db.relationship("Locations", backref = "artist")

    def __repr__(self):
        return f"{self.artist_name} is rockin! You can find them in {self.location_id}"


class Locations(db.Model):
    """ Location is everything and nothing in the digital age"""

    __tablename__ = "locations"

    location_id = db.Column(db.Integer, 
                        primary_key = True,
                        autoincrement = True)
    state = db.Column(db.String)
    city = db.Column(db.String)
    zipcode = db.Column(db.Integer)

    def __repr__(self):
        return f"Location {self.city}, {self.state} has been created."


def connect_to_db(flask_app, db_uri = 'localsound', echo = True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the Data Base")


if __name__ == "__main__":
    from server import app
    connect_to_db(app)

    test_user = User(u_name = 'Tesy', u_password = 'Besty')
    db.session.add(test_user)
    db.session.commit()

    test_artist = Artist(artist_name = 'Potato', artist_URI = 'http://TheSkinsss.com' )
    db.session.add(test_artist)
    db.session.commit()

    test_location = Locations(state = 'California', city = 'San Francisco', zipcode = 94703)
    db.session.add(test_location)
    db.session.commit()