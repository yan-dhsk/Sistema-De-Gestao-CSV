import csv
import datetime


def registar_despesas(usuario, tipo, custo, nome):
    with open("despesas.csv", "r", encoding="utf-8") as arquivo:
        despesas=list(csv.reader(arquivo, delimiter=','))
    hora_atual=datetime.datetime.now()
    despeas_atual=[]
    despeas_atual.append(hora_atual.strftime("%Y-%m-%d %H:%M:%S"))
    despeas_atual.append(tipo)
    despeas_atual.append(custo)
    despeas_atual.append(nome)
    despeas_atual.append(usuario)
    despesas.append(despeas_atual)
    with open("despesas.csv", "w", encoding="utf-8", newline="") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerows(despesas)


def ver_despesas(data):
    if data == 0:
        with open("despesas.csv", "r", encoding="utf-8") as arquivo:
            despesas=list(csv.reader(arquivo, delimiter=','))
        return despesas
    elif data != int:
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


def editar_despesas():
    print("rapaz ta em construção ainda")
