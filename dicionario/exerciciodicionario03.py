dicionario_de_quadrados = {}

for i in range(1,6):
    dicionario_de_quadrados.setdefault(i, i**2)
#print(dicionario_de_quadrados)

for k, v in dicionario_de_quadrados.items():
        print(f"{k} -> {v}")