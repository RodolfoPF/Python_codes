import random

def jogar():
    user = input("Qual a sua escolha? 'pe' para pedra, 'pa' para papel e 'te' para tesoura. \n")
    computer = random.choice(["pe", "pa", "te"])

    if user == computer:
        return "Empate"

    if venceu(user, computer):
        return "Você venceu"
    
    return  "Você Perdeu"

def venceu(jogador, oponente):
    if (jogador == "pe" and oponente == "te") or (jogador == "te" and oponente == "pa") or (jogador == "pa" and oponente == "pe"):
        return True

print(jogar())