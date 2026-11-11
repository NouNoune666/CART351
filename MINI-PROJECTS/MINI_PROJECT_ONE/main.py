import os
import json
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'gif'}


app = Flask(__name__)

# a route
@app.route('/')
def index():
    return render_template("index.html")

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # 16 MB limit

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/thank_form_two",methods = ['POST', 'GET'])
def thank_you_two():
    if request.method == 'POST':
        #key is the same as in the form :)
        uploadedfile = request.files['the_file']
        #save file to uploads folder
        uploadedfile.save(os.path.join(app.config['UPLOAD_FOLDER'], uploadedfile.filename))
        app.logger.info(uploadedfile.filename)

    return render_template("thankyou_form_rev.html", 
                           imgPath = uploadedfile.filename)
                        #    owner = request.form["o_name"]) 

# # another route
# @app.route('/p5BreakOut')
# def runpP5():
#     return render_template("p5_BreakOut.html")

# # for the get from p5
# @app.route('/getDataFromP5')
# def getDataFromP5():
#     #give back request.args
#     app.logger.info(request.args["id"])
#     app.logger.info(request.args["score"])
#          # Check if the file exists (can be a file or directory)
#     filePath="filesForP5/p5Data.json"
#     if os.path.exists(filePath):
#         jsonFile = open(filePath, "r+")
#         theList = json.load(jsonFile)
#         nameExists = False
#         oldData = ""
#         for el in theList:
#             if el["id"].upper() ==  request.args["id"].upper():
#                 nameExists = True
#                 oldData = el["score"]
#                 el["score"] = request.args["score"]
#                 break # This exits the loop entirely
#         #clear 
#         jsonFile.truncate(0)
#         jsonFile.close()
#         jsonFile_write = open(filePath, "w")
#         if nameExists ==True: 
#             json.dump(theList,  jsonFile_write, indent =4)
#             jsonFile_write.close()
#             return({"inFile":"true","score":oldData})
#         else:
#             theList.append(request.args)
#             json.dump(theList, jsonFile_write, indent =4)
#             jsonFile_write.close()
#             return({"inFile":"false"}) 

app.run(debug = True)