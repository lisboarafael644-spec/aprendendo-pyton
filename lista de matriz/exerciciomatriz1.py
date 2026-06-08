estoque = [
    [12, 5, 8],
    [3, 15, 2],
    [19, 0, 7]
]

entrada = input("Digite a prateleira e a divisória: ")
prateleira, divisora = entrada.split(",")

prateleira = int(prateleira)
divisora = int(divisora)

print("Quantidade de caixas:", estoque[prateleira][divisora])