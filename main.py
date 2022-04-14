 
import json

import math
 
# Opening JSON file
f = open('demoScreen.json')
 
# returns JSON object as
# a dictionary
data = json.load(f)
# Iterating through the json
# list
positions = []
item_goc = data[0]
pos_goc = data[0]["data"]["position"]
for i in data[1:]:
    pos = i['data']["position"]
    distance = math.sqrt((pos_goc["x"] - pos["x"]) ** 2 + (pos_goc["y"] - pos["y"]) ** 2)
    print("khoang cach tu button id %s den button id %s la: %f"  % (item_goc["id"], i["id"], distance))
#print(positions)
# Closing file
f.close()