numeros = []
pares = []
impares = []

print("--- Separador de Pares e Ímpares ---")

while len(numeros) < 10:
    numero = int(input(f"Digite o {len(numeros) + 1} numero: "))
    numeros.append(numero)

for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print("\n--- Resultado ---")
print("Lista principal:", numeros)
print("Lista de pares:", pares)
print("Lista de impares:", impares)