import json
import pprint
# reading the json file
jsonFile = open("files/test.json", "r")
data = json.load(jsonFile)
# pprint.pp(data)
# pprint.pp(type(data)) # a list
# pprint.pp(data)

# json_str = '{"name":"Sabs", "fav_col":"red", "fav_city":"montreal"}'
# pprint.pp(json_str)
# pprint.pp(type(json_str))
# data_2 = json.loads(json_str) 
# pprint.pp(data_2)
# pprint.pp(type(data_2))#converts to a dict

# data_toSave = {"name":"mandy", "fav_col":"blue", "fav_city":"winnipeg"}
# #convert dictionary to str
# jsonStr = json.dumps(data_toSave, indent=4)
# #open or create if non existent
# fileOpen = open("files/new_sample.json","w")
# fileOpen.write(jsonStr)

# jsonFile = open("files/new_sample_b.json", "w")
# data_toSave_2= {"name":"mandy", "fav_col":"blue", "fav_city":["list",3,4,True,"abc"]}
# json.dump(data_toSave_2,jsonFile, indent =4)


jsonFile = open("files/new_sample_b.json", "r+")
data = json.load(jsonFile)
pprint.pp(data['fav_city'])
pprint.pp(type(data['fav_city']))
#go to beginning of file
jsonFile.seek(0)
data['fav_city'].append("another element")
data["newKey"] = 1234
#output to the file
json.dump(data,jsonFile, indent =4)