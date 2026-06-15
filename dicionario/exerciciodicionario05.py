contagens = {}

frase = input("Digite uma frase: ").split()

for i in frase:
    if i not in contagens:
        contagens[i] = 1
    else:
        contagens[i] += 1

print(contagens)