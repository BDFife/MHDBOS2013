"""
potpourri.py

a delightful mix of fun matching filters for music and stuff
"""


star_trek_sings = {
    "award_name":"In space, no-one can hear you sing",
    "music": {
        "Leonard Nimoy": ["Leonard Nimoy Presents Mr. Spock's Music \
                           from Outer Space",
                          "Two Sides of Leonard Nimoy",
                          "The Way I Feel",
                          "The Touch of Leonard Nimoy",
                          "The New World of Leonard Nimoy"],
        "William Shatner": ["The Transformed Man",
                            "Has Been",
                            "Seeking Major Tom"],
        "Brent Spiner": ["Ol' Yellow Eyes Is Back"],
        "Nichelle Nichols": ["Down to Earth",
                             "Out of This World"] }
}

spektor_guests = {
    "award_name":"Albums where Regina Spektor has one or more \
                featured tracks",
    "music": { 
        "Anders Griffen": ["All Over the Place",
                           "Ox"],
        "Kimya Dawson": ["Hidden Vagenda"],
        "The Strokes": ["Reptilia"],
        "Jenny Owen Youngs":["Batten the Hatches"],
        "Ben Folds":["Way To Normal"],
        "Joshua Bell":["At Home with Friends"],
        "Nickel Eye":["The Time of the Assassins"] }
}

vampires = {
    
   "award_name":"References to Vampires",
   "music": {
        "The Mountain Goats": ["All Eternals Deck"],
        "Bauhaus": ["Crackle: The Best Of Bauhaus"],
        "Allen Sherman": ["Dr. Demento Presents: Spooky Tunes & Scary Melodies"]}
}

potpourri_filters = [star_trek_sings, spektor_guests, vampires]

def get_relevant_awards(itunes_data):
    user_list = potpourri_filters
    for dict in potpourri_filters:
        relevant = False
        for artist in dict['music'].keys():
            if artist in itunes_data:
                relevant = True
        if not relevant:
            user_list.remove(dict)
    return user_list

def progress_on_award(itunes_data, award):
    albums_needed = {}
    albums_owned = {}
    for artist in award['music'].keys():
        if artist in itunes_data:
            for album in award['music'][artist]:
                # if the album is in the library
                if itunes_data[artist].get(album):
                    # add it to the 'owned' dict
                    if artist in albums_owned: 
                        albums_owned[artist].append(album)
                    else: 
                        albums_owned[artist] = [album,]
                else:
                    # add it to the 'needed' dict
                    if artist in albums_needed: 
                        albums_needed[artist].append(album)
                    else: 
                        albums_needed[artist] = [album,]

        else:
            albums_needed[artist] = award['music'][artist]
    return {'needed':albums_needed,
            'owned':albums_owned}

    