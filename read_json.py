import json

def dataP():
    try:
        caminho = input()
        file = open(caminho, "rt", encoding="utf-8")
        json_data = file.read()
        data = json.loads(json_data)
        print(data)
        file.close()
    except(FileNotFoundError):
        print("Ocurreu um erro! ")
    finally:
        print("Processo concluido! ")




dataP()

'''
def andar(posição_atual, posição_antiga ):

    posição_defenida= posição_atual + posição_antiga 
    print (posição_defenida)

andar(2, 3)'''