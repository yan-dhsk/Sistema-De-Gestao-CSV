import CRUD_produto

def vendas():
    print("Sentimos muito, esta área ainda esta em desenvolvimento!")
    print("==================================================================")
    menu()

def relatorio():
    print("Sentimos muito, esta área ainda esta em desenvolvimento!")
    print("==================================================================")
    menu()

def despesas():
    print("Sentimos muito, esta área ainda esta em desenvolvimento!")
    print("==================================================================")
    menu()

def backup():
    print("Sentimos muito, esta área ainda esta em desenvolvimento!")
    print("==================================================================")
    menu()

def produto():
    while True:
        print("Bem-Vindo a seção de produtos!")
        escolha = int(input("1 - Consultar produtos\n2 - Adicionar novo produto\n3 - Remover produto\n4 - Atualizar produto\n5 - Mostrar itens com estoque baixo\n6 - Mostrar itens com estoque alto\n7 - Listar todos os produtos\n0 - Retornar ao menu principal\nPorfavor selecione sua opção: "))
        if escolha == 0:
            print("==================================================================")
            menu()
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
            ordem = ["Descrição", "Quantidade", "Preço", "ID de categoria", "Nome", "ID de usuario"]
            quantidade = int(input("Quantos produtos você deseja adicionar? "))
            for i in range(quantidade):
                novo_produto_info = []
                print("Digite as informações do produto")
                for campo in ordem:
                    valor = input(f"Informe {campo} do produto: ")
                    novo_produto_info.append(valor)
                novo_id = CRUD_produto.adicionar_produto(novo_produto_info)
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

def menu ():
    print("Olá, bem-vindo ao menu principal! Qual área você gostaria de acessar?")
    print("1 - Produtos\n2 - Vendas\n3 - Despesas\n4 - Relátorio\n5 - Backup\n0 - Encerrar")
    escolha = int(input("Porfavor selecione sua opção: "))
    if escolha == 1:
        print("==================================================================")
        produto()
    elif escolha == 2:
        print("==================================================================")
        vendas()
    elif escolha == 3:
        print("==================================================================")
        despesas()
    elif escolha == 4:
        print("==================================================================")
        relatorio()
    elif escolha == 5:
        print("==================================================================")
        backup()
    elif escolha == 0:
        return 0
    else:
        print("Escolha inválida! Porfavor selecione uma opção válida!\n")
        menu()

menu()