# imports are like toolboxes :)
from flask import Flask,render_template,request,redirect,url_for
import requests
import pprint # useful for decoding big files!
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

# 1. Recieve: this is what the user will input in the search bar, we are recieving it
    searchValue = request.args["search_criteria"]
    app.logger.info(searchValue)

# 2. Build: we built a URL using the data received and used a f-string to glue to user's name to the Nasa URL
    nasaURL = f"https://images-api.nasa.gov/search?q={searchValue}&media_type=image"
    app.logger.info(nasaURL)

# 3. Fetch: acting as client, we ask NASA for the URL we created, we recieved raw json text so .json() translates it into a readable structure, nice   
    response = requests.get(nasaURL)
    data = response.json()
    app.logger.info(data['collection']['items'])

# 4. digging / accessing items to get a better understanding of the structure
    listOfItems = data['collection']['items']
    app.logger.info(listOfItems[0])

# 5. digging even more to access a single item/search result
    singleItem = data['collection']['items'][0]
    pprint.pp(singleItem) #discovered this to make the file more readable / pretty print

# 6. digging deeper again to access image link and image description in the json file from NASA
    imgFromNasa = singleItem['links'][0]['href']
    app.logger.info(imgFromNasa)
    description = singleItem['data'][0]['description']
    app.logger.info(description)

# 7. Sabine's line to clean up spaces for multi word searches   
    imgFromNasa = imgFromNasa.replace(' ', '%20') #clean up

# 8. This will render the same template as the t1 route with these 3 elements carried through. Also Sabine's code
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

# 1. Same as steps 1-3 in T1
    searchValue = request.args["search_criteria_adv"]
    nasaURL = f"https://images-api.nasa.gov/search?q={searchValue}&media_type=image"
    response = requests.get(nasaURL)
    data = response.json()

# 2. A list that we will later iterate through, no [0] this time since we'll have many images
    listOfItems = data['collection']['items']

# 3. Creating an empty list in which all the image links will be stored
    encodedImageLinks = []

# 4. For each item in our listOfItems list we find the image link, clean it up, store it in singleImage and add it to the encodedImageLinks
    for item in listOfItems:
        singleImage = item['links'][0]['href']
        singleImage = singleImage.replace(' ', '%20')
        encodedImageLinks.append(singleImage)

# 5. Sabine's line: this will render the same template as the t2 route with these 2 elements carried through.
    return render_template("t2.html",images=encodedImageLinks)
    # pass
#*************************************************

#run
app.run(debug=True)