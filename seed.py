""" Seeding my localsound db with data """

from model import db, User, Artist, Location, connect_to_db

def populate_musicians():
    """ Load musician info from dataset into db """

    with open("xristosk-bandcamp_artists-2021-04.csv") as artist_data:
        for i, row in enumerate(artist_data):
            name = row[0]
            URI = row[1]
            city = row[4].split(',')
            state = row[4] #This needs to be split for city and state

            # create_location()
            # create_artist()

            # db.session.add(Artist(*row.rstrip().split("????")))
    #     print("{i} musicains have been added".format(i=i)
    # db.session.commit()



if __name__ == '__main__':
    from server import app
    connect_to_db(app)
    db.create_all()

    get_musicians()