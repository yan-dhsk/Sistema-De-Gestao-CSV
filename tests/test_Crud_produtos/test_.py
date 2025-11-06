import CRUD_produto
import csv

def test_lista_tudo():
    produtos = CRUD_produto.listar_todos()
    with open("listaProdutos.csv", "r", encoding="utf-8") as arquivo:
        lista = list(csv.reader(arquivo, delimiter=','))
    assert f'ID: {lista[1][0]} ' in produtos[0]
    assert len(lista)-1 == len(produtos)

def test_adicionar_produtos():
    produto=["fone","2","5","1","fone bluetooth","1"]
    id=CRUD_produto.adicionar_produto(produto)
    with open("listaProdutos.csv", "r", encoding="utf-8") as arquivo:
        lista = list(csv.reader(arquivo, delimiter=','))
    assert int(lista[len(lista)-1][0]) == id


def test_deletar_produto():
    with open("listaProdutos.csv", "r", encoding="utf-8") as arquivo:
        lista = list(csv.reader(arquivo, delimiter=','))
    id=int(lista[len(lista)-1][0])
    assert CRUD_produto.deletar_produto(id)==True

def test_atualizar_produtos():
    with open("listaProdutos.csv", "r", encoding="utf-8") as arquivo:
        lista = list(csv.reader(arquivo, delimiter=','))
    id=int(lista[len(lista)-1][0])
    elemento=1
    valor=5
    assert CRUD_produto.atualizar_produtos(id,elemento,valor)==True

def test_pesquisar_produto():
    with open("listaProdutos.csv", "r", encoding="utf-8") as arquivo:
        lista = list(csv.reader(arquivo, delimiter=','))
    nome=lista[1][5]
    produto=CRUD_produto.buscar_produto(nome)
    assert f'ID: {lista[1][0]} - R${lista[1][3]} - {lista[1][5]} - {lista[1][2]} em estoque' in produto

def test_estoque_baixo():
    estoque=CRUD_produto.baixo_estoque()
    n1=(estoque[0][len(estoque[0])-14])
    n2=(estoque[0][len(estoque[0])-13])
    num=int(n1+n2)
    assert num < 30

def test_estoque_alto():
    estoque=CRUD_produto.alto_estoque()
    print(f"{estoque}\n")
    n1=(estoque[0][len(estoque[0])-15])
    n2=(estoque[0][len(estoque[0])-14])
    n3=(estoque[0][len(estoque[0])-13])
    num=int(n1+n2+n3)
    assert num > 100
