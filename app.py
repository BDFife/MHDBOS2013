#!/usr/bin/python

import os
from flask import Flask, request, redirect, url_for, render_template
from artists import extract_artists
from discographies import discography_filter
from discographies import get_missing_albums
from potpourri import get_relevant_awards, spektor_guests, progress_on_award

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    # The POST code gets called when a file (iTunes XML)
    # is uploaded.
    if request.method == 'POST':
        file = request.files['file']
        data_struct = extract_artists(file)
        # Attempt to show missing albums from user catalog for filters
        return str(progress_on_award(data_struct, spektor_guests))
        # Shows potpourri filters matching user catalog
        #return str(get_relevant_awards(data_struct))
        # Shows albums missing from matched "discography list"
        #return str(get_missing_albums(data_struct))
        # Returns matches between iTunes library and "discography" list
        #return str(discography_filter(data_struct))
        # Returns the structured data in JSON format
        #return str(data_struct)
    # Otherwise the 'home page' is shown that prompts the
    # user to upload their iTunes XML file. 
    else:
        return render_template("index.html")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port, debug=True)
