""" Model for my local sound app"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#ADD RELATIONSHIPS between classes

class User(db.Model):
    """ A user for the app """

    __tablename__ = "users"

    user_id = db.Column(db.Integer, 
                        primary_key = True,
                        autoincrement = True)
    u_name = db.Column(db.String(30), unique = True)
    u_password = db.Column(db.String(30))
    location_id = db.Column(db.Integer, db.ForeignKey('Locations.location_id'))

    def __repr__(self):
        return f"User {self.u_name} has been created! Their primary location in {self.location_id}"


class Artist(db.Model):
    """ The arts and location I am scrapping from a csv"""

    __tablename__ = "artist"

    artist_id = db.Column(db.Integer, 
                        primary_key = True,
                        autoincrement = True)
    artist_name = db.Column(db.String)
    artist_URI = db.Column(db.URL, unique = True) #Is URL even a column input type? Double chek this
    location_id = db.Column(db.Integer, db.ForeignKey('Locations.location_id'))

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
    zipcode = db.Column(db.Integer

    def __repr__(self):
        return f"Location {self.city}, {self.state} has been created."