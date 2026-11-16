import os
import json
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename


app = Flask(__name__)


UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # 16 MB limit


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/catForm",methods = ['POST'])
def catForm():

    #key is the same as in the form :)
    uploadedfile = request.files['the_file']
    #save file to uploads folder
    uploadedfile.save(os.path.join(app.config['UPLOAD_FOLDER'],uploadedfile.filename)) # writes the bytes to disk
    app.logger.info(uploadedfile.filename)
    return json.dumps({"filename": uploadedfile.filename})


@app.route('/pastUploads')
def pastUploads():
# this will handle past uploaded images
    img_list = os.listdir(app.config['UPLOAD_FOLDER'])
    app.logger.info(img_list)
    return img_list

app.run(debug = True)