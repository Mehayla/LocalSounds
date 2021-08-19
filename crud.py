""" CRUD file for the LocalSound project """

import model 

###  GAME PLAN   ###

# create_location function will populate the location table
# edit create_artist to check if a location exist then add it under the location id
# edit creat_user to check if a location exist then add it under the location id as a Forigne key
# Call these functions in SEED

def create_user(name, password, city):
    """ Adds a new user to the user table"""

    current_users = db.session.query(User.u_name).all()
    locations = db.session.query(Location.city)
    
    if current_users.filter(User.u_name == name): #This returns a boolean T/F
        return f"{name} already exists please sign in." # Should this redirect?
    else:
        if locations.query.filter(Location.in_(city)):  #Checks to see if the city is already in db

        db.session.add(new_user)
        db.session.commit()
        return new_user


def create_artist(artist_name, artist_URI, city):
    """ Adds a new artist to the artist table"""

    current_artist = db.session.query(User.u_name).all()

    if current_artist.filter(Artist.artist_name = artist_name):
        return f"You're already in our database silly."
    else:
        new_artist = Artist(artist_name = artist_name, artist_URI = artist_URI, location = city)
        db.session.add(new_artist)
        db.session.commit()
        return new_artist


def create_location(state, city, zipcode):
    """ Adds a new location to the DB"""

    # This should be able to take in a location 2 ways.
    # 1. When the csv is loaded into the application via seed
    # 2. When a user or artist inputs a location that is not currently in the db

    new_location = Location(state = state, city = city, zipcode = zipcode)
    db.session.add(new_location)
    db.session.commit()
    return new_location 

# def get_artist():
#     """ Gets all artists in a particular location """


if __name__ == "__main__":
    from server import app
    connect_to_db(app)
