import csv
import Main

def login():
    print("==================================================================")
    usuario=input("Digite o usuario:\n")
    senha=input("Digite a senha:\n")
    with open("contas.csv", "r", encoding="utf-8") as arquivo:
        lista = list(csv.reader(arquivo, delimiter=','))
    for x in range (1, len(lista)):
        if lista[x][0]==usuario:
            if lista[x][1]==senha:
                print("==================================================================")
                print("Login efetuado com sucesso!")
                print("==================================================================")
                Main.menu()
    print("Usuario ou senha nao cadastrados!")


def registrar():
    print("==================================================================")
    usuario=input("Digite o usuario:\n")
    senha=input("Digite a senha:\n")
    id=input("Digite o id do usuario:\n")
    with open("contas.csv", "r", encoding="utf-8") as arquivo:
        lista = list(csv.reader(arquivo, delimiter=','))
    for x in range (1, len(lista)):
        if lista[x][0]==usuario:
            print("==================================================================")
            print("Usuario ja cadastrado!")
            break
    lista.append(f"{usuario}{senha}{id}")
    with open("contas.csv", "w", encoding="utf-8", newline="") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerows(lista)
        print("Usuario cadastrado com sucesso!")
        
            
opcao=5
while opcao!=0:
    print("==================================================================")
    opcao=int(input("Oque deseja fazer?\n1-Login\n2-Registrar novo usuario\n0-Sair\nDigite o numero da opção desejada:\n"))
    if opcao==1:
        login()
    elif opcao==2:
        registrar()