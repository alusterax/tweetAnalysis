import json

def watsonKey():
    with open("Credentials\\Watson_PI.json") as readWatson:
        dadosWatson = json.load(readWatson)
        keyWatson = dadosWatson['apikey']
    return keyWatson
