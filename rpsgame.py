import random
while True:

    choices = ["pedra","papel","tesoura"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("Pedra, papel ou tesoura?").lower()
    if player == computer:
        print("O computador escolheu", computer)
        print("O jogador escolheu", player)
        print("O jogo empatou")
    elif player == "pedra":
        if computer == "papel":
            print("O computador escolheu", computer)
            print("O jogador escolheu", player)
            print("Você perdeu!")
        if computer == "tesoura":
            print("O computador escolheu", computer)
            print("O jogador escolheu", player)
            print("Você ganhou!")
    elif player == "papel":
        if computer == "tesoura":
            print("O computador escolheu", computer)
            print("O jogador escolheu", player)
            print("Você perdeu!")
        if computer == "pedra":
            print("O computador escolheu", computer)
            print("O jogador escolheu", player)
            print("Você ganhou!")
    elif player == "tesoura":
        if computer == "pedra":
            print("O computador escolheu", computer)
            print("O jogador escolheu", player)
            print("Você perdeu!")
        if computer == "papel":
            print("O computador escolheu", computer)
            print("O jogador escolheu", player)
            print("Você ganhou!")

    play_again = input("Quer jogar novamente? (Sim/Não)").lower()
    if play_again != "sim":
        break
print("Adeus! \nFoi bom jogar com você!")