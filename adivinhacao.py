import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1, 101)
total_de_tentativas = 0
pontos = 1000
nivel = 0

nivel = int(input("Escolha o nível de dificuldade (1-Fácil | 2-Médio | 3-Difícil): "))

if (nivel == 1):
    total_de_tentativas = 20
elif (nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

# rodada = 1
# while (rodada <= total_de_tentativas):
for rodada in range(1,(total_de_tentativas + 1)):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite o seu número: ")
    print("Você digitou", chute_str)
    chute = int(chute_str)

    if (chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto

    if (acertou):
        print("Você acertou e fez {} pontos!".format(pontos))
        break
    elif(maior):
        print("Você errou! O seu chute foi maior que o número secreto.")
    else:
        print("Você errou! O seu chute foi menor que o número secreto.")
    pontos_perdidos = abs(numero_secreto - chute)
    pontos = pontos - pontos_perdidos
    # rodada = rodada + 1

print("O número secreto era {}".format(numero_secreto))
print("Fim do jogo")