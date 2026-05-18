ano_atual = 2026
ano_nacimento = int(input("Ano de Nacimento"))

idade = ano_atual -ano_nacimento
if idade < 18:
    print("menor de idade")
elif idade < 60:
    print("adulto")
else:
    print("Idoso")