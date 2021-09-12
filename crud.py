""" CRUD file for the LocalSound project """

from model import db, User, Artist, Location, connect_to_db
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
import spotipy
import random
import os

API_KEY = os.environ['SPOTIPY_CLIENT_SECRET']
SPOTIPY_CLIENT_ID = os.environ['SPOTIPY_CLIENT_ID']
auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

# Need to make a password reset for artist - esp default artists

def create_user(name, password, city, state):
    """ Adds a new user to the user table"""

    if city == '' or city == None:
        city = None
    else:
        city = city.lower()
    state = state.lower()
    
    user = User.query.filter(User.u_name == name).one_or_none()                 #us.one_or_none() allows for exceptions when handling errors
    location = Location.query.filter(Location.city == city, Location.state == state).one_or_none()

    if user == None:  
        if location == None:                                                    #Checks if location doesn't exist
            state = Location.query.filter_by(state = state, city = None).one()  #If location doesn't exist yet, give them a state code 

            new_user = User(u_name = name, u_password = password, location_id = state.location_id)
            db.session.add(new_user)
            db.session.commit()
            return new_user
        else:
            loc_obj = Location.query.filter_by(city = city, state = state).one() # gets the PK from location db 
            new_user = User(u_name = name, u_password = password, location_id = loc_obj.location_id) 
            db.session.add(new_user)
            db.session.commit()
            return new_user
    else:
        return False



def create_artist(artist_name, artist_password, city, state, artist_URI, link_1, link_2):
    """ Adds a new artist to the artist table"""

    artist_name = artist_name.lower()
    state = state.lower()
    if city == '' or city == None:
        city = None
    else:
        city = city.lower()

    seed_status = False

    artist = Artist.query.filter(Artist.artist_name == artist_name).one_or_none()
    location = Location.query.filter(Location.city == city, Location.state == state).one_or_none()
    # ^^^^ Multiple rows were found when one or none was required ^^^^

    if artist == None:
        if location == None:        # See create_location for why this is here #When called in server call extra
            new_location = Location(city = city, state = state) #
            db.session.add(new_location)                        #
            db.session.commit()                                 #
            # A way to email users that a new band has joined from their town

            loc_obj = Location.query.filter_by(city = city, state = state).one()
            new_artist = Artist(artist_name = artist_name, artist_password = artist_password, seed_status = seed_status, location_id = loc_obj.location_id, artist_URI = artist_URI, link_1 = link_1, link_2 = link_2)
            db.session.add(new_artist)
            db.session.commit()
            return new_artist
        else:
            loc_obj = Location.query.filter_by(city = city, state = state).one() # gets the PK from location db 
            new_artist = Artist(artist_name = artist_name, artist_password = artist_password, seed_status = seed_status, location_id = loc_obj.location_id, artist_URI = artist_URI, link_1 = link_1, link_2 = link_2)
            db.session.add(new_artist)
            db.session.commit()
            return new_artist
    else:
        return False
       


def create_location(city, state):
    """ Adds a new location to the DB"""

    # This should be able to take in a location 2 ways.
    # 1. When the csv is loaded into the application via seed 
    # 2. When a user or artist inputs a location that is not currently in the db 3.0

    state = state.lower()
    if city == '' or city == None:
        city = None
    else:
        city = city.lower()

    location = Location.query.filter(Location.city == city, Location.state == state).one_or_none()

    if location == None:
        new_location = Location(state = state, city = city)
        db.session.add(new_location)
        db.session.commit()
        return new_location


def get_user_by_username(username):
    """gets the user """

    user = User.query.filter(User.u_name == username).one_or_none()
    return user

def get_artist_by_name(name):
    artist = Artist.query.filter(Artist.artist_name == name).one_or_none()
    return artist

    

def get_artists(city, state):
    """ Gets all artists in a particular location """

    city = city.lower()
    state = state.lower()
    rec_list = []
    count = 0

    loc_obj = Location.query.filter(Location.city == city, Location.state == state).first()
    if loc_obj is None:
        loc_obj = Location.query.filter(Location.city == None, Location.state == state).one()
        
    artists = Artist.query.filter(Artist.location_id == loc_obj.location_id).all()
    
    for artist in artists:
        rec_list.append(artist.artist_name)

    rec_lis = random.sample(rec_list, k=2) #Picks 50 random artists
    return rec_lis



def spotify_info(artists):
    """ This takes in a pre-selected artist list and returns a sorted dictionary """

    spotify_dic = {}
    count = 0

    for artist in artists:

        artist_info = sp.search(artist, limit = 1, type = 'artist')
        artist_items = artist_info['artists']['items']

        if len(artist_items) > 0:
            if artist == artist_items[0]['name'].lower():
                try:

                    spotify_dic[count] = {}
            
                    artist_tracks = sp.artist_top_tracks(artist_items[0]['id'])
                    spotify_dic[count]['artist_pic'] = artist_items[0]['images'][2]['url']  #Artist image how do I turn this into an image? src in HTML
                    spotify_dic[count]['artist_name'] = artist_tracks['tracks'][0]['artists'][0]['name']
                    spotify_dic[count]['track_name'] = artist_tracks['tracks'][0]['name']
                    spotify_dic[count]['album_name'] = artist_tracks['tracks'][0]['album']['name']
                    spotify_dic[count]['track_preview'] = artist_tracks['tracks'][0]['preview_url']
                    # big_pic = artist_items[0]['images'][0]            # USE THIS WITH ARTIST INFO

                    count += 1

                except:
                    pass

    return spotify_dic


if __name__ == "__main__":
    from server import app
    connect_to_db(app)

    # db.drop_all()
    # db.create_all()