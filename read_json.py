import json

def dataP():
    try:
        caminho = input()
        file = open(caminho, "rt", encoding="utf-8")
        json_data = file.read()
        data = json.loads(json_data)
        print(data)
        file.close()
    except:
        print("Ocurreu um erro! ")
    finally:
        print("Processo concluido! ")

dataP()