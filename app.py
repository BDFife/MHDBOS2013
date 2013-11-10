#!/usr/bin/python

import os
from flask import Flask, request, redirect, url_for, render_template
from artists import extract_artists

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    # The POST code gets called when a file (iTunes XML)
    # is uploaded.
    if request.method == 'POST':
        file = request.files['file']
        data_struct = extract_artists(file)
        return str(data_struct)
    # Otherwise the 'home page' is shown that prompts the
    # user to upload their iTunes XML file. 
    else:
        return render_template("index.html")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port, debug=True)
