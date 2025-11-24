import utils
from questao1 import check_float


def adjustment():
    print("""
----------- Reajuste de salário -------------
|  Insira o valor de um salário para que o  |
|  programa apresente o mesmo após reajuste |
|       da inflação no valor de 10%.        |
---------------------------------------------""")
    utils.pause()
    utils.clear_console()
    num = input("Insira o valor atual do salário: R$")
    if check_float(num):
        global num_float
        num_float = float(num)
        if utils.check_zero(num_float, num_float):
            print(f"""
Salário atual: {num_float}
Salário após reajuste de 10%: {num_float + (num_float * 0.1)}""")
            utils.pause()
            if utils.loop():
                adjustment()
        else:
            print(f"""
Número inválido!
Por favor, insira um valor de salário válido.""")
            utils.pause()
            if utils.loop():
                adjustment()
    else:
        adjustment()