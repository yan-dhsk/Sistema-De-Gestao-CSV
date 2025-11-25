import CRUD_produto
import datetime
import modulo_vendas
import Login
import modulo_despesas

def vendas(usuario):
    while True:
        print("Bem-Vindo a seção de Vendas!")
        escolha = input("1 - Registrar nova venda\n2 - Pesquisar venda\n3 - Remover venda\n4 - Atualizar venda\n5 - Consultar todas as vendas\n0 - Retornar ao menu principal\nPorfavor selecione sua opção: ")
        escolha = escolha.strip()
        if escolha.isdigit():
            escolha = int(escolha)
        else:
            escolha = -1
        if escolha == 0:
            print("==================================================================")
            menu()
            break
        elif escolha == 1:
            novaVenda = [0]
            produtoid = input("Digite o id do produto (zero se não souber): ")
            produtoid = produtoid.strip()
            if produtoid.isdigit():
                produtoid = int(produtoid)
            else:
                produtoid = 0
            preço = input("Digite o preço do produto (zero se não souber): ")
            preço = preço.strip()
            if preço.isdigit():
                preço = int(preço)
            else:
                preço = 0
            nomeProduto = input("Escreva o nome do produto: ")
            if produtoid == 0:
                resultados = CRUD_produto.buscar_produto(nomeProduto)
                if not resultados:
                    print("Nenhum produto com este nome cadastrado!")
                    continue
                else:
                    if len(resultados) == 1:
                        produtoid = int(resultados[0][0]) if len(resultados[0]) > 0 and str(resultados[0][0]).strip().isdigit() else 0
                    else:
                        print("==================================================================")
                        for res in resultados:
                            print(res)
                        print("==================================================================")
                        produtoid = input("Agora digite corretamente o id do produto (zero se não achar): ")
                        produtoid = produtoid.strip()
                        if produtoid.isdigit():
                            produtoid = int(produtoid)
                        else:
                            produtoid = 0
                        preço = input("Agora digite corretamente o preço do produto (zero se não achar): ")
                        preço = preço.strip()
                        if preço.isdigit():
                            preço = int(preço)
                        else:
                            preço = 0
            quantidade = input("Digite a quantidade vendida: ")
            quantidade = quantidade.strip()
            if quantidade.isdigit():
                quantidade = int(quantidade)
            else:
                quantidade = 0
            total = preço * quantidade
            cliente = input("Digite o ID do cliente (zero se não cadastrado): ")
            cliente = cliente.strip()
            if cliente.isdigit():
                cliente = int(cliente)
            else:
                cliente = 0
            metodo = input("Digite o metodo de pagamento: ")
            data = datetime.datetime.now().replace(microsecond=0)
            novaVenda.append(produtoid)
            novaVenda.append(nomeProduto)
            novaVenda.append(quantidade)
            novaVenda.append(preço)
            novaVenda.append(total)
            novaVenda.append(1)
            novaVenda.append(cliente)
            novaVenda.append(metodo)
            novaVenda.append(data)
            resultado = modulo_vendas.registrarVenda(novaVenda)
            if resultado == 1:
                print("Venda registrada com sucesso!")
            elif resultado == 0:
                print("Estoque insuficiente para concluir a venda!")
            elif resultado == 2:
                print("Produto não encontrado no cadastro!")
            else:
                print("Houve um problema ao registrar a venda!")
            print("==================================================================")
        elif escolha == 2:
            pesquisa = input("Digite um parametro de pesquisa (nome do produto, data, metodo de pagamento): ")
            encontradas = modulo_vendas.pesquisarVendas(pesquisa)
            print("==================================================================")
            if not encontradas:
                print("Nenhuma venda encontrada!")
            else:
                for item_venda in encontradas:
                    print(f"ID da venda: {item_venda[0] if len(item_venda)>0 else ''} - ID do produto: {item_venda[1] if len(item_venda)>1 else ''} - Nome: {item_venda[2] if len(item_venda)>2 else ''} - Preço: {item_venda[4] if len(item_venda)>4 else ''} - Quantidade: {item_venda[3] if len(item_venda)>3 else ''} - Valor total: {item_venda[5] if len(item_venda)>5 else ''} - Usuário: {item_venda[6] if len(item_venda)>6 else ''} - Cliente: {item_venda[7] if len(item_venda)>7 else ''} - Pagamento: {item_venda[8] if len(item_venda)>8 else ''} - Data: {item_venda[9] if len(item_venda)>9 else ''}")
                    print("------------------------------------------------------------------")
            print("==================================================================")
        elif escolha == 3:
            id = input("Digite o ID da venda (digite zero para voltar ao menu): ")
            id = id.strip()
            if id.isdigit():
                id = int(id)
            else:
                id = 0
            if id == 0:
                print("Voltando para o menu de vendas...")
                pass
            else:
                resultado = modulo_vendas.removerVenda(id)
                if resultado == 0:
                    print("Venda não encontrada!")
                else:
                    print("Venda removida com sucesso!")
        elif escolha == 4:
            escolha2 = input("Escolha o elemento da venda que deseja alterar!\n1 - ID do produto\n2 - Nome do produto\n3 - Quantidade\n4 - Preço unitario\n5 Preço total\n 6- ID do úsuario\n7 - ID do cliente\n8 - Metodo de pagamento\n9 - Data e horario\nSelecione sua opção: ")
            escolha2 = escolha2.strip()
            if escolha2.isdigit():
                escolha2 = int(escolha2)
            else:
                escolha2 = -1
            id = input("Digite o ID da venda (zero para voltar ao menu): ")
            id = id.strip()
            if id.isdigit():
                id = int(id)
            else:
                id = 0
            if id == 0:
                print("Voltando para o menu de vendas...")
                pass
            novo = input("Digite o novo parametro: ")
            resultado = modulo_vendas.alterarVenda(escolha2, id, novo)
            if resultado == 1:
                print("Venda alterada com sucesso!")
                print("==================================================================")
            else:
                print("Houve um problema ao alterar a venda!")
                print("==================================================================")
        elif escolha == 5:
            resultado = modulo_vendas.listarVendas()
            for x in range(1, len(resultado)):
                print("==================================================================")
                print(f"ID da venda: {resultado[x][0] if len(resultado[x])>0 else ''} - ID do produto: {resultado[x][1] if len(resultado[x])>1 else ''} - Nome: {resultado[x][2] if len(resultado[x])>2 else ''} - Preço: {resultado[x][4] if len(resultado[x])>4 else ''} - Quantidade: {resultado[x][3] if len(resultado[x])>3 else ''} - Valor total: {resultado[x][5] if len(resultado[x])>5 else ''} - Usuário: {resultado[x][6] if len(resultado[x])>6 else ''} - Cliente: {resultado[x][7] if len(resultado[x])>7 else ''} - Pagamento: {resultado[x][8] if len(resultado[x])>8 else ''} - Data: {resultado[x][9] if len(resultado[x])>9 else ''}")
            print("==================================================================")
        else:
            print("Opção Inválida!")
            pass

def relatorio(usuario):
    print("Sentimos muito, esta área ainda esta em desenvolvimento!")
    print("==================================================================")
    menu(usuario)

def despesas(usuario):
    while True:
        print("Bem-Vindo a seção de despesas!")
        escolha = int(input("1 - Adicionar novas despesas\n2 - Excluir despesas\n3 - Consultar todos as despesas\n4 - Consultar despesas de dia especifico\n5 - Consultar pro usuario\n6 - Editar despesas\n0 - Voltar ao menu\n"))
        if escolha == 0:
                print("==================================================================")
                menu(usuario)
                break
        
        elif escolha == 1:
            divida_tipo=input("Digite as informações da despesa\nQual o tipo de despesa? (Anual, Mensal, Semanal, Unica ....)\n")
            divida_custo=input("Qual o custo?\n")
            divida_nome=input("Qual o nome?\n")
            resul=modulo_despesas.registar_despesas(usuario, divida_tipo, divida_custo, divida_nome )
            print("==================================================================")
            if resul == 1:
                print("Despesa adicionada com sucesso")
            else:
                print("Ocorreu um erro, despesa nao adicionada")
            print("==================================================================")

        elif escolha == 2:
            data=input("Digite a data conforme o exemplo: (19-07-2021):\n")
            despesas=modulo_despesas.editar_despesas1(data)
            if despesas == 0:
                print("==================================================================")
                print("Data não encontrada")
                pass
            else:
                for i in range (0, len(despesas)):
                    print("==================================================================")
                    print(f"ID: {i+1} | Data: {despesas[i][0]} | Tipo: {despesas[i][1]} | Custo: R${despesas[i][2]} | Nome: {despesas[i][3]} | Usuario: {despesas[i][4]}")
                print("==================================================================")
                id=int(input("Digite o ID que quer deletar: "))
                resultado=modulo_despesas.excluir_despesa(id, despesas)
                if resultado==0:
                    print("Algum erro ocorreu")
                else:
                    print("Deletado com sucesso")
            print("==================================================================")

        elif escolha == 3:
            despesas=modulo_despesas.ver_despesas(0)
            for i in range (1,len(despesas)):
                print("=============================================================================================================")
                print(f"Data: {despesas[i][0]} | Tipo: {despesas[i][1]} | Custo: R${despesas[i][2]} | Nome: {despesas[i][3]} | Usuario: {despesas[i][4]}")
            print("=============================================================================================================")
        
        elif escolha == 4:
            print("==================================================================")
            data=input("Digite a data conforme o exemplo: (19-07-2021): ")
            despesas=modulo_despesas.ver_despesas(data)
            if despesas == 0:
                print("==================================================================")
                print("Data não encontrada")
            else:
                for i in range (0, len(despesas)):
                    print("=============================================================================================================")
                    print(f"Data: {despesas[i][0]} | Tipo: {despesas[i][1]} | Custo: R${despesas[i][2]} | Nome: {despesas[i][3]} | Usuario: {despesas[i][4]}")
            print("=============================================================================================================")

        elif escolha == 5:
            print("==================================================================")
            nome=input("Digite o nome do usuario: ")
            despesas=modulo_despesas.ver_despesas(nome)
            if despesas == 0:
                print("==================================================================")
                print("Usuario não encontrado")
            else:
                for i in range (0, len(despesas)):
                    print("=============================================================================================================")
                    print(f"Data: {despesas[i][0]} | Tipo: {despesas[i][1]} | Custo: R${despesas[i][2]} | Nome: {despesas[i][3]} | Usuario: {despesas[i][4]}")
            print("=============================================================================================================")

        elif escolha == 6:
            print("==================================================================")
            opcao=int(input("Oque deseja editar?\n1 - Tipo\n2 - Custo\n3 - Nome\n4 - Usuario\n"))
            data=input("Digite a data conforme o exemplo: (19-07-2021):\n")
            despesas=modulo_despesas.editar_despesas1(data)
            if despesas == 0:
                print("==================================================================")
                print("Data não encontrada")
                pass
            else:
                for i in range (0, len(despesas)):
                    print("==================================================================")
                    print(f"ID: {i+1} | Data: {despesas[i][0]} | Tipo: {despesas[i][1]} | Custo: R${despesas[i][2]} | Nome: {despesas[i][3]} | Usuario: {despesas[i][4]}")
                print("==================================================================")
                id=int(input("Digite o ID que quer alterar: "))
                novo_valor=input("Digite o novo valor: ")
                resultado=modulo_despesas.editar_despesas2(id, opcao, despesas, novo_valor)
                if resultado==0:
                    print("Algum erro ocorreu")
                else:
                    print("Editado com sucesso")
            print("==================================================================")


def produto(usuario):
    while True:
        print("Bem-Vindo a seção de produtos!")
        escolha = int(input("1 - Consultar produtos\n2 - Adicionar novo produto\n3 - Remover produto\n4 - Atualizar produto\n5 - Mostrar itens com estoque baixo\n6 - Mostrar itens com estoque alto\n7 - Listar todos os produtos\n0 - Retornar ao menu principal\nPorfavor selecione sua opção: "))
        if escolha == 0:
            print("==================================================================")
            menu(usuario)
            break
        elif escolha == 1:
            busca = input("Digite o nome do produto pelo qual deseja buscar: ")
            print("==================================================================")
            resultados = CRUD_produto.buscar_produto(busca)
            if not resultados:
                print("Nenhum produto encontrado!")
            else:
                for res in resultados:
                    print(res)
            print("==================================================================")
        elif escolha == 2:
            print("==================================================================")
            ordem = ["Descrição", "Quantidade", "Preço", "ID de categoria", "Nome", "ID de usuario","Preço de custo"]
            quantidade = int(input("Quantos produtos você deseja adicionar? "))
            for i in range(quantidade):
                novo_produto_info = []
                print("Digite as informações do produto")
                for campo in ordem:
                    valor = input(f"Informe {campo} do produto: ")
                    novo_produto_info.append(valor)
                novo_id = CRUD_produto.adicionar_produto(novo_produto_info, usuario)
                print(f"Produto de id: '{novo_id}' adicionado com sucesso!")
            print("==================================================================")
        elif escolha == 3:
            print("==================================================================")
            deletar = int(input("Digite o ID do produto a ser deletado ou digite 0 para cancelar: "))
            if deletar != 0:
                if CRUD_produto.deletar_produto(deletar):
                    print("Produto deletado com sucesso!")
                else:
                    print("ID inválida!")
            print("==================================================================")
        elif escolha == 4:
            print("==================================================================")
            id_produto = int(input("Digite o ID do produto a ser alterado ou digite 0 para cancelar: "))
            if id_produto != 0:
                elemento = int(input("Digite o elemento que deseja alterar\n1 - Preço\n2 - Quantidade\n3 - Nome\n4 - Descrição\n5 - ID de categoria\n"))
                novo_valor = None
                sucesso = False
                if elemento == 1:
                    novo_valor = int(input("Digite o novo preço: R$"))
                    sucesso = CRUD_produto.atualizar_produtos(id_produto, elemento, novo_valor)
                elif elemento == 2:
                    novo_valor = int(input("Digite a nova quantidade: "))
                    sucesso = CRUD_produto.atualizar_produtos(id_produto, elemento, novo_valor)
                elif elemento == 3:
                    novo_valor = input("Digite o novo nome: ")
                    sucesso = CRUD_produto.atualizar_produtos(id_produto, elemento, novo_valor)
                elif elemento == 4:
                    novo_valor = input("Digite a nova descrição: ")
                    sucesso = CRUD_produto.atualizar_produtos(id_produto, elemento, novo_valor)
                elif elemento == 5:
                    novo_valor = int(input("Digite o novo ID de categoria: "))
                    sucesso = CRUD_produto.atualizar_produtos(id_produto, elemento, novo_valor)
                if sucesso:
                    print("Produto alterado com sucesso!")
                else:
                    print("ID inválida!")
            print("==================================================================")
        elif escolha == 5:
            print("==================================================================")
            resultados = CRUD_produto.baixo_estoque()
            for res in resultados:
                print(res)
            print("==================================================================")
        elif escolha == 6:
            print("==================================================================")
            resultados = CRUD_produto.alto_estoque()
            for res in resultados:
                print(res)
            print("==================================================================")
        elif escolha == 7:
            print("==================================================================")
            resultados = CRUD_produto.listar_todos()
            for res in resultados:
                print(res + "\n")
            print("==================================================================")
        else:
            print("Escolha inválida!")

def menu(usuario):
    print("Olá, bem-vindo ao menu principal! Qual área você gostaria de acessar?")
    print("1 - Produtos\n2 - Vendas\n3 - Despesas\n4 - Relátorio\n5 - Logoff\n0 - Encerrar")
    escolha = int(input("Porfavor selecione sua opção: "))
    if escolha == 1:
        print("==================================================================")
        produto(usuario)
    elif escolha == 2:
        print("==================================================================")
        vendas(usuario)
    elif escolha == 3:
        print("==================================================================")
        despesas(usuario)
    elif escolha == 4:
        print("==================================================================")
        relatorio(usuario)
    elif escolha == 5:
        print("==================================================================")
        return 1
    elif escolha == 0:
        return 0
    else:
        print("Escolha inválida! Porfavor selecione uma opção válida!\n")
        menu(usuario)

def registrar():
    print("==================================================================")
    usuario=input("Digite o usuario:\n")
    senha=input("Digite a senha:\n")
    id=input("Digite o id do usuario:\n")
    resul=Login.registrar(usuario, senha, id)
    if resul == 1:
        print("==================================================================")
        print("Usuario ja cadastrado!")
    elif resul == 0:
        print("==================================================================")
        print("Usuario cadastrado com sucesso!")

def login():
    print("==================================================================")
    usuario=input("Digite o usuario:\n")
    senha=input("Digite a senha:\n")
    resul=Login.login(usuario, senha)
    if resul == 0:
        print("==================================================================")
        print("Login efetuado com sucesso!")
        print("==================================================================")
        return menu(usuario)
    elif resul == 1:
        print("Usuario ou senha incorretos!")

def menu_login():
    print("================================Bem-Vindo================================")
    opcao=int(input("Oque deseja fazer?\n1-Login\n2-Registrar novo usuario\n0-Sair\nDigite o numero da opção desejada:\n"))
    if opcao==1:
        opcao=login()
    elif opcao==2:
        registrar()
    else:
        print("==================================================================")
        print("Valor invalido")
    if opcao==0:
        return 0
    menu_login()

Login