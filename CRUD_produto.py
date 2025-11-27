import csv
import modulo_despesas

def listar_todos():
    with open("listaProdutos.csv", "r", encoding="utf-8") as arquivo:
        produtos = list(csv.reader(arquivo, delimiter=','))
    resultados = []
    for p in range (1, len(produtos)):
        resultados.append(f"ID: {produtos[p][0]} - R${produtos[p][3]} - {produtos[p][5]} - {produtos[p][1]} - {produtos[p][2]} em estoque - ID de categoria: {produtos[p][4]} - Registrado pelo úsuario de ID: {produtos[p][6]}")
    return resultados
            
def buscar_produto(busca):
    controle = 0
    resultados = []
    with open ("listaProdutos.csv", "r", encoding="utf-8") as arquivo:
        produtos = list(csv.reader(arquivo, delimiter=','))
        for x in range (1, len(produtos)):
            if busca.lower() in produtos[x][5].lower():
                resultados.append(f"ID: {produtos[x][0]} - R${produtos[x][3]} - {produtos[x][5]} - {produtos[x][2]} em estoque")
                controle += 1
    if controle == 0:
        return []
    return resultados

def adicionar_produto(informacoes_produto,usuario):
    with open("listaProdutos.csv", "r", encoding="utf-8") as arquivo:
        produtos = list(csv.reader(arquivo, delimiter=','))
    novo_produto = []
    maior_id = 0
    for i in range (1, len(produtos)):
        if int(produtos[i][0]) > maior_id:
            maior_id = int(produtos[i][0])
    novo_id = maior_id + 1
    novo_produto.append(str(novo_id))
    for valor in informacoes_produto:
        novo_produto.append(valor)
    produtos.append(novo_produto)
    with open("listaProdutos.csv", "w", encoding="utf-8", newline="") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerows(produtos)
    modulo_despesas.registar_despesas(usuario, "produto", int(produtos[novo_id][7])*int(produtos[novo_id][2]), produtos[novo_id][5])
    return novo_id

def deletar_produto(deletar):
    with open ("listaProdutos.csv", "r", encoding="utf-8") as arquivo:
        produtos = list(csv.reader(arquivo, delimiter=","))
    controle = 0
    for y in range (1, len(produtos)):
        if deletar == int(produtos[y][0]):
            controle += 1
            break;
    if controle == 0:
        return False
    for x in range (1, len(produtos)):
            if int(produtos[x][0]) == deletar:
                produtos.pop(x)
                break
    with open ("listaProdutos.csv", "w", encoding="utf-8", newline='') as arquivo:
        escrita = csv.writer(arquivo)
        escrita.writerows(produtos)
    return True

def atualizar_produtos(id_produto, elemento, novo_valor):
    with open ("listaProdutos.csv", "r", encoding="utf-8") as arquivo:
        produtos = list(csv.reader(arquivo, delimiter=","))
    controle = 0
    posicao = 0
    for y in range (1, len(produtos)):
        if id_produto == int(produtos[y][0]):
            controle += 1
            posicao = y
            break;
    if controle == 0:
        return False
    if elemento == 1:
        produtos[posicao][3] = novo_valor
    elif elemento == 2:
        produtos[posicao][2] = novo_valor
    elif elemento == 3:
        produtos[posicao][5] = novo_valor
    elif elemento == 4:
        produtos[posicao][1] = novo_valor
    elif elemento == 5:
        produtos[posicao][4] = novo_valor
    with open("listaProdutos.csv", "w", encoding="utf-8", newline='') as arquivo:
        escrita = csv.writer(arquivo)
        escrita.writerows(produtos)
    return True

def baixo_estoque():
    with open("listaProdutos.csv", "r", encoding="utf-8") as arquivo:
        produtos = list(csv.reader(arquivo, delimiter=','))
    resultados = []
    for i in range (1, len(produtos)):
        if int(produtos[i][2]) < 30:
            resultados.append(f"{produtos[i][5]} - tem {produtos[i][2]} em estoque!")
    return resultados

def alto_estoque():
    with open("listaProdutos.csv", "r", encoding="utf-8") as arquivo:
        produtos = list(csv.reader(arquivo, delimiter=','))
    resultados = []
    for i in range (1, len(produtos)):
        if int(produtos[i][2]) > 100:
            resultados.append(f"{produtos[i][5]} - tem {produtos[i][2]} em estoque!")
    return resultados