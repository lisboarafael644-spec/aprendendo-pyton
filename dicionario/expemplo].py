from email.policy import default

dados_pessoais = {
    "nome":"joao",
    "idade": 21,
    "sexo": "M",
    "altura": 1.70,
    "temCNH": True,

}
continuar = "s"
while continuar == "s":
    dados = input("digite oque voce quer encontrar:")
    print(dados_pessoais.get(dados, ))