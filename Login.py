import csv
import Main

def login(usuario, senha):
    with open("contas.csv", "r", encoding="utf-8") as arquivo:
        lista = list(csv.reader(arquivo, delimiter=','))
    for x in range (1, len(lista)):
        if lista[x][0]==usuario:
            if lista[x][1]==senha:
                return 0
    return 1


def registrar(usuario, senha, id):
    with open("contas.csv", "r", encoding="utf-8") as arquivo:
        lista = list(csv.reader(arquivo, delimiter=','))
    for x in range (1, len(lista)):
        if lista[x][0]==usuario:
            return 1
    dados=[]
    dados.append(usuario)
    dados.append(senha)
    dados.append(id)
    lista.append(dados)
    with open("contas.csv", "w", encoding="utf-8", newline="") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerows(lista)
        return 0

Main.menu_login()