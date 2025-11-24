import utils

def ant_suc():
    print("""
------- Antecessor e Sucessor -------
|    Digite um número para que o    |
|   programa responda mostrando o   |
| antecessor e o sucessor do mesmo. |
-------------------------------------""")
    utils.pause()
    utils.clear_console()
    answer = input("Insira um número inteiro: ")
    utils.check_if_digit(answer)
    if utils.check_if_digit(answer):
        answer_int = int(answer)
        utils.clear_console()
        print(f"""
Você inseriu o número: {answer_int}
Seu antecessor é: {answer_int -1}
Seu sucessor é: {answer_int + 1}""")
        utils.pause()
        if utils.loop():
            ant_suc()
    else:
        print(f"""
Número inválido!
Você inseriu {answer} que não 
corresponde a um número inteiro válido.""")
        utils.pause()
        if utils.loop():
            ant_suc()