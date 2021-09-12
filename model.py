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
    email = db.Column(db.String)
    location_id = db.Column(db.Integer, db.ForeignKey('locations.location_id'))
    site_theme = db.Column(db.String, nullable = True)

    def __repr__(self):
        return f"{self.u_name} is in {self.location_id} \n"



class Artist(db.Model):
    """ The arts and location I am scrapping from a csv"""

    __tablename__ = "artists"

    artist_id = db.Column(db.Integer, 
                        primary_key = True,
                        autoincrement = True)
    artist_name = db.Column(db.String, unique = True, nullable = False)
    artist_password = db.Column(db.String)
    seed_status = db.Column(db.String, nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey('locations.location_id'))
    artist_URI = db.Column(db.String, unique = True, nullable=True)
    link_1 = db.Column(db.String, unique = True, nullable = True)
    link_2 = db.Column(db.String, unique = True, nullable=True)

    def __repr__(self):
        return f"{self.artist_name} is rockin in {self.location_id}\n"



class Location(db.Model):
    """ Location is everything and nothing in the digital age"""

    __tablename__ = "locations"

    location_id = db.Column(db.Integer, 
                        primary_key = True,
                        autoincrement = True)
    city = db.Column(db.String)
    state = db.Column(db.String)

    artists = db.relationship('Artist', backref='location')
    users = db.relationship('User', backref='location')


    def __repr__(self):
        return f"Location {self.city}, {self.state} \n"


def connect_to_db(flask_app, db_uri="postgresql:///localsound", echo = True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the Data Base")


if __name__ == "__main__":
    from server import app
    connect_to_db(app)

    # db.drop_all()
    # db.create_all()

    # test_user = User(u_name = 'Tesy' , u_password = 'Besty')
    # db.session.add(test_user)
    # db.session.commit()

    # test_user2 = User(u_name = 'Patty' , u_password = 'Smith')
    # db.session.add(test_user2)
    # db.session.commit()

    # test_artist = Artist(artist_name = 'Potato', artist_URI = 'http://TheSkinsss.com' )
    # db.session.add(test_artist)
    # db.session.commit()

    # test_location = Location(state = 'california', city = 'san francisco')
    # db.session.add(test_location)
    # db.session.commit()

    # test_state_id = Location(state = 'ohio')
    # db.session.add(test_state_id)
    # db.session.commit()

    # test_state_id_2 = Location(state = 'california')
    # db.session.add(test_state_id_2)
    # db.session.commit()