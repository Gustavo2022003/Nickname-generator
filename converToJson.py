import json


def convertToJson(lista):
    lista_json = json.dumps(lista)
    with open("nicknames.json", "w") as arquivo:
        arquivo.write(lista_json)
