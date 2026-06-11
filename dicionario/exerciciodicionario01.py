cadastro_simples = {
    "nome": "Rafael",
    "idade": 17,
    "cidade": "Sao Paulo",
}

for i, j in cadastro_simples.items():
    if i == "nome" or i == "cidade":
        print(i, j)