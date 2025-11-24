import utils
from questao1 import calc
from questao2 import ant_suc
from questao3 import dtm
from questao4 import mean
from questao5 import discount
from questao6 import adjustment
from questao7 import odd_even
#TODO update float checks to entry with ","


def qst1():
    calc()

def qst2():
    ant_suc()

def qst3():
    dtm()

def qst4():
    mean()

def qst5():
    discount()

def qst6():
    adjustment()

def qst7():
    odd_even()

def main():
    print("""
---------- Questões da primeira atividade ----------
|1 - Questão 1                                     |
|2 - Questão 2                                     |
|3 - Questão 3                                     |
|4 - Questão 4                                     |
|5 - Questão 5                                     |
----------------------------------------------------""")
    check_selection = input("Resposta: ")
    utils.clear_console()
    utils.check_if_digit(check_selection)
    if utils.check_if_digit(check_selection):
        selection = int(check_selection)
        lista[selection - 1]()
    else:
        print("""
Opção inválida!
Por favor insira um número inteiro válido.""")

def loop_main():
    print("Deseja testar o código de outra questão? (S/N)")
    answer = input("Resposta: ")
    if answer == "s" or answer == "S":
        utils.clear_console()
        main()
    elif answer == "n" or answer == "N":
        end()
    else:
        print("""
Opção inválida!
Por favor, tente novamente.""")

def end():
    utils.clear_console()
    print("""
Obrigado por testar!
Se encontrou algum erro ou tiver alguma sugestão, 
as informações de contato estão no github: 
https://github.com/gustavoFalcao-dev""")
    utils.pause()
    utils.clear_console()


lista = [qst1, qst2, qst3, qst4, qst5, qst6, qst7, end]
main()
loop_main()