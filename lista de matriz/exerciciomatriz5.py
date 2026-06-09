print("---------------------")
print("batalha naval")
print("---------------------")
oceano = [
    ["~", "~", "~", "~"],
    ["~", "~", "N", "~"],
    ["~", "~", "~", "~"],
    ["~", "~", "~", "~"]
]

while True:
    linha = int(input("Digite a linha (0 a 3): "))
    coluna = int(input("Digite a coluna (0 a 3): "))

    if oceano[linha][coluna] == "N":
        print("Você afundou o navio!")
        break
    else:
        print("Água")

