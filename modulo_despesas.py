import csv
import datetime


def registar_despesas(usuario, produto, custo):
    with open("despesas.csv", "r", encoding="utf-8") as arquivo:
        despesas=list(csv.reader(arquivo, delimiter=','))
    hora_atual=datetime.datetime.now()
    despeas_atual=[]
    despeas_atual.append(hora_atual.strftime("%Y-%m-%d %H:%M:%S"))
    despeas_atual.append(produto)
    despeas_atual.append(custo)
    despeas_atual.append(usuario)
    despesas.append(despeas_atual)
    with open("despesas.csv", "w", encoding="utf-8", newline="") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerows(despesas)


def ver_despesas(data):
    if data == 0:
        with open("despesas.csv", "r", encoding="utf-8") as arquivo:
            despesas=list(csv.reader(arquivo, delimiter=','))
        print(despesas)
        return 0



def editar_despesas():
    print("rapaz ta em construção ainda")
