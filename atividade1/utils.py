import os


def pause():
    os.system('pause')

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def check_if_digit(num1):
    try:
        int(num1)
        return True
    except:
        clear_console()
        print("""
Número inválido!
O número inserido não corresponde
a um número inteiro válido.""")
        pause()
        if loop():
            return False

def loop():
    clear_console()
    print("Deseja inserir o(s) número(s) novamente? (S/N)")
    answer = input("Resposta: ")
    if answer == "s" or answer == "S":
        clear_console()
        return True
    elif answer == "n" or answer == "N":
        clear_console()
        return False
    else:
        clear_console()
        print("""
Opção inválida!
Por favor, tente novamente.""")
        pause()
        clear_console()
        loop()

def check_zero(num1,num2):   
    try:
        num1 / num2
        num1 % num2
        return True
    except:
        return False