""" Seeding my localsound db with data """

from model import db, User, Artist, Location, connect_to_db
from crud import create_user, create_artist, create_location
import os
import re

# os.system('dropdb localsound')
# os.system('createdb localsound')


def set_state_codes():
    """ This adds 253 default locations that are US states and countires"""

    with open("State_country codes.csv") as state_country_data:
        for i, row in enumerate(state_country_data):
                state = row.lower().strip('\n')
                create_location(None, state)



def populate_musicians_loc():
    """ Load musician location from dataset into db """
    
    with open("xristosk-bandcamp_artists-2021-04.csv") as artist_data:
        for i, row in enumerate(artist_data, start = 1):
            loc_serch = re.findall(r"\d{4,7},\"(\w+?\s*\w+),?(\D+?\s*\w+)?$", row) #Coping group 1 for group 2 = None for all of them??
            # loc_city = loc_serch.group(1)
            # loc_state = loc_serch.group(2) #PYTHON HATES GROUPING
            print(loc_serch)
            if i > 50:
                break 

            # r"(\d{5,7}),\"(\w+?,\s*\w+)" works for one word cities

            # if state == None
                # new_location = create_location(None, loc_city)              #DO LOCATIONS FIRST
                # db.session.add(new_location)
                # db.session.commit()
            # else:
                # new_location = create_location(loc_city, loc_state)
                # db.session.add(new_location)
                # db.session.commit()


def populate_artists():
    """ Load musican info from csv file"""

    with open("xristosk-bandcamp_artists-2021-04.csv") as artist_data:
        for i, row in enumerate(artist_data, start = 1):
            # loc_serch = re.search(r"(\w+),\b", row)             # Give a match object?
            # print(loc_serch)
            if i > 30:
                break 

            # name = row[0]
            # URI = row[1]                            #Maybe add another table for genere? or just the Spotify API for dat
            # new_artist = create_artist()
            # db.session.add(new_artist)
            # db.session.commit()
    # print("{i} musicains have been added".format(i=i)




if __name__ == '__main__':
    from server import app
    connect_to_db(app)
    db.create_all()

    # get_musicians()