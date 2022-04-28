#PROGRAMA DE CALCULAR IMC E CONSUMO CALORICO

from os import system
from time import sleep

def cleartime():
    system("cls")

def returnmenu():
    system("cls")
    print("Retornado ao menu ...")
    sleep(3)
    system("cls")
    menu()

def imc():
    peso = int(input("Qual o seu PESO em quilogramas? "))
    altura = float(input("Qual a sua ALTURA em metros? "))
    
    resultado = peso / (altura ** 2)
    cleartime()
    if resultado <= 18.5:
        print(f"Seu IMC é {int(resultado)} e você está com o abaixo do peso")
    elif resultado <= 25.0:
        print(f"Seu IMC é {int(resultado)} e você está com o peso normal")
    elif resultado <= 30:
        print(f"Seu IMC é {int(resultado)} e você está com o sobre peso")
    elif resultado <= 35:
        print(f"Seu IMC é {int(resultado)} e você está com o Obesidade Grau 1")
    elif resultado <= 40:
        print(f"Seu IMC é {int(resultado)} e você está com o Obesiade Grau 2")
    else:
        print(f"Seu IMC é {int(resultado)} e você está com o Obesidade Grau 3 ou Mórbida")

    input("\nPressione ENTER para retornar ao menu inicial.")
    returnmenu()

def menu():
    cleartime()
    print(
    "======================"
    "\n= 1- Calculo de IMC ="
    "\n======================"
    )
    escolha = int(input("Escolha um número acima: "))

    match escolha:
        case 1:
            cleartime()
            imc()
        case 2:
            print("EUUUU")


menu()