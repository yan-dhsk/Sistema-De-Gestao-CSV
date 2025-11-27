import csv

def verificarFormato(data):
    try:
        partes = data.split('-')
        if len(partes) != 3:
            return 2
        dia = int(partes[2])
        mes = int(partes[1])
        ano = int(partes[0])
        if dia > 31 or mes > 12:
            return 2
        return 1
    except ValueError:
        return 2

def validarData(data):
    with open("listaVendas.csv", "r", encoding="utf-8") as arquivo:
        leitor = list(csv.reader(arquivo))
        for x in range(1, len(leitor)):
            if leitor[x][9] == data:
                return 1
    return 0

def montarBi(inicio, fim):
    encontrado = 0
    with open("listaProdutos.csv", "r", encoding="utf-8") as produtos:
        todosProdutos = list(csv.reader(produtos))
    agrupado = []
    cabecalho = ['Data','Produto','Categoria','Quantidade','Preco_Unitario','Custo_Unitario']
    with open("listaVendas.csv", "r", encoding="utf-8") as arquivo:
        vendas = list(csv.reader(arquivo))
        for x in range(1, len(vendas)):
            if vendas[x][9] >= inicio and vendas[x][9] <= fim:
                for p in range(1, len(todosProdutos)):
                    if todosProdutos[p][0] == vendas[x][1]:
                        custo = float(todosProdutos[p][7])
                        categoria = todosProdutos[p][4]
                        break
                for k in range(len(agrupado)):
                    if agrupado[k][0] == vendas[x][9] and agrupado[k][1] == vendas[x][2]:
                        agrupado[k][3] += int(vendas[x][3])
                        encontrado = 1
                        break
                if encontrado == 0:
                    nova = [vendas[x][9], vendas[x][2], categoria, int(vendas[x][3]), vendas[x][4], custo]
                    agrupado.append(nova)
    if not agrupado:
        return 3
    with open("relatorioBi.csv", "w", newline='', encoding="utf-8") as relatorio:
        escrita = csv.writer(relatorio)
        escrita.writerow(cabecalho)
        escrita.writerows(agrupado)
    return 1

def criarRelatorio(inicio, fim):
    listaVendas = []
    vendasCategorias = {}
    faturamento = 0.0
    despesa = 0
    quantidadeTotal = 0
    with open("listaProdutos.csv", "r", encoding="utf-8") as arquivo:
        todosProdutos = list(csv.reader(arquivo))
    with open("listaVendas.csv", "r", encoding="utf-8") as arquivo:
        vendas = list(csv.reader(arquivo))
        for x in range(1, len(vendas)):
           for p in range(1, len(todosProdutos)):
                    if todosProdutos[p][0] == vendas[x][1]:
                        vendasCategorias[todosProdutos[p][4]] = 0
        for x in range(1, len(vendas)):
            if vendas[x][9] >= inicio and vendas[x][9] <= fim:
                faturamento += float(vendas[x][5])
                quantidadeTotal += int(vendas[x][3])
                for p in range(1, len(todosProdutos)):
                    if todosProdutos[p][0] == vendas[x][1]:
                        vendasCategorias[todosProdutos[p][4]] += int(vendas[x][3])
                        break
                existe = 0
                for i in range(len(listaVendas)):
                    if listaVendas[i][0] == vendas[x][2]:
                        listaVendas[i][1] += int(vendas[x][3])
                        existe = 1
                        break
                if existe == 0:
                    listaVendas.append([vendas[x][2], int(vendas[x][3])])

    with open("despesas.csv", "r", encoding="utf-8") as arquivo:
        despesas = list(csv.reader(arquivo))
        for x in range(1, len(despesas)):
            if despesas[x][0] >= inicio and despesas[x][0] <= fim:
                despesa += float(despesas[x][2])

    listaVendas.sort(key=lambda x: x[1], reverse=True)
    topDez = listaVendas[:10]
    listaVendas.sort(key=lambda x: x[1])
    menosDez = listaVendas[:10]
    lucroLiq = faturamento - despesa
    
    with open("relatorioPronto.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("=== RELATORIO DE VENDAS ===\n")
        arquivo.write("Periodo: " + inicio + " ate " + fim + "\n")
        arquivo.write(f"Faturamento Total: R${faturamento:.2f}\n")
        arquivo.write(f"Lucro Bruto: R${lucroLiq:.2f}\n")
        arquivo.write(f"Total Despesas: R${despesa:.2f}\n")
        arquivo.write(f"Vendas Totais: {quantidadeTotal}\n")
        arquivo.write("\n--- TOP 10 MAIS VENDIDOS ---\n")
        for x in range(len(topDez)):
            arquivo.write(topDez[x][0] + " - Quantidade: " + str(topDez[x][1]) + "\n")
        arquivo.write("\n ---TOP 10 MENOS VENDIDOS ---\n")
        for x in range(len(menosDez)):
            arquivo.write(menosDez[x][0] + " - Quantidade: " + str(menosDez[x][1]) + "\n")
        arquivo.write("\n--- Vendas por categoria ---")
        for x in dict.keys(vendasCategorias):
            arquivo.write(f'\n{x}: {vendasCategorias[x]}')
def carregarRelatorio():
    linhas = []
    with open("relatorioPronto.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
    return linhas