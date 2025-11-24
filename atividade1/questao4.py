import utils


def mean():
    print("""
""")
    lista = []
    counter = 1
    term = "xxx" 
    while term != "00":
        term = input(f"Insira o {counter}º número (digite '00' para terminar): ")
        if utils.check_if_digit(term):
            value = int(term)
            lista.append(value)
            if (counter % 5) == 0:
                utils.clear_console()
            counter += 1
        else:
            mean()
    lista.pop()
    list_sum = int(sum(lista))
    items = len(lista)
    result = list_sum / items
    print(f"""
Voce inseriu os números:
{lista}
A média aritmética desses números é: {result}""")
    utils.pause()
    if utils.loop():
        mean()