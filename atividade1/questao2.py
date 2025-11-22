from main import check_if_digit

def ant_suc():
    answer = input("Insira um número inteiro: ")
    check_if_digit(answer)
    if check_if_digit(answer):
        print(f"O antecessor e sucessor de {answer} são (respectivamente): {answer - 1} e {answer + 1}")
    else:
        print(f"Número inválido!")
        print(f"Você inseriu {answer} que não corresponde a ")