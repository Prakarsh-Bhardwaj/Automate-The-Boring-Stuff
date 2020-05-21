import json , pprint
import requests

url = "https://api.darksky.net/forecast/****************/26.9124,%2075.7873"
response = requests.get(url)
response.raise_for_status()
weather = json.loads(response.text)
print("Current weather for Jaipur is " + weather["currently"]["summary"])
print("Weather today: " + weather["hourly"]["summary"])
print("Predicted weather for the week: " + weather["daily"]["summary"])

