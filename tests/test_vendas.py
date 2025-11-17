import pytest
import csv
import os
import datetime

from modulo_vendas import registrar_venda, alterar_venda, pesquisar_vendas_nome

@pytest.fixture
def setup_csvs_temporarios():
    
    arquivo_produtos_teste = 'test_produtos.csv'
    cabecalho_produtos = ['ProdutoID','Descricao','Quantidade','PreçoDeVenda','CategoriaID','Nome','UsuarioID','PreçoDeCusto']
    dados_produtos = [
        ['1','Fone de ouvido...','43','250','1','Fone Bluetooth Elite','1','100'],
        ['2','Capinha silicone...','100','25','2','Capinha Protetora X','1','10'],
        ['3','Caixa de som...','30','180','3','Caixa Som Bluetooth Pro','1','80']
    ]

    arquivo_vendas_teste = 'test_vendas.csv'
    cabecalho_vendas = [
        'VendaID','ProdutoID','NomeProdutoVendido','QuantidadeVendida',
        'PrecoUnitarioVendido','ValorTotalVendido','UsuarioID','ClienteID',
        'MetodoPagamento','DataVenda'
    ]
    
    dados_venda_inicial = [
        ['2','1','Fone Bluetooth Elite','2','250','500','1','21','Dinheiro','2025-11-15'],
        ['1','1','Fone Bluetooth Elite','5','250','1250','1','20','Pix','2025-11-16']
    ]

    with open(arquivo_produtos_teste, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(cabecalho_produtos)
        writer.writerows(dados_produtos)
        
    with open(arquivo_vendas_teste, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(cabecalho_vendas)
        writer.writerows(dados_venda_inicial)

    yield {
        "produtos": arquivo_produtos_teste, 
        "vendas": arquivo_vendas_teste
    }
    
    os.remove(arquivo_produtos_teste)
    os.remove(arquivo_vendas_teste)


# A função deve retornar o ID da nova venda (3) e o estoque do ID 2 deve ser 90.
def test_venda_sucesso(setup_csvs_temporarios):
    arquivos = setup_csvs_temporarios
    produtos_csv = arquivos["produtos"]
    vendas_csv = arquivos["vendas"]

    dados_nova_venda = {
        "produto_id": 2,
        "quantidade": 10,
        "usuario_id": 1,
        "cliente_id": "30",
        "metodo_pagamento": "Cartão"
    }
    
    novo_id_venda = registrar_venda(dados_nova_venda, produtos_csv, vendas_csv)
    
    assert novo_id_venda == 3

    with open(produtos_csv, 'r', encoding='utf-8') as f:
        produtos = list(csv.reader(f))
    
    assert produtos[2][2] == '90' 

    with open(vendas_csv, 'r', encoding='utf-8') as f:
        vendas = list(csv.reader(f))
        
    assert len(vendas) == 4
    
    nova_venda_registrada = vendas[3]
    
    assert nova_venda_registrada[0] == '3'
    assert nova_venda_registrada[5] == '250'


# A função deve retornar False. O CSV não deve ser alterado.
def test_venda_sem_estoque(setup_csvs_temporarios):
    arquivos = setup_csvs_temporarios
    
    dados_nova_venda = {"produto_id": 3, "quantidade": 40}
    
    resultado = registrar_venda(dados_nova_venda, arquivos["produtos"], arquivos["vendas"])
    
    assert resultado == False
    
    with open(arquivos["produtos"], 'r', encoding='utf-8') as f:
        produtos = list(csv.reader(f))
    assert produtos[3][2] == '30'

    with open(arquivos["vendas"], 'r', encoding='utf-8') as f:
        vendas = list(csv.reader(f))
    assert len(vendas) == 3


# A função deve retornar False. O CSV não deve ser alterado.
def test_venda_produto_inexistente(setup_csvs_temporarios):
    arquivos = setup_csvs_temporarios
    dados_nova_venda = {"produto_id": 9999, "quantidade": 1}
    
    resultado = registrar_venda(dados_nova_venda, arquivos["produtos"], arquivos["vendas"])
        
    assert resultado == False

    with open(arquivos["produtos"], 'r', encoding='utf-8') as f:
        produtos = list(csv.reader(f))
    assert len(produtos) == 4

    with open(arquivos["vendas"], 'r', encoding='utf-8') as f:
        vendas = list(csv.reader(f))
    assert len(vendas) == 3


# A função deve retornar True e o MetodoPagamento da VendaID 1 deve ser "Dinheiro".
def test_alterar_venda_simples(setup_csvs_temporarios):
    arquivos = setup_csvs_temporarios
    
    resultado = alterar_venda(
        venda_id=1,
        campo="MetodoPagamento",
        novo_valor="Dinheiro",
        arquivo_produtos=arquivos["produtos"],
        arquivo_vendas=arquivos["vendas"]
    )
    
    assert resultado == True
    
    with open(arquivos["vendas"], 'r', encoding='utf-8') as f:
        vendas = list(csv.reader(f))
    venda_alterada = vendas[2]
    
    assert venda_alterada[8] == "Dinheiro"


# A função deve retornar False se a VendaID não for encontrada.
def test_alterar_venda_nao_encontrada(setup_csvs_temporarios):
    arquivos = setup_csvs_temporarios
    
    resultado = alterar_venda(
        venda_id=999,
        campo="MetodoPagamento",
        novo_valor="Inexistente",
        arquivo_produtos=arquivos["produtos"],
        arquivo_vendas=arquivos["vendas"]
    )
    assert resultado == False


# A função deve retornar True. O estoque do ID 1 deve aumentar para 45 e o ValorTotal da Venda ID 1 deve ser 750.
def test_alterar_venda_devolucao(setup_csvs_temporarios):
    arquivos = setup_csvs_temporarios
    
    resultado = alterar_venda(
        venda_id=1,
        campo="QuantidadeVendida",
        novo_valor=3,
        arquivo_produtos=arquivos["produtos"],
        arquivo_vendas=arquivos["vendas"]
    )
    
    assert resultado == True
    
    with open(arquivos["vendas"], 'r', encoding='utf-8') as f:
        vendas = list(csv.reader(f))
    venda_alterada = vendas[2]
    assert venda_alterada[3] == '3'
    assert venda_alterada[5] == '750'
    
    with open(arquivos["produtos"], 'r', encoding='utf-8') as f:
        produtos = list(csv.reader(f))
    produto_fone = produtos[1]
    
    assert produto_fone[2] == '45'


# A função deve retornar True. O estoque do ID 1 deve diminuir para 41 e o ValorTotal da Venda ID 1 deve ser 1750.
def test_alterar_venda_nova_venda(setup_csvs_temporarios):
    arquivos = setup_csvs_temporarios

    resultado = alterar_venda(
        venda_id=1,
        campo="QuantidadeVendida",
        novo_valor=7,
        arquivo_produtos=arquivos["produtos"],
        arquivo_vendas=arquivos["vendas"]
    )
    
    assert resultado == True
    
    with open(arquivos["vendas"], 'r', encoding='utf-8') as f:
        vendas = list(csv.reader(f))
    venda_alterada = vendas[2]
    assert venda_alterada[3] == '7'
    assert venda_alterada[5] == '1750'
    
    with open(arquivos["produtos"], 'r', encoding='utf-8') as f:
        produtos = list(csv.reader(f))
    produto_fone = produtos[1]
    
    assert produto_fone[2] == '41'
            
    
# A função deve retornar False. O CSV não deve ser alterado.
def test_alterar_venda_estoque_falha(setup_csvs_temporarios):
    arquivos = setup_csvs_temporarios

    resultado = alterar_venda(
        venda_id=1,
        campo="QuantidadeVendida",
        novo_valor=51,
        arquivo_produtos=arquivos["produtos"],
        arquivo_vendas=arquivos["vendas"]
    )
    
    assert resultado == False
    
    with open(arquivos["produtos"], 'r', encoding='utf-8') as f:
        produtos = list(csv.reader(f))
    assert produtos[1][2] == '43'

    with open(arquivos["vendas"], 'r', encoding='utf-8') as f:
        vendas = list(csv.reader(f))
    assert vendas[2][3] == '5'


# A função deve retornar uma lista de duas vendas, onde a Venda ID 1 (16/11) aparece antes da Venda ID 2 (15/11).
def test_pesquisar_nome_sucesso(setup_csvs_temporarios):
    arquivos = setup_csvs_temporarios
    
    resultados = pesquisar_vendas_nome("Fone Bluetooth Elite", arquivos["vendas"])
    
    assert len(resultados) == 2
    
    assert "1" in resultados[0]
    assert "2" in resultados[1]
    assert "R$1250" in resultados[0]


# A função deve retornar uma lista vazia ([]) se o produto não for encontrado.
def test_pesquisar_nome_vazio(setup_csvs_temporarios):
    arquivos = setup_csvs_temporarios
    
    resultados = pesquisar_vendas_nome("Produto Inexistente", arquivos["vendas"])
    
    assert resultados == []