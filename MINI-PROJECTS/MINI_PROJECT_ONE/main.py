import os
import json
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # 16 MB limit


@app.route('/')
def index():
    return render_template("index.html")

# we are not using this anymore but probably should later? idk
# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/thank_form_two",methods = ['POST'])
def thank_you_two():

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