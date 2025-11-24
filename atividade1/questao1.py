import utils


def soma(floatA,floatB):
    utils.clear_console()
    print(f"A soma de {floatA} com {floatB} é igual a {floatA + floatB}")

def sub(floatA,floatB):
    utils.clear_console()
    print(f"A subtração de {floatA} por {floatB} é igual a {floatA - floatB}")

def multi(floatA,floatB):
    utils.clear_console()
    print(f"A multiplição de {floatA} por {floatB} é igual a {floatA * floatB}")

def div(floatA,floatB):
    utils.clear_console()
    if utils.check_zero(floatA,floatB):
        print(f"A divisão de {floatA} por {floatB} é igual a {floatA / floatB}")
    else:
        print(f"Divisão por 0 não é aceita.")

def res_div(floatA,floatB):
    utils.clear_console()
    if utils.check_zero(floatA,floatB):
        print(f"O resto da divisão de {floatA} por {floatA} é igual a {floatA % floatB}")
    else:
        print("Divisão por 0 não é permitida.")

def check_float(num):
    try:
        float(num)
        return True
    except:
        return False


def options(floatA,floatB):
    lista = [soma, div, sub, multi, res_div]
    print("""
---------- Selecione a operação ----------
|1- Adição ...........................(+)|
|2- Divisão ..........................(/)|
|3- Subtração ........................(-)|
|4- Multiplicação ....................(*)|
|5- Resto da divisão .................(%)|
------------------------------------------""")
    operator = input("Resposta: ")
    if utils.check_if_digit(operator):
        operator_int = int(operator)
        lista[operator_int - 1](floatA,floatB)
        utils.pause()
#TODO create option to reuse the same numbers
    else:
        print("""
Opção inválida!
Por favor, insira um número inteiro válido.""")
        utils.pause()
        utils.clear_console()
        options()

def calc():
    print("""
---------- Calculadora de dois números -----------
|   Insira dois números decimais e em seguida    |
|  selecione qual operador você deseja utilizar  |
|                   nessa conta                  |
--------------------------------------------------""")
    utils.pause()
    utils.clear_console()
    num1 = input("Insira o primeiro número: ")
    if check_float(num1):
        numf1 = float(num1)
        num2 = input("Insira o segundo número: ")
        if check_float(num2):
            numf2 = float(num2)
            utils.clear_console()
            options(numf1,numf2)
            if utils.loop():
                calc()
        else:
            print(f"""
Número inválido!
{num2} não é um número com
casas decimais. Por favor,
tente novamente.""")
    else:
        print(f"""
Número inválido!
{num1} não é um número com
casas decimais. Por favor,
tente novamente.""")