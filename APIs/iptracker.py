import json , sys , pprint
import requests

if len(sys.argv) < 2:
    print("Usage: python ipstack.py <ip address>")
    sys.exit()

url = "http://api.ipstack.com/{}?access_key=your_key".format(sys.argv[1])
response = requests.get(url)
response.raise_for_status()
ipdata = json.loads(response.text)
try:
    print("This IP has been traced to " + ipdata["city"] + "," + ipdata["region_name"] + "," + ipdata["country_name"] + ".")
    print("Zip code is: " + ipdata["zip"] + ".")
except:
    print("Input IP doesn't exist.")

#	h_TM_WN112yJMhywQJWwjGovULE