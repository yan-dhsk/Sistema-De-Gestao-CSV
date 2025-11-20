import csv

def listarVendas():
    with open ("listaVendas.csv", "r", encoding="utf-8") as vendas:
        todasVendas = list(csv.reader(vendas))
        todasVendas.sort(key=lambda venda: venda[9], reverse=True)
    return todasVendas

def pesquisarVendas(nome):
    itensEncontrados = []
    with open ("listaVendas.csv", "r", encoding="utf-8") as vendas:
        todasVendas = list(csv.reader(vendas))
        for x in range (1, len(todasVendas)):
            if nome.lower in todasVendas[x].lower:
                itensEncontrados.append(todasVendas[x])
        itensEncontrados.sort(key=lambda venda: venda[9], reverse=True)
    return itensEncontrados

def removerVenda(id):
    linhaDoItem = 0
    with open ("listaVendas.csv", "r", encoding="utf-8") as vendas:
        todasVendas = list(csv.reader(vendas))
        for x in range (1, len(todasVendas)):
            if id == int(todasVendas[x][0]):
                linhaDoItem = x
                break
    with open ("listaVendas.csv", "r", encoding="utf-8") as vendas:
        escrita = csv.writer(vendas)
        todasVendas.pop(linhaDoItem)
        escrita.writerow(todasVendas)

def alterarVenda(escolha, id, novo):
    linhaDoItem = 0
    with open ("listaVendas.csv", "r", encoding="utf-8") as vendas:
        todasVendas = list(csv.reader(vendas))
        for x in range (1, len(todasVendas)):
            if id == int(todasVendas[x][0]):
                linhaDoItem = x
                break
    with open ("listaVendas.csv", "w", encoding="utf-8"):
        todasVendas[linhaDoItem][escolha] = novo
        escrita = csv.writer(vendas)
        escrita.writerow(todasVendas)

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