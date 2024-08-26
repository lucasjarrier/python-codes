import random


def sortear_numero(totalizador):
    numero = random.randint(1, 10000)
    if 1 <= numero <= 10:
        premio = 1000
    elif 11 <= numero <= 100:
        premio = 100
    elif 101 <= numero <= 300:
        premio = 10
    elif 301 <= numero <= 1000:
        premio = 5
    else:
        premio = 0.5

    totalizador += premio - 2  # Decrementa $2 e adiciona o valor do prêmio
    print(f"Número sorteado: {numero}")
    print(f"Prêmio: {premio} dólares")
    print(f"Totalizador atual: {totalizador} dólares\n")
    return totalizador


def main():
    totalizador = 0  # Inicializa o totalizador com 0
    while True:
        print("Escolha uma opção:")
        print("1 - Sortear")
        print("2 - Exit")
        escolha = input("Digite o número da opção desejada: ")

        if escolha == "1":
            totalizador = sortear_numero(totalizador)
        elif escolha == "2":
            print("Saindo do programa.")
            print(f"Totalizador final: {totalizador} dólares")
            break
        else:
            print("Opção inválida. Tente novamente.\n")


if __name__ == "__main__":
    main()
