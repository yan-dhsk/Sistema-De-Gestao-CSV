import CRUD_produto
import csv

def test_lista_tudo():
    produtos = CRUD_produto.listar_todos()
    with open("listaProdutos.csv", "r", encoding="utf-8") as arquivo:
        lista = list(csv.reader(arquivo, delimiter=','))
    assert f'ID: {lista[6][0]} ' in produtos[5]

def test_adicionar_produtos():
    produtos=CRUD_produto.listar_todos()
    id= len(produtos)+1
    produto=["fone","2","5","1","fone bluetooth","1"]
    assert CRUD_produto.adicionar_produto(produto)==id


def test_deletar_produto():
    produtos= CRUD_produto.listar_todos()
    id=len(produtos)
    assert CRUD_produto.deletar_produto(id)==True

def test_atualizar_produtos():
    id=1
    elemento=1
    valor=5
    assert CRUD_produto.atualizar_produtos(id,elemento,valor)==True

def test_pesquisar_produto():
    nome="CaIXa SoM fM"
    lista=CRUD_produto.buscar_produto(nome)
    assert 'ID: 68 - R$110 - Caixa Som FM - 55 em estoque' in lista

def test_estoque_baixo():
    estoque=CRUD_produto.baixo_estoque()
    assert "Fone Stylus - tem 25 em estoque!" in estoque

def test_estoque_alto():
    estoque=CRUD_produto.alto_estoque()
    assert "Película Hidrogel - tem 180 em estoque!" in estoque

