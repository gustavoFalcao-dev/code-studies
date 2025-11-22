import os
from main import check_if_digit, clear_console


def soma(a,b):
    clear_console()
    print(f"A soma de {a} com {b} é igual a {a + b}")

def sub(a,b):
    clear_console()
    print(f"A subtração de {a} por {b} é igual a {a - b}")

def multi(a,b):
    clear_console()
    print(f"A multiplição de {a} por {b} é igual a {a * b}")
#TODO Adicionar try/except por causa do zero
def div(a,b):
    clear_console()
    print(f"A divisão de {a} por {b} é igual a {a / b}")

def res_div(a,b):
    clear_console()
    print(f"O resto da divisão de {a} por {b} é igual a {a % b}")

def options():
    lista = [soma, div, sub, multi, res_div]
#TODO Reduzir pra um print só por causa do processamento
    print("--------- Selecione a operação ---------")
    print("1- Adição ...........................(+)")
    print("2- Divisão ..........................(/)")
    print("3- Subtração ........................(-)")
    print("4- Multiplicação ....................(*)")
    print("5- Resto da divisão .................(%)")
    print("----------------------------------------")
    operator = input("Resposta: ")
    check_if_digit(operator)
    if check_if_digit(operator):
        operator_int = int(operator)
        lista[operator_int - 1](num1,num2)
    else:
        print("Opção inválida!")
        print("Por favor insira um número inteiro válido.")
        os.system('pause')
        clear_console()
        options()

def calc():
    global num1 
    global num2
    num1 = float(input("Insira o primeiro número: "))
    num2 = float(input("Insira o segundo número: "))
    clear_console()
    options()