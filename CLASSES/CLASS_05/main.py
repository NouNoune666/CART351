from flask import Flask,render_template,request
app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template("index.html")
# # app.run(debug=True)


@app.route("/")
def index():

    return render_template("index.html",
                           user={"username":"sabine"},
                           passedDictionary={
                                            "fav_color":"fuscia", 
                                             "fav_veg":"cauliflower",
                                             "fav_fruit":"kiwi",
                                             "fav_animal":"toucan"
                                             },
                            imgPath = "../static/images/pineapple_2.jpg"          
                        )
  

@app.route('/testroute')
def testdef():
    return render_template("test.html")


@app.route("/pineappleC")
def pineAppleA():

    return render_template("pineapplechildA.html",
                           dataPassedA = "child A!" )

@app.route("/pineappleB")
def pineAppleB():

    return render_template("pineapplechildB.html",
                           passedImg = "../static/images/pineapple_2.jpg" )

@app.route("/inputPlant")
def addPlantData():
    return render_template("addPlantData.html") 

@app.route("/thankyou")
def thank_you():
    app.logger.info(request.args)
    return render_template("thankyou.html",owner_name = request.args["o_name"])


app.run(debug=True)