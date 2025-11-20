import csv

def listarVendas():
    with open("listaVendas.csv", "r", encoding="utf-8") as vendas:
        todasVendas = list(csv.reader(vendas))
        if not todasVendas:
            return []
        todasVendas[1:] = sorted(todasVendas[1:], key=lambda venda: venda[9] if len(venda) > 9 else '', reverse=True)
    return todasVendas

def pesquisarVendas(nome):
    itensEncontrados = []
    with open("listaVendas.csv", "r", encoding="utf-8") as vendas:
        todasVendas = list(csv.reader(vendas))
        for x in range(1, len(todasVendas)):
            if nome.lower() in ' '.join(todasVendas[x][1:10]).lower():
                itensEncontrados.append(todasVendas[x])
        itensEncontrados.sort(key=lambda venda: venda[9] if len(venda) > 9 else '', reverse=True)
    return itensEncontrados

def removerVenda(id):
    linhaDoItem = 0
    with open("listaVendas.csv", "r", encoding="utf-8") as vendas:
        todasVendas = list(csv.reader(vendas))
        for x in range(1, len(todasVendas)):
            if len(todasVendas[x]) > 0 and id == int(todasVendas[x][0]):
                linhaDoItem = x
                break
        if linhaDoItem == 0:
            return 0
    with open("listaVendas.csv", "w", newline='', encoding="utf-8") as vendas:
        todasVendas.pop(linhaDoItem)
        escrita = csv.writer(vendas)
        escrita.writerows(todasVendas)
        return 1

def alterarVenda(escolha, id, novo):
    linhaDoItem = 0
    with open("listaVendas.csv", "r", encoding="utf-8") as vendas:
        todasVendas = list(csv.reader(vendas))
        for x in range(1, len(todasVendas)):
            if len(todasVendas[x]) > 0 and id == int(todasVendas[x][0]):
                linhaDoItem = x
                break
        if linhaDoItem == 0:
            return 0
    if escolha < 0 or escolha >= len(todasVendas[linhaDoItem]):
        return 0
    with open("listaVendas.csv", "w", newline='', encoding="utf-8") as vendas:
        todasVendas[linhaDoItem][escolha] = novo
        escrita = csv.writer(vendas)
        escrita.writerows(todasVendas)
        return 1

def registrarVenda(novaVenda):
    with open("listaProdutos.csv", "r", encoding="utf-8") as produtos:
        linhaDoProduto = 0
        todosProdutos = list(csv.reader(produtos, delimiter=','))
        for x in range(1, len(todosProdutos)):
            if int(todosProdutos[x][0]) == int(novaVenda[1]):
                linhaDoProduto = x
                break
        if linhaDoProduto == 0:
            return 2
        if int(todosProdutos[linhaDoProduto][2]) < int(novaVenda[3]):
            return 0
        todosProdutos[linhaDoProduto][2] = int(todosProdutos[linhaDoProduto][2]) - int(novaVenda[3])
    with open("listaProdutos.csv", "w", newline='', encoding="utf-8") as produtos:
        escritor = csv.writer(produtos)
        escritor.writerows(todosProdutos)
    id = int(0)
    with open("listaVendas.csv", "a+", newline='', encoding="utf-8") as vendas:
        vendas.seek(0)
        todasVendas = list(csv.reader(vendas, delimiter=','))
        for x in range(1, len(todasVendas)):
            if int(todasVendas[x][0]) > id:
                id = int(todasVendas[x][0])
        id += 1
        novaVenda[0] = id
    novaVenda[5] = int(novaVenda[3]) * int(novaVenda[4])
    if todasVendas:
        todasVendas.append(novaVenda)
    else:
        todasVendas = [['VendaID','ProdutoID','NomeProdutoVendido','QuantidadeVendida','PrecoUnitarioVendido','ValorTotalVendido','UsuarioID','ClienteID','MetodoPagamento','DataVenda']]
        todasVendas.append(novaVenda)
    with open("listaVendas.csv", "w", newline='', encoding="utf-8") as vendas:
        escrita = csv.writer(vendas)
        escrita.writerows(todasVendas)
        return 1
