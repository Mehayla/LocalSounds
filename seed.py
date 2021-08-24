""" Seeding my localsound db with data """

from model import db, User, Artist, Location, connect_to_db
from crud import create_user, create_artist, create_location
import os

os.system('dropdb localsound')
os.system('createdb localsound')


def set_state_codes():
    """ This adds 50 locations that are just states and 190 that are countires"""

    with open("State_country codes.csv") as state_country_data:
        for i, row in enumerate(state_country_data):
                state = row.lower().strip('\n')
                create_location(None, state)



def populate_musicians():
    """ Load musician info from dataset into db """
    
    with open("xristosk-bandcamp_artists-2021-04.csv") as artist_data:
        for i, row in enumerate(artist_data, start = 1):    
            if ',' not in row[4]:
                state = row[4]
                # new_location = create_location()              #DO LOCATIONS FIRST
                # db.session.add(new_location)
                # db.session.commit()
            else:
                city = row[4].split(',')[0]
                state = row[4].split(',')[1]
                # create_location()
                # db.session.add(new_location)
                # db.session.commit()

            name = row[0]
            URI = row[1]                            #Maybe add another table for genere? or just the Spotify API for dat
            # new_artist = create_artist()
            # db.session.add(new_artist)
            # db.session.commit()
    # print("{i} musicains have been added".format(i=i)




if __name__ == '__main__':
    from server import app
    connect_to_db(app)
    db.create_all()

    # get_musicians()