#!/usr/bin/python

import os
from flask import Flask, request, redirect, url_for, render_template
from artists import extract_artists
from discographies import discography_filter
from discographies import get_missing_albums
from potpourri import get_relevant_awards, progress_on_award

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    # The POST code gets called when a file (iTunes XML)
    # is uploaded.
    if request.method == 'POST':
        iTunes_xml = request.files['file']
        
        # Note, this is the biggest performance hit when 
        # processing. Largely due to the plist parser
        iTunes_json = extract_artists(iTunes_xml)

        # Pull missing albums from user catalog via discography
        discography_gaps = get_missing_albums(iTunes_json)
        
        award_status = {}
        # Find relevant awards and make it awesome
        for award in get_relevant_awards(iTunes_xml):
            award_status[award['award_name']] = progress_on_award(iTunes_json, award)

        return render_template("results.html", itunes=iTunes_json, 
                                               discog=discography_gaps,
                                               awards=award_status)

    # Otherwise the 'home page' is shown that prompts the
    # user to upload their iTunes XML file. 
    else:
        return render_template("index.html")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port, debug=True)
