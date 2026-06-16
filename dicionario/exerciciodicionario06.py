estoque = {"teclado":15, "mouse":22, "monitor":8}
selecao = {}
print(estoque)
atulaliza_estoque = False
continuar = "s"
while continuar == "s":
    nome, quatidade = input("digite o nome do produto que voce deseja comprar e a quantidade separdos por virgular: ").split(",")

    retorno = estoque.get(nome , "produto nao encontrado")

    for chave, valor in estoque.items():
        if nome.lower() == chave.lower():
            if valor == 0:
                print("estoque esgotado")
                continue
            if valor < int(quatidade):
                print("estoque insuficiente")
                continue
            else:
                estoque[chave] -= int(quatidade)
                atulaliza_estoque = True

        if atulaliza_estoque:
            print("estoque atualizado")
            for chave, valor in estoque.items():
                print(f"{chave} : {valor}")
