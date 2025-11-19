import csv

def registrarVenda(novaVenda):
    with open ("listaProdutos.csv", "r", encoding="utf-8") as produtos:
        linhaDoProduto = 0
        todosProdutos = list(csv.reader(produtos, delimiter=','))
        for x in range (1, len(todosProdutos)):
            if int(todosProdutos[x][0]) == int(novaVenda[1]):
                linhaDoProduto = x
                break
        if int(todosProdutos[linhaDoProduto][2]) <= 0:
            return 0
        else:
            int(todosProdutos[linhaDoProduto][2]) -= int(novaVenda[3])
    int(id) = 0
    with open ("listaVenda.csv", "a+", encoding="utf-8") as vendas:
        todasVendas = list(csv.reader(vendas, delimiter=','))
        for x in range (1, len(todasVendas)):
            if todasVendas[x][0] > id:
                id = int(todasVendas[x][0])
        id += 1
        novaVenda[0] = id
        escrita = csv.writer(vendas)
        escrita.writerow(novaVenda)
        return 1


