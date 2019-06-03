import json

def save(content):
    with open("content.json",'w') as saida:
        json.dump (content,saida)

def load():
    with open("content.json") as contentJson:
        dadosContent = json.load(contentJson)
    return dadosContent
