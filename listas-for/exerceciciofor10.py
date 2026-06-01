import random

numero_secreto = random.randint(1, 20)

print("--- Jogo da Adivinhação ---")

palpite = int(input("Digite um número entre 1 e 20: "))

while palpite != numero_secreto:
    if palpite < numero_secreto:
        print("O número secreto é maior!")
    else:
        print("O número secreto é menor!")

    palpite = int(input("Tente novamente: "))

print("Parabéns! Você acertou!")
print("Número secreto:", numero_secreto)    