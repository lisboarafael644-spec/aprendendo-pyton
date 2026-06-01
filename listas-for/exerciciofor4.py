maiores = 0
menores = 0
ano_atual = 2026

print("--- Verificador de Maioridade ---")

for i in range(7):
    ano_nascimento = int(input(f"Digite o ano de nascimento da {i + 1} pessoa: "))

    idade = ano_atual - ano_nascimento

    if idade >= 18:
        maiores = maiores + 1
    else:
        menores = menores + 1

print("\n--- Resultado Final ---")
print("Pessoas maiores de idade:", maiores)
print("Pessoas menores de idade:", menores)
