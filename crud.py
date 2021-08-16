""" CRUD file for the LocalSound project """

import model 

# Do this in a SEED.PY file ???
# def populate_locations():
#     """ Something that will take the csv read it and populae my db """

# Add to Queue ask about location_id to user and artist when creating an new user/artist
# Query db for locations

def make_new_user(name, password, city):
    """ Adds a new user to the user table"""

    new_user = User(u_name = name, u_password = password, location = city)
    db.session.add(new_user)
    db.session.commit()
    return new_user


def make_new_artist(artist_name, artist_URI, city):
    """ Adds a new artist to the artist table"""

    new_artist = Artist(artist_name = artist_name, artist_URI = artist_URI, location = city)
    db.session.add(new_artist)
    db.session.commit()
    return new_artist


def make_new_location(state, city, zipcode):
    """ Adds a new location to the DB"""

    new_location = Location(state = state, city = city, zipcode = zipcode)
    db.session.add(new_location)
    db.session.commit()
    return new_location 

    # test_user = User(u_name = 'Tesy', u_password = 'Besty')
    # db.session.add(test_user)
    # db.session.commit()

    # test_artist = Artist(artist_name = 'Potato', artist_URI = 'http://TheSkinsss.com' )
    # db.session.add(test_artist)
    # db.session.commit()

    # test_location = Locations(state = 'California', city = 'San Francisco', zipcode = 94703)
    # db.session.add(test_location)
    # db.session.commit()

if __name__ == "__main__":
    from server import app
    connect_to_db(app)
