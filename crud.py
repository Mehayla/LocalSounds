""" CRUD file for the LocalSound project """

from model import db, User, Artist, Location, connect_to_db


###  GAME PLAN   ###

# create_location function will populate the location table
# edit create_artist to check if a location exist then add it under the location id
# edit creat_user to check if a location exist then add it under the location id as a Forigne key
# Call these functions in SEED

# Look up what one or none does


def create_user(name, password, city, state):
    """ Adds a new user to the user table"""

    user = User.query.filter(User.u_name == name).one_or_none() #us.one_or_none() - returns an error when nothing 
    location = User.query.filter(Location.city == city, state == state).one_or_none()

    if user == None:  
        if location == None:  #Checks if location doesn't exist
            state_id = Location.query.filter_by(state = state, city = None) #If location doesn't exist yet, give them a state code ALSO ADD A FLASH? ALSO UPDATE WHEN AN ARTIST ADDS A NEW LOCATION?
            new_user = User(u_name = name, u_password = password, location_id = state_id.location_id) # Is this still a FK???
            db.session.add(new_user)
            db.session.commit()
        else:
            loc_obj = Location.query.filter_by(city = city, state = state).one() # gets the PK from location db 
            new_user = User(u_name = name, u_password = password, location_id = loc_obj.location_id) # Is this still a FK???
            db.session.add(new_user)
            db.session.commit()
            return new_user
    else:
        return f"{name} already exits. Now redirecting to sign-up"



def create_artist(artist_name, artist_URI, city, state):
    """ Adds a new artist to the artist table"""

    # current_artist = db.session.query(User.u_name).all()
    artist = User.query.filter(Artist.artist_name == artist_name).one_or_none()
    location = User.query.filter(Location.city == city, state == state).one_or_none()

    if artist == None:
         if location == None:        # Creates a new artist and a new location OR SHOULD I call the other function? #SCALABILITY
            # new_location = Location(city = city, state = state)
            # db.session.add(new_location)
            # db.session.commit()

            loc_id = Location.query.filter_by(state = state)
            new_artist = Artist(artist_name = artist_name, artist_URI = artist_URI, location_id = loc_id)
            db.session.add(new_user)
            db.session.commit()
            return new_location, new_artist

        else:
            loc_id = Location.query.filter_by(city = city, state = state) # gets the PK from location db 
            new_artist = Artist(artist_name = artist_name, artist_URI = artist_URI, location_id = loc_id.location_id)
            db.session.add(new_artist)
            db.session.commit()
            return new_artist
    else:
        return f"You're already in our database silly."
       


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
