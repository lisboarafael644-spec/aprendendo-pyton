matriz_base = [[1, 2], [3, 4]]
fator = int(input("digite o fator de escala:"))
nova_matriz = []
for linha in matriz_base:
    nova_linha = []
    for numero in linha:
        nova_linha.append(numero * fator)

        nova_matriz.append(nova_linha)
    print("nova matriz:")
    for linha in nova_matriz:
      print(linha)