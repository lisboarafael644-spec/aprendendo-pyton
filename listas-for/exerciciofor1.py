listaNumeros = []

print("----- O Analista de Numeros -----")

while len(listaNumeros) < 6:
    numero = int(input("Digite um numero: "))
    listaNumeros.append(numero)

soma = 0
maior = listaNumeros[0]
menor = listaNumeros[0]

for numero in listaNumeros:
    soma = soma + numero

    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero

print("\nLista completa:", listaNumeros)
print("Soma dos valores:", soma)
print("Maior valor:", maior)
print("Menor valor:", menor)