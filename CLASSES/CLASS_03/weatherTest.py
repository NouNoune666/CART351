#import the lib
import requests

# #city arg
# city = "Toronto" 

# # My API key 
# api_key = "7990e650e887a464b3834da415767392"

# # URL to get results with the city added
# url_with_city = "http://api.openweathermap.org/data/2.5/weather?q=" + city

# #url with the api key appeneded
# url_to_send = url_with_city + "&APPID=" + api_key 

# #make the request
# response = requests.get(url_to_send) 
# print(url_to_send) #check

# # get the response as json
# data = response.json()
# # print(data)
# # print(type(data))
# print(data.keys())

city = "Montreal"
api_key = "7990e650e887a464b3834da415767392"
bare_url = 'http://api.openweathermap.org/data/2.5/weather'
response = requests.get(bare_url , params={"q": city, "APPID":api_key })
data = response.json()
print(data["weather"])