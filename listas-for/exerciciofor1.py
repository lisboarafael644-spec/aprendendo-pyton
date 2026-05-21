listaNumeros = []

for i in range(1,7):
    numero = int(input(f"Digite o {i}° numero:"))
    listaNumeros.append(numero)

listaNumeros.sort()
print(listaNumeros)

print(f"a soma é : {sum(listaNumeros)}")
print(f"o maior numero é : {max(listaNumeros)}")
print(" o menor numero é : {min(listaNumeros}")