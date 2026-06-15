produtos = {
    "macarrao": 25.90,
    "feijao": 9.50,
    "arroz": 6.75,
}

produto = input("digite o nome do produto:").lower()
if produto in produtos:
    print("preço R$",produtos[produto])
else:
    print("produto nao encontrado")
    continue
if valor < 