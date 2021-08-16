""" CRUD file for the LocalSound project """

import model 

# def populate_locations():
#     """ Something that will take the csv read it and populae my db """
# Do this in a SEED.PY file ???

def make_new_user(name, password):
    """ Adds a new user to the user table"""

    new_user = User(u_name = name, u_password = password)
    return new_user


def make_new_artist(stagename, bandcamplink):
    """ Adds a new artist to the artist table"""

    new_artist = Artist(stagename = artist_name, bandcamplink = artist_URI)
    return new_artist


def make_new_location(state, city, zipcode):
    """ Adds a new location to the DB"""

    new_location = Locations(state = state, city = city, zipcode = zipcode)
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
