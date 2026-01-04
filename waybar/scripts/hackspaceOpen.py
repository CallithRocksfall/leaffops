import datetime
import json
import requests

icon_color = "#8c6aa8"
ip_address = 'https://club.entropia.de/spaceapi' 

server_status = requests.get(ip_address).json()['state']['open']
if(server_status):
    print(json.dumps({"text": "<span color='" + icon_color + "'>" + "" + "</span>"}))
else:
    print(json.dumps({"text": "<span color ='" + icon_color + "'>" + "" + "</span>"}))
