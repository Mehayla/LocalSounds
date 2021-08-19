""" CRUD file for the LocalSound project """

from model import db, User, Artist, Location, connect_to_db


###  GAME PLAN   ###

# create_location function will populate the location table
# edit create_artist to check if a location exist then add it under the location id
# edit creat_user to check if a location exist then add it under the location id as a Forigne key
# Call these functions in SEED


def create_user(name, password, city, state):
    """ Adds a new user to the user table"""

    if User.query.filter(User.u_name == name): #This returns a boolean T/F
        return f"{name} already exits. Now redirecting to sign-up"
    else:
        if locations.query.filter(Location.city == city):  #Checks to see if the city is already in db
            loc_id = Location.query.filter_by(city = city, state = state) # gets the PK from location db 
            new_user = User(u_name = name, u_password = password, loc_id = location_id) # Is this still a FK???
            db.session.add(new_user)
            db.session.commit()
            return new_user
        else:
            loc_id = Location.query.filter_by(state = state) #Does mean I'd need state codes?
            new_user = User(u_name = name, u_password = password, loc_id = location_id) # Is this still a FK???
            db.session.add(new_user)
            db.session.commit()


def create_artist(artist_name, artist_URI, city, state):
    """ Adds a new artist to the artist table"""

    # current_artist = db.session.query(User.u_name).all()

    # if current_artist.filter(Artist.artist_name == artist_name):
    #     return f"You're already in our database silly."
    # else:

    #     if locations.query.filter(Location.city == city):  #What if city is NULLLL?
    #         loc_id = Location.query.filter_by(city = city, state = state) # gets the PK from location db 
    #         new_artist = Artist(artist_name = artist_name, artist_URI = artist_URI, location_id = loc_id)
    #         db.session.add(new_artist)
    #         db.session.commit()
    #         return new_artist

        # else:        # Creates a new artist and a new location OR SHOULD I call the other function?
        #     new_location = Location(city = city, state = state)
        #     db.session.add(new_location)
        #     db.session.commit()

        #     loc_id = Location.query.filter_by(state = state)
        #     new_artist = Artist(artist_name = artist_name, artist_URI = artist_URI, location_id = loc_id)
        #     db.session.add(new_user)
        #     db.session.commit()
        #     return new_location new_artist


def create_location(state, city):
    """ Adds a new location to the DB"""

    # This should be able to take in a location 2 ways.
    # 1. When the csv is loaded into the application via seed
    # 2. When a user or artist inputs a location that is not currently in the db

    state = state.lower()
    city = city.lower()

    new_location = Location(state = state, city = city)
    db.session.add(new_location)
    db.session.commit()
    return new_location 


def get_artist():
    """ Gets all artists in a particular location """
# Use a join function ??? 


if __name__ == "__main__":
    from server import app
    connect_to_db(app)
