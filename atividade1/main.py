import os
from questao1 import calc


def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def check_if_digit(x):
    if x.isdigit():
        return True
    return False

def qst1():
    return calc

def qst2():
    return

def qst3():
    return

def qst4():
    return

def qst5():
    return

def qst6():
    return

def qst7():
    return

def main():
    print("--------- Questões da primeira atividade ---------")
    print("1 - Questão 1                                     ")
    print("2 - Questão 2                                     ")
    print("3 - Questão 3                                     ")
    print("4 - Questão 4                                     ")
    print("5 - Questão 5                                     ")
    print("--------------------------------------------------")
    check_selection = input()

    check_if_digit(check_selection)
    if check_if_digit(check_selection):
        lista = [qst1, qst2, qst3, qst4, qst5, qst6, qst7]
        selection = int(check_selection)
        lista[selection]()
    else:
        print("Opção inválida!")
        print("Por favor insira um número inteiro válido.")
def end():
    print("Obrigado por testar!")
    print("Se encontrou algum erro ou tiver alguma sugestão, entre em contato pelo email: luizgf2019@gmail.com")
#TODO Inserir link do github
    print("ou pelo github:")

main()
print("Deseja testar o código de outra questão? (S/N)")
answer = input("Resposta: ")
if answer == "s" or answer == "S":
    main()
elif answer == "n" or answer == "N":
    end()
else:
    print("Opção inválida!")
    print("Por favor insira uma resposta válida como 'S' para Sim\nou 'N' para Não.")