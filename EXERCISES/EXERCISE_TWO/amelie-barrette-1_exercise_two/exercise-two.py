from flask import Flask,render_template,request,redirect,url_for
import requests
import pprint #*useful for decoding big files
app = Flask(__name__)


# the default route
@app.route("/")
def index():
      return render_template("index.html")

#*************************************************
#Task-1: GET REQUEST
@app.route("/t1")
def t1():
    return render_template("t1.html",have_results=False)
#*************************************************
@app.route("/getSearchCriteria")
def getSearchCriteria():

    searchValue = request.args["search_criteria"]
    app.logger.info(searchValue)
   
    nasaURL = f"https://images-api.nasa.gov/search?q={searchValue}&media_type=image"
    # app.logger.info(nasaURL)
   
    response = requests.get(nasaURL)
    data = response.json()
    # app.logger.info(data['collection']['items'])
   
    # listOfItems = data['collection']['items']
    # app.logger.info(listOfItems[0])
    singleItem = data['collection']['items'][0]
    pprint.pp(singleItem)
    imgFromNasa = singleItem['links'][0]['href']
    app.logger.info(imgFromNasa)
    description = singleItem['data'][0]['description']
    app.logger.info(description)
   
    imgFromNasa = imgFromNasa.replace(' ', '%20')
    return render_template("t1.html",
                              have_results = True,
                              description=description,
                              imgPath = imgFromNasa                                     
                           )

   
    

#*************************************************
# #Task-2: GET REQUEST
@app.route("/t2")
def t2():
    return render_template("t2.html")
#*************************************************
@app.route("/getSearchCriteria_adv")
def getSearchCriteria_adv():


    searchValue = request.args["search_criteria_adv"]
   
    nasaURL = f"https://images-api.nasa.gov/search?q={searchValue}&media_type=image"
   
    response = requests.get(nasaURL)
    data = response.json()

    listOfItems = data['collection']['items']

    encodedImageLinks = []

    for item in listOfItems:
        singleImage = item['links'][0]['href']
        singleImage = singleImage.replace(' ', '%20')
        encodedImageLinks.append(singleImage)



 
    return render_template("t2.html",images=encodedImageLinks)
    # pass
#*************************************************

#run
app.run(debug=True)