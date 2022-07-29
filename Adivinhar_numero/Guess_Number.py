import random

def adivinhar(x):
    random_number = random.randint(1, x)
    adivinhar = 0
    while adivinhar != random_number:
        adivinhar = int(input(f"Adivinhe o número entre 1 e {x}. \n"))
        if adivinhar < random_number:
            print("Desculpe, seu chute foi baixo.")
        elif adivinhar > random_number:
            print("Desculpe, seu chute foi alto.")
    print(f"Dalé, você acertou o número! \nEra {adivinhar}")

x = int(input("Digite um número máximo: "))
adivinhar(x)