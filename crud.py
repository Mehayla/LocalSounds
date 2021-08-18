""" CRUD file for the LocalSound project """

import model 

# Do this in a SEED.PY file ???
# def populate_locations():
#     """ Something that will take the csv read it and populae my db """

# Add to Queue ask about location_id to user and artist when creating an new user/artist
# Query db for locations

def make_new_user(name, password, city):
    """ Adds a new user to the user table"""

    current_users = db.session.query(User.u_name).all()
    locations = db.session.query(Location.zipcode) ### What is best? City? ZipCode? ###
    
    if current_users.filter(User.u_name == name): #This returns a boolean T/F
        return f"{name} already exists please sign in." # Should this redirect?
    else:
        new_user = User(u_name = name, u_password = password, location = city)
        if 
        db.session.add(new_user)
        db.session.commit()
        return new_user


def make_new_artist(artist_name, artist_URI, city):
    """ Adds a new artist to the artist table"""

    current_artist = db.session.query(User.u_name).all()

    if current_artist.filter(Artist.artist_name = artist_name):
        return f"You're already in our database silly."
    else:
        new_artist = Artist(artist_name = artist_name, artist_URI = artist_URI, location = city)
        db.session.add(new_artist)
        db.session.commit()
        return new_artist


def make_new_location(state, city, zipcode):
    """ Adds a new location to the DB"""

    # This should be able to take in a location 2 ways.
    # 1. When the csv is loaded into the application via seed
    # 2. When a user or artist inputs a location that is not currently in the db

    new_location = Location(state = state, city = city, zipcode = zipcode)
    db.session.add(new_location)
    db.session.commit()
    return new_location 


if __name__ == "__main__":
    from server import app
    connect_to_db(app)
