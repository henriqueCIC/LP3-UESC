import random

def jogar_dados():
    return random.randint(1, 6)

def main():
    dado01 = jogar_dados()
    dado02 = jogar_dados()
    pontos = dado01 + dado02

    print(f"Dado 01: {dado01}, Dado 02: {dado02}")
    print(f"Pontos: {pontos}")

    if pontos in (7, 11):
        print("VOCÊ GANHOU!!!")
        return

    if pontos in (2, 3, 12):
        print("PERDEU!!!")
        return

    print("PRÓXIMA FASE!")

    contador = 0
    while True:
        contador += 1

        dado01 = jogar_dados()
        dado02 = jogar_dados()
        soma = dado01 + dado02

        print(f"Dado 1: {dado01}, Dado 2: {dado02}")
        print(f"Jogada {contador}: {soma}")

        if soma == 7:
            print("VOCÊ PERDEU!!!")
            return

        if soma == pontos:
            print("VOCÊ GANHOU!!!")
            return

if __name__ == "__main__":
    main()
