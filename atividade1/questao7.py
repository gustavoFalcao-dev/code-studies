import utils

def odd_even():
    print("""
--------------- Ímpar ou par ---------------
|       Digite um número para que o        |
|     programa responda mostrando se o     |
|           mesmo é ímpar ou par.          |
--------------------------------------------""")
    utils.pause()
    utils.clear_console()
    answer = input("Insira um número inteiro: ")
    utils.check_if_digit(answer)
    if utils.check_if_digit(answer):
        answer_int = int(answer)
        utils.clear_console()
        if (answer_int % 2) != 0:
            print(f"""
Você inseriu o número: {answer_int}
que é um número ímpar.""")
            utils.pause()
            if utils.loop():
                odd_even()
        else:
            print(f"""
Você inseriu o número: {answer_int}
que é um número par.""")
            utils.pause()
            if utils.loop():
                odd_even()
    else:
        print(f"""
Número inválido!
Você inseriu {answer} que não 
corresponde a um número inteiro válido.""")
        utils.pause()
        if utils.loop():
            odd_even()