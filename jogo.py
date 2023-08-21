import random

def jogadas(jogador1, respostaComputador, pontosComputador, pontosJogador, empate):
    if respostaComputador == "papel":
        if jogador1 == "papel":
            print("Empate")
            empate += 1
        elif jogador1 == "pedra": 
            pontosComputador += 1
        else:
            print("Jogador ganhou")
            pontosJogador += 1
    elif respostaComputador == "pedra":
        
        if jogador1 == "papel":
            print("Jogador ganhou")
            pontosJogador += 1
        elif jogador1 == "pedra":
            print("Empate")
            empate += 1
        else:
            print("Computador ganhou")
            pontosComputador += 1
    else:
        if jogador1 == "papel":
            print("Computador ganhou")
            pontosComputador += 1
        elif jogador1 == "pedra":
            print("Jogador ganhou")
            pontosJogador += 1
        else:
            print("Empate")
            empate += 1
    return pontosComputador, pontosJogador, empate

modo = int(input("Deseja jogar com 1 ou 2 jogadores: "))
while (modo != 1) and (modo != 2):
    print("ERRO!")
    modo = int(input("Digite 1 ou 2: "))

vezesJogo = int(input("Quantas rodadas você quer jogar (3 ou 5)? "))
while (vezesJogo != 3) and (vezesJogo != 5):
    print("ERRO!")
    vezesJogo = int(input("Digite 3 ou 5: "))

pontosComputador = 0
pontosJogador = 0
empate = 0

if modo == 1:
    nome1 = input("Nome do jogador: ")
    nome2 = "computador"
    for i in range(vezesJogo):
        jogador1 = input("Digite Pedra, Papel ou Tesoura: ").lower()
        while jogador1 not in ("pedra", "papel", "tesoura"):
            print("Erro! Digite uma opção válida")
            jogador1 = input("PEDRA, PAPEL OU TESOURA: ").lower()
        jogadaCom = random.choice(["pedra", "papel", "tesoura"])
        print(f"Computador jogou: {jogadaCom}")
        pontosComputador, pontosJogador, empate = jogadas(jogador1, jogadaCom, pontosComputador, pontosJogador, empate)
else:
    nome1 = input("Nome do primeiro jogador: ")
    nome2 = input("Nome do segundo jogador: ")
    for i in range(vezesJogo):
        jogador1 = input(f"{nome1} - Digite Pedra, Papel ou Tesoura: ").lower()
        while jogador1 not in ("pedra", "papel", "tesoura"):
            print("Erro! Digite uma opção válida")
            jogador1 = input("PEDRA, PAPEL OU TESOURA: ").lower()
        jogador2 = input(f"{nome2} - Digite Pedra, Papel ou Tesoura: ").lower()
        while jogador2 not in ("pedra", "papel", "tesoura"):
            print("Erro! Digite uma opção válida")
            jogador2 = input("PEDRA, PAPEL OU TESOURA: ").lower()
        pontosComputador, pontosJogador, empate = jogadas(jogador1, jogador2, pontosComputador, pontosJogador, empate)

print(f"\nResultado final:")
print(f"{nome1}: {pontosJogador} pontos")
print(f"{nome2}: {pontosComputador} pontos")
print(f"Empates: {empate}")