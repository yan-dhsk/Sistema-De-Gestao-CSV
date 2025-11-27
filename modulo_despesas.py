import csv
import datetime


def excluir_despesa(id, despesas):
    with open("despesas.csv", "r", encoding="utf-8") as arquivo:
        lista=list(csv.reader(arquivo, delimiter=','))
    item=despesas[id-1]
    for i in range (1, len(lista)):    
        if item == lista[i]:
            lista.pop(i)
            with open("despesas.csv", "w", encoding="utf-8", newline="") as arquivo:
                escritor = csv.writer(arquivo)
                escritor.writerows(lista)
                return 1
    return 0




def registar_despesas(usuario, tipo, custo, nome):
    with open("despesas.csv", "r", encoding="utf-8") as arquivo:
        despesas = list(csv.reader(arquivo, delimiter=','))

    hora_atual = datetime.datetime.now()
    despesa_atual = []
    despesa_atual.append(hora_atual.strftime("%Y-%m-%d"))
    despesa_atual.append(tipo)
    despesa_atual.append(custo)
    despesa_atual.append(nome)
    despesa_atual.append(usuario)
    despesas.append(despesa_atual)
    with open("despesas.csv", "w", encoding="utf-8", newline="") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerows(despesas)
        return 1
    return 0


def ver_despesas(data):
    if data == 0:
        with open("despesas.csv", "r", encoding="utf-8") as arquivo:
            despesas=list(csv.reader(arquivo, delimiter=','))
        return despesas
    elif data != int and "-" not in data:
        with open("despesas.csv", "r", encoding="utf-8") as arquivo:
            despesas=list(csv.reader(arquivo, delimiter=','))
        contador=0
        lista=[]
        str(data).upper()
        for i in range (1,len(despesas)):
            str(despesas[i][4]).upper()
            if despesas[i][4]==data:
                lista.append(despesas[i])
                contador=+1
        if contador == 0:
            return 0
        else:
            return lista
    else:
        with open("despesas.csv", "r", encoding="utf-8") as arquivo:
            despesas=list(csv.reader(arquivo, delimiter=','))
        lista=[]
        contador=0
        for i in range (1,len(despesas)):
            if data in despesas[i][0]:
                lista.append(despesas[i])
                contador=+1
        if contador == 0:
            return 0
        else:
            return lista


def editar_despesas1(data):
    with open("despesas.csv", "r", encoding="utf-8") as arquivo:
        despesas=list(csv.reader(arquivo, delimiter=','))
    lista=[]
    contador=0
    for i in range (1,len(despesas)):
        if data in despesas[i][0]:
            lista.append(despesas[i])
            contador=+1
    if contador == 0:
        return 0
    else:
        return lista


def editar_despesas2(id, opcao, despesas, novo_valor):
    with open("despesas.csv", "r", encoding="utf-8") as arquivo:
        lista=list(csv.reader(arquivo, delimiter=','))
    item=despesas[id-1]
    for i in range (1, len(lista)):    
        if item == lista[i]:
            if opcao == 0 and isinstance(novo_valor, datetime.datetime):
                novo_valor = novo_valor.strftime("%Y-%m-%d")
            lista[i][opcao]=novo_valor
            with open("despesas.csv", "w", encoding="utf-8", newline="") as arquivo:
                escritor = csv.writer(arquivo)
                escritor.writerows(lista)
            return 1
    return 0
