import adivinhacao
import forca

print("*********************************")
print("***** Escolha o seu jogo ! ******")
print("*********************************")

opcao = int(input("1-Adivinhação | 2-Forca : "))

if (opcao == 1):
    adivinhacao.jogar()
elif (opcao == 2):
    forca.jogar()


