import requests
import base64
import json

IMAGE_PATH = 'index.jfif'
SECRET_KEY = ''

with open(IMAGE_PATH, 'rb') as image_file:
    img_base64 = base64.b64encode(image_file.read())

url = 'https://api.openalpr.com/v2/recognize_bytes?recognize_vehicle=1&country=in&secret_key=%s' % (SECRET_KEY)
r = requests.post(url, data = img_base64)
pdata = json.loads(r.text)
print("The number plate of provided vehicle is " + pdata["results"][0]["plate"] + ".")
