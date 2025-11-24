import utils
from questao1 import check_float


def discount():
    print("""
-------------- Desconto ---------------
|  Insira o valor de um produto para  |
|   que o programa apresente o mesmo  |
|   com 10%, 20% e 50% de desconto.   |
---------------------------------------""")
    utils.pause()
    utils.clear_console()
    num = input("Insira o valor de um produto: R$")
    if check_float(num):
        global num_float
        num_float = float(num)
        if utils.check_zero(num_float, num_float):
            disc_10 = num_float *0.1
            print(f"""
Você inseriu: {num_float}
R${num_float} com 10% de desconto é: {num_float - disc_10}
R${num_float} com 20% de desconto é: {num_float - (disc_10 * 2)}
R${num_float} com 50% de desconto é: {num_float / 2}""")
            utils.pause()
            if utils.loop():
                discount()
        else:
            print(f"""
Número inválido!
Não é possível tirar porcentagem de zero.""")
            utils.pause()
            if utils.loop():
                discount()
    else:
        discount()