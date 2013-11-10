""" 
discographies.py

"""

discographies = {
    "James Taylor": ["James Taylor", 
                     "Sweet Baby James",
                     "Mud Slide Slim and the Blue Horizon",
                     "One Man Dog",
                     "Walking Man",
                     "Gorilla",
                     "In the Pocket",
                     "JT", 
                     "Flag",
                     "Dad Loves His Work",
                     "That's Why I'm Here", 
                     "Never Die Young",
                     "New Moon Shine", 
                     "Hourglass",
                     "October Road"],
    "The Beatles": ["Please Please Me",
                    "With the Beatles",
                    "A Hard Day's Night", 
                    "Beatles for Sale", 
                    "Help!",
                    "Rubber Soul",
                    "Revolver", 
                    "Sgt. Pepper's Lonely Hearts Club Band",
                    "Magical Mystery Tour",
                    "The Beatles",
                    "Yellow Submarine",
                    "Abbey Road",
                    "Let It Be"],
    # Pearl Jam entry is incomplete for now.
    "Pearl Jam": ["Ten",]
}


"""
This strips down the list of keys to the matches between discography and 
the user's iTunes library
"""
def discography_filter(itunes_data):
    filter_artists = discographies.keys()
    itunes_artists = itunes_data.keys()

    artist_list = set(filter_artists).intersection(set(itunes_artists))
    
    return list(artist_list)

def get_missing_albums(itunes_data):
    tracklist = {}

    artists = discography_filter(itunes_data)
    for artist in artists:
        owned_albums = itunes_data[artist].keys()
        # since we don't have tracks in discographies, this is
        # a list, not a dict, at this point. 
        total_albums = discographies[artist]

        missing_albums = list(set(total_albums).difference(set(owned_albums)))
        
        tracklist[artist] = { 'owned':owned_albums,
                              'missing':missing_albums }

    return tracklist




# To Add: 
# The Rolling Stones
# Led Zeppelin
# Nirvana
# Metallica
# Queen
# Pink Floyd
# U2
# Guns N' Roses
# Radiohead
# Pearl Jam
# Rush
