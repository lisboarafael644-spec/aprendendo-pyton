listaNumeros = []
print("----- O analista de numeros-----")
while len(listaNumeros) <6:
    numero = int (input("digite um numero:"))
    listaNumeros.append(numero)
soma  = 0
maior = listaNumeros
menor = listaNumeros
    soma = soma + numero
if numero > maior:
    maior = numero
    