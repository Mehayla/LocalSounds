""" Seeding my localsound db with data """

from model import db, User, Artist, Location, connect_to_db
from crud import create_user, create_artist, create_location
import pandas as pd
import os
import re

# os.system('dropdb localsound')
# os.system('createdb localsound')

# YOU HAVE TO RUN THESE FUNCTIONS IN THIS EXACT ORDER!



def set_state_codes():
    """ This adds 253 default locations that are US states and countires"""

    with open("State_country codes.csv") as state_country_data:
        for i, row in enumerate(state_country_data):
                state = row.lower().strip('\n')
                create_location(None, state)



def populate_musicians_loc():
    """ Load musician location from dataset into db """

    artist_data = pd.read_csv("xristosk-bandcamp_artists-2021-04.csv")

    for i, row in artist_data.iterrows(): #What is I just pull everything from the csv?
        location = row['location'].split(',')
        try:
            city = location[0]
            state = location[1].strip()         #strip the sapce in front & end of state string
            create_location(city, state)
        except:
            city = None
            state = location[0]
            create_location(city, state)


def populate_artists():
    """ Load musican info from csv file"""

    artist_data = pd.read_csv("xristosk-bandcamp_artists-2021-04.csv",converters={'artist_name':str})

    for i, row in artist_data.iterrows():
        name = row['artist_name']
        url = row['bc_url']
        location = row['location'].split(',')
        password = 'potato'                     # I know there's a better way to do this lol
        try:
            city = location[0].strip()
            state = location[1].strip()         #strip the sapce in front & end of state string
            create_artist(name, password, url, city, state)
        except:
            city = None
            state = location[0].strip()
            create_artist(name, password, url, city, state)

              #Maybe add another table for genere? or just the Spotify API for dat




if __name__ == '__main__':
    from server import app
    connect_to_db(app)
    db.create_all()

    # get_musicians()