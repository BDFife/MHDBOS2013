#!/usr/bin/python

import os
from flask import Flask, request, redirect, url_for, render_template
from werkzeug import secure_filename
import artists


UPLOAD_FOLDER = '~/Projects/Collector'
ALLOWED_EXTENSIONS = set(['xml'])

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
       	mybuffer = file.readlines()
        return str(mybuffer)
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''
	
"""
@app.route("/")
def check_template():
	return render_template("index.html")
"""

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port, debug=True)
