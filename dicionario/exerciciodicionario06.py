from email.policy import default

estoque = {"teclado":15, "mouse":22, "monitor":8}

while True:
    nome, quatidade = input("digite o nome do produto que voce deseja comprar e a quantidade separdos: ").split(",")

    retorno = estoque.get(nome , "produto nao encontrado")

    for chave, valor in estoque.items():
        if nome == chave:
            estoque[chave] -= quatidade

    print("estoque atualizado")
    for chave, valor in estoque
