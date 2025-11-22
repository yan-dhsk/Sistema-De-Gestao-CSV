import pytest
import csv
import os

CABECALHO = ['DespesaID', 'UsuarioID', 'Nome', 'Descricao', 'Valor', 'DataVencimento', 'TipoDespesa']

try:
    from modulo_despesas import (
        add_despesa,
        busca_despesas,
        lista_despesas,
        altera_despesa,
        remove_despesa
    )
except ImportError:
    # Mocks para evitar erro de importação antes de criar o arquivo real
    def add_despesa(*args, **kwargs): return 1
    def busca_despesas(*args, **kwargs): return []
    def lista_despesas(*args, **kwargs): return []
    def altera_despesa(*args, **kwargs): return 1
    def remove_despesa(*args, **kwargs): return 1


@pytest.fixture
def csv_temp(tmp_path):
    arquivo_csv = tmp_path / "despesas.csv"
    try:
        with open(arquivo_csv, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(CABECALHO)
    except IOError as e:
        pytest.fail(f"Falha ao criar CSV de teste: {e}")
        
    yield str(arquivo_csv)

def _popula_busca(csv_temp):
    with open(csv_temp, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['1', '1', 'Aluguel do Apto', '', '1500.0', '2025-11-01', 'Moradia'])
        writer.writerow(['2', '1', 'ALMOÇO da firma', '', '45.0', '2025-12-01', 'Alimentação'])
        writer.writerow(['3', '1', 'Luz', '', '200.0', '2025-10-01', 'Casa'])
        writer.writerow(['4', '2', 'Aluguel (Garagem)', '', '250.0', '2025-10-15', 'Outros'])

# add_despesa deve retornar o ID (int) da nova despesa ou 0 em caso de erro.
def test_add_ok(csv_temp):
    nova_despesa = {
        'UsuarioID': '123',
        'Nome': 'Luz',
        'Descricao': 'Conta de energia',
        'Valor': 250.00,
        'DataVencimento': '2025-12-10',
        'TipoDespesa': 'Fixa'
    }
    
    despesa_id = add_despesa(csv_temp, nova_despesa)
    assert despesa_id == 1

    with open(csv_temp, 'r') as f:
        reader = list(csv.reader(f))
        assert len(reader) == 2
        assert reader[1] == ['1', '123', 'Luz', 'Conta de energia', '250.0', '2025-12-10', 'Fixa']

# add_despesa deve retornar o ID (int) sequencial correto.
def test_add_auto_id(csv_temp):
    with open(csv_temp, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['1', '1', 'Agua', '', '100.0', '2025-11-01', 'Fixa'])
        writer.writerow(['2', '1', 'Net', '', '120.0', '2025-11-05', 'Fixa'])

    nova_despesa = { 'UsuarioID': '2', 'Nome': 'Aluguel', 'Valor': 1500.00, 'DataVencimento': '2025-11-10', 'Descricao': '', 'TipoDespesa': 'Moradia' }
    
    despesa_id = add_despesa(csv_temp, nova_despesa)
    
    assert despesa_id == 3

    with open(csv_temp, 'r') as f:
        reader = list(csv.reader(f))
        assert len(reader) == 4
        assert reader[3][0] == '3'
        assert reader[3][1] == '2'
        assert reader[3][2] == 'Aluguel'

# add_despesa deve retornar 0 em caso de valor inválido.
def test_add_valor_errado(csv_temp):
    despesa_invalida = { 'UsuarioID': '1', 'Nome': 'Invalida', 'Valor': 'cem reais', 'DataVencimento': '2025-12-10' }
    
    retorno = add_despesa(csv_temp, despesa_invalida)
    assert retorno == 0

# add_despesa deve retornar 0 em caso de data inválida.
def test_add_data_errada(csv_temp):
    despesa_invalida = { 'UsuarioID': '1', 'Nome': 'Invalida', 'Valor': 100.0, 'DataVencimento': '30/02/2025' }
    
    retorno = add_despesa(csv_temp, despesa_invalida)
    assert retorno == 0

# busca_despesas deve retornar uma lista de dicionários filtrada por nome.
def test_busca_nome_data(csv_temp):
    _popula_busca(csv_temp)
    
    despesas = busca_despesas(csv_temp, filtro_nome='Aluguel')
    
    assert len(despesas) == 2
    assert despesas[0]['DespesaID'] == '1'
    assert despesas[1]['DespesaID'] == '4'

# busca_despesas deve retornar uma sublista filtrada parcial e case-insensitive.
def test_busca_nome_parcial(csv_temp):
    _popula_busca(csv_temp)
    
    despesas = busca_despesas(csv_temp, filtro_nome='al')
    
    assert len(despesas) == 3
    assert despesas[0]['DespesaID'] == '2'
    assert despesas[1]['DespesaID'] == '1'
    assert despesas[2]['DespesaID'] == '4'

# busca_despesas deve retornar lista vazia se nenhum resultado for encontrado.
def test_busca_sem_res(csv_temp):
    _popula_busca(csv_temp)
    despesas = busca_despesas(csv_temp, filtro_nome='Inexistente')
    assert despesas == []

# lista_despesas deve retornar todas as despesas ordenadas por data decrescente.
def test_lista_todas(csv_temp):
    _popula_busca(csv_temp)
    
    # Deve retornar TUDO (4 itens)
    despesas = lista_despesas(csv_temp)
    
    assert len(despesas) == 4
    # Ordem decrescente de data:
    # 1. 2025-12-01 (ID 2)
    # 2. 2025-11-01 (ID 1)
    # 3. 2025-10-15 (ID 4)
    # 4. 2025-10-01 (ID 3)
    assert despesas[0]['DespesaID'] == '2'
    assert despesas[1]['DespesaID'] == '1'
    assert despesas[2]['DespesaID'] == '4'
    assert despesas[3]['DespesaID'] == '3'

# lista_despesas deve retornar lista vazia se CSV vazio.
def test_lista_vazio(csv_temp):
    despesas = lista_despesas(csv_temp)
    assert despesas == []

# altera_despesa deve retornar 1 se sucesso ou 0 em erro.
def test_altera_ok(csv_temp):
    _popula_busca(csv_temp)
    
    novos_dados = {'Valor': 1650.0, 'Descricao': 'Aumento'}
    
    retorno = altera_despesa(csv_temp, despesa_id='1', novos_dados=novos_dados)
    assert retorno == 1
    
    with open(csv_temp, 'r') as f:
        reader = csv.DictReader(f)
        for linha in reader:
            if linha['DespesaID'] == '1':
                assert linha['Valor'] == '1650.0'
                assert linha['Descricao'] == 'Aumento'
                break
        else:
            pytest.fail("ID 1 nao encontrado")

# altera_despesa deve retornar 0 se o ID não existir.
def test_altera_id_errado(csv_temp):
    _popula_busca(csv_temp)
    
    retorno = altera_despesa(csv_temp, despesa_id='99', novos_dados={'Valor': 100})
    assert retorno == 0

# altera_despesa deve retornar 0 se os novos dados forem inválidos.
def test_altera_dado_errado(csv_temp):
    _popula_busca(csv_temp)
    
    retorno = altera_despesa(csv_temp, despesa_id='1', novos_dados={'Valor': 'mil reais'})
    assert retorno == 0
    
    # Verifica integridade do arquivo
    with open(csv_temp, 'r') as f:
        reader = csv.DictReader(f)
        linha1 = next(reader)
        assert linha1['Valor'] == '1500.0'

# remove_despesa deve retornar 1 se sucesso ou 0 em erro.
def test_remove_ok(csv_temp):
    _popula_busca(csv_temp)
    
    # Remove ID 2 (ALMOÇO)
    retorno = remove_despesa(csv_temp, despesa_id='2')
    assert retorno == 1
    
    with open(csv_temp, 'r') as f:
        reader = list(csv.reader(f))
        # Cabeçalho + 3 itens restantes = 4 linhas
        assert len(reader) == 4
        
        ids_restantes = [row[0] for row in reader[1:]]
        assert '2' not in ids_restantes
        assert '1' in ids_restantes
        assert '3' in ids_restantes

# remove_despesa deve retornar 0 se ID não encontrado.
def test_remove_erro(csv_temp):
    _popula_busca(csv_temp)
    
    retorno = remove_despesa(csv_temp, despesa_id='99')
    assert retorno == 0
    
    with open(csv_temp, 'r') as f:
        reader = list(csv.reader(f))
        # Deve manter 5 linhas (cabeçalho + 4 dados)
        assert len(reader) == 5