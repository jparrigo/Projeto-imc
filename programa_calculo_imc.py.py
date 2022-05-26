#PROGRAMA DE CALCULAR IMC E CONSUMO CALORICO

#--------------------------------------------------------------------------------------------------------------------------------------------------------
#-- VARIABLES
#--------------------------------------------------------------------------------------------------------------------------------------------------------
from os import system
from time import sleep
from tracemalloc import stop
from datetime import datetime
import mysql.connector
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-- LISTA
#-----------------------------------------------------------------------------------------------------------------------------------------------
login = []
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-- Conexão com o Banco de Dados
#-----------------------------------------------------------------------------------------------------------------------------------------------
db = mysql.connector.connect(user='root', host='localhost', database='imc')

cursor = db.cursor()
#--------------------------------------------------------------------------------------------------------------------------------------------------------
#-- FUNÇÃO EXTRA
#--------------------------------------------------------------------------------------------------------------------------------------------------------
def cleartime():
    system("cls")

def returnmenu():
    ld = 1
    while ld <= 3:
        system("cls")
        print("Retornando ao menu" + "."*ld)
        sleep(1)
        ld += 1
    menu()

def loading():
    ld = 1
    while ld <= 3:
        system("cls")
        print("Carregando" + "."*ld)
        sleep(1)
        ld += 1

def exit():
    ld = 1
    while ld <= 3:
        system("cls")
        print("Desconectando" + "."*ld)
        sleep(1)
        ld += 1
#--------------------------------------------------------------------------------------------------------------------------------------------------------
#-- FUNÇÃO IMC
#--------------------------------------------------------------------------------------------------------------------------------------------------------
def imc():
    cleartime()
    try:
        data = datetime.today().strftime('%Y-%m-%d')
        peso = int(input("Qual o seu PESO em quilogramas? "))
        altura = int(input("Qual a sua ALTURA em centímetros? "))
        
        resultado = peso / ((altura/100) ** 2)
        cleartime()
        if resultado <= 18.5:
            print(f"Seu IMC é {int(resultado)} e você está abaixo do peso")
        elif resultado <= 25.0:
            print(f"Seu IMC é {int(resultado)} e você está com o peso normal")
        elif resultado <= 30:
            print(f"Seu IMC é {int(resultado)} e você está com sobre peso")
        elif resultado <= 35:
            print(f"Seu IMC é {int(resultado)} e você está com Obesidade Grau 1")
        elif resultado <= 40:
            print(f"Seu IMC é {int(resultado)} e você está com Obesiade Grau 2")
        else:
            print(f"Seu IMC é {int(resultado)} e você está com Obesidade Grau 3 ou Mórbida")

        cursor.execute(f"INSERT INTO dados (fk_nome_contas,altura_dados,peso_dados,imc_dados,data_dados) VALUES ('{login[0]}','{altura}','{peso}','{resultado}','{data}')")
        db.commit()

        input("\nPressione ENTER para retornar ao menu inicial.")
        returnmenu()
    except:
        cleartime()
        print("Digite apenas números!")
        sleep(2)
        imc()
#--------------------------------------------------------------------------------------------------------------------------------------------------------
#-- FUNÇÃO DE CALORIAS
#--------------------------------------------------------------------------------------------------------------------------------------------------------
def caloria():
    cleartime()
    notes = ["Café da Manha", "Café","Almoço","Café da Tarde","Jantar","Ceia"]
    tabela = []
    print(
    "Escolha o sexo"
    "\nMasculino (M) ou Feminino (F)"
    )
    s = str(input("Digite aqui: ").upper())
    cleartime()

    try:
        idade = int(input("Qual a sua IDADE? "))
        peso = int(input("\nQual o seu PESO (kg)? "))
    except:
        cleartime()
        print("Apenas números inteiros!")
        sleep(2)
        caloria()

    if idade < 0 or idade < 0:
        cleartime()
        print("Apenas números postivos!")
        sleep(2)
        caloria()

    gastom1 = (59.512 * peso) - 30.4 #0 a 3 anos
    gastom2 = (22.706 * peso) + 504.3 #3 a 10 anos
    gastom3 = (17.686 * peso) + 658.2 #10 a 18 anos
    gastom4 = (15.057 * peso) + 692.2 #18 a 30 anos
    gastom5 = (11.472 * peso) + 873.1 #30 a 60 anos
    gastom6 = (11.711 * peso) + 587.7 # maior do que 60 anos

    gastof1 = (58.317 * peso) - 31.1 #0 a 3 anos
    gastof2 = (20.315 * peso) + 485.9 #3 a 10 anos
    gastof3 = (13.384 * peso) + 692.6 #10 a 18 anos
    gastof4 = (14.818 * peso) + 486.6 #18 a 30 anos
    gastof5 = (8.126 * peso) + 845.6 #30 a 60 anos
    gastof6 = (9.082 * peso) + 658.5 #maior do que 60 anos

    if 3 > idade >= 0:
        gastocal = gastom1
    elif 10 > idade >= 3:
        gastocal = gastom2
    elif 18 > idade >= 10:
        gastocal = gastom3
    elif 30 > idade >= 18:
        gastocal = gastom4
    elif 60 > idade >= 30:
        gastocal = gastom5
    else:
        gastocal = gastom6

    if 3 > idade >= 0:
        gastocal = gastof1
    elif 10 > idade >= 3:
        gastocal = gastof2
    elif 18 > idade >= 10:
        gastocal = gastof3
    elif 30 > idade >= 18:
        gastocal = gastof4
    elif 60 > idade >= 30:
        gastocal = gastof5
    else:
        gastocal = gastof6

    if s == "M":
        var = 0
        while var < 6:
            cleartime()
            number = int(input(f"Digite o consumo calorico de cada refeição ({notes[var]})\n: "))
            tabela.append(number)
            var += 1

            result = sum(tabela)

        cleartime()
        print(f"O seu consumo total foi de {int(result)} calorias no dia.")

        escolha = str(input(f"\nDeseja checar o seu consumo médio ({int(gastocal)})? (S) | (N)\n").lower())
        cleartime()

        if escolha == "s":
            if result == gastocal:
                print(f"Voce está na média, com {int(result)}")
            elif result > gastocal:
                print(f"Voce está acima da média, com {int(result - gastocal)} calorias a mais.")
            else:
                print(f"Voce está abaixo da média, com {int(gastocal - result)} calorias a menos.")
        else:
            returnmenu()

        input("\nPressione ENTER para retornar ao menu inicial.")
        returnmenu()

    if s == "F":
        var = 0
        while var < 6:
            cleartime()
            number = int(input(f"Digite o consumo calorico de cada refeição ({notes[var]})\n: "))
            tabela.append(number)
            var += 1

            result = sum(tabela)

        cleartime()
        print(f"O seu consumo total foi de {int(result)} calorias no dia.")

        escolha = str(input(f"\nDeseja checar o seu consumo médio ({int(gastocal)})? (S) | (N)\n").lower())
        cleartime()

        if escolha == "s":
            if result == gastocal:
                print(f"Voce está na média, com {int(result)}")
            elif result > gastocal:
                print(f"Voce está acima da média, com {int(result - gastocal)} calorias a mais.")
            else:
                print(f"Voce está abaixo da média, com {int(gastocal - result)} calorias a menos.")
        else:
            returnmenu()

        input("\nPressione ENTER para retornar ao menu inicial.")
        returnmenu()

    if s != "M" or s != "F":
        cleartime()
        print("Escolha Masculino (M) ou Feminino (F)")
        sleep(2)
        caloria()
#--------------------------------------------------------------------------------------------------------------------------------------------------------
#-- FUNÇÃO DE CREDITOS
#--------------------------------------------------------------------------------------------------------------------------------------------------------
def creditos():
    print(
    "Pessoas envolvidas nesse projeto:"
    "\n\nJoão Paulo Toledo de Almeida Arrigo"
    "\nBruno Fontolan Alves"
    "\nEnrico Ribeiro Farina"
    "\nMatheus Furlan Ferragut de Oliveira"
    "\nGustavo de Campos Soares"
    "\n\nAgradecimentos Especiais ao Professor e Mentor"
    "\nJosé Marcelo Traina Chacon"
    )   

    input("\nPressione ENTER para retornar ao menu inicial.")
    returnmenu()
#--------------------------------------------------------------------------------------------------------------------------------------------------------
#-- FUNÇÃO DE HISTÓRICO
#--------------------------------------------------------------------------------------------------------------------------------------------------------
def historico():
    loading()
    cursor.execute(f"SELECT * FROM dados WHERE fk_nome_contas='{login[0]}'")
    bancodedados = cursor.fetchall()

    if bancodedados:
        cleartime()
        print("{:<10} {:<10} {:<10} {:<10} {:<10}".format('Usuário', 'Altura', 'Peso', 'IMC', 'Data'))
        print("-"*50)
        for values in bancodedados:
            print("{:<10} {:<10} {:<10} {:<10} {:<10}".format(values[0], values[1], values[2], values[3], values[4]))
            print("-"*50)
    else:
        cleartime()
        print("Nenhum dado foi computado ainda.")

    input("\nPressione ENTER para retornar ao menu inicial.")
    returnmenu()
#--------------------------------------------------------------------------------------------------------------------------------------------------------
#-- FUNÇÃO DE RETORNAR AO MENU DE LOGIN
#--------------------------------------------------------------------------------------------------------------------------------------------------------
def returnlogin():
    cleartime()
    exit()
    login.clear()
    login_registro()
#--------------------------------------------------------------------------------------------------------------------------------------------------------
#-- MENU
#--------------------------------------------------------------------------------------------------------------------------------------------------------
def menu():
    try:
        cleartime()
        print(
        "=========================="
        "\n= 1- Calculo de IMC      ="
        "\n= 2- Calculo de Calorias ="
        "\n= 3- Histórico           ="
        "\n= 4- Creditos            ="
        "\n= 5- Sair                ="
        "\n==========================")
        escolha = int(input("Escolha um número acima: "))

        if escolha == 1:
            imc()
        elif escolha == 2:
            caloria()
        elif escolha == 3:
            historico()
        elif escolha == 4:
            cleartime()
            creditos()
        elif escolha == 5:
            cleartime()
            returnlogin()
        else:
            cleartime()
            print("Função Não Encontrada! Tente Novamente.")
            sleep(3)
            menu()
    except:
        cleartime()
        print("Apenas números interios!")
        sleep(3)
        menu()
#--------------------------------------------------------------------------------------------------------------------------------------------------------
#-- LOGIN E REGISTRO
#--------------------------------------------------------------------------------------------------------------------------------------------------------
def registrar():    
    cursor.execute("SELECT nome_contas, senha_contas FROM contas")
    bancodedados = cursor.fetchall()

    cleartime()

    Nome = str(input("Crie um nome de usuário: ")).lower()
    senha = str(input("Crie uma senha: "))
    senha_confirmar = str(input("Confirme a sua senha, por favor: "))

    for n in bancodedados:
        if Nome in n[0]:
            cleartime()
            print("Esse nome ja existe")
            sleep(3)
            registrar()

    if senha != senha_confirmar:
        cleartime()
        print("A confirmação de senha está incorreta. Por favor tente novamente.")
        sleep(3)
        registrar()

    if len(senha)< 5:
        cleartime()
        print("A sua senha é muito pequena, use pelo menos 5 caracteres para uma maior segurança.")
        sleep(3)
        registrar()
    else:
        cursor.execute(f"INSERT INTO contas (nome_contas,senha_contas) VALUES ('{Nome}','{senha}')")
        #cursor.execute(f"INSERT INTO dados (fk_nome_contas) VALUES ('{Nome}')")
        db.commit()
        cleartime()
        print("Dados gravados com sucesso.")
        sleep(3)
        login_registro()
#--------------------------------------------------------------------------------------------------------------------------------------------------------
#-- FUNÇÃO DE ACESSO
#--------------------------------------------------------------------------------------------------------------------------------------------------------
def acessar():
    Nome = str(input("Digite o seu nome de usuário: "))
    senha = str(input("Digite a sua senha: "))

    cursor.execute(f"SELECT nome_contas, senha_contas FROM contas WHERE nome_contas='{Nome}' AND senha_contas='{senha}'")
    bancodedados = cursor.fetchall()

    if bancodedados:
        loading()
        cleartime()
        print("Login Bem-Sucedido")
        print("Bem vindo,", Nome)
        login.append(Nome)
        sleep(2)
        menu()
    else:
        cleartime()
        print("Usuário e Senha não Encontrados!")
        sleep(3)
        login_registro()
#--------------------------------------------------------------------------------------------------------------------------------------------------------
#-- LOGIN REGISTRO
#--------------------------------------------------------------------------------------------------------------------------------------------------------
def login_registro():
    cleartime()
    print(
    "=========================="
    "\n= 1- Criar Conta       ="
    "\n= 2- Realizar o Login  ="
    "\n= 3- Fechar Programa   ="
    "\n========================")
    opcao = input("Escolha uma opção acima: ")
    if opcao == "1":
        cleartime()
        registrar()
    elif opcao == "2":
        cleartime()
        acessar()
    elif opcao == "3":
        stop
    else:
        print("Por favor escolha uma opção válida\n")
        login_registro()
#--------------------------------------------------------------------------------------------------------------------------------------------------------
#-- START
#--------------------------------------------------------------------------------------------------------------------------------------------------------
login_registro()