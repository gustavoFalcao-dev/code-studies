import utils


def dtm():
    print("""
------------- DTM --------------
| Insira um número para que o  |
| programa apresente o Dobro,  |
| o Triplo e a Metade do mesmo |
--------------------------------""")
    utils.pause()
    utils.clear_console()
    num = input("Insira um número: ")
    if utils.check_if_digit(num):
        global num_int
        num_int = int(num)
        if utils.check_zero(num_int, num_int):
            print(f"""
Você inseriu: {num_int}
O dobro de {num_int} é: {num_int * 2}
O triplo de {num_int} é: {num_int * 3}
A metade de {num_int} é: {num_int / 2}""")
            utils.pause()
            if utils.loop():
                dtm()
        else:
            print(f"""
Você inseriu: {num_int}
O dobro de {num_int} é: {num_int * 2}
O triplo de {num_int} é: {num_int * 3}
A metade de zero não é definida.""")
            utils.pause()
            if utils.loop():
                dtm()
    else:
        dtm()