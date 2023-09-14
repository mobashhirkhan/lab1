import requests

#print(requests.__version__)

resp = requests.get("https://raw.githubusercontent.com/mobashhirkhan/lab1/master/lab1.py")

print(resp.text)
