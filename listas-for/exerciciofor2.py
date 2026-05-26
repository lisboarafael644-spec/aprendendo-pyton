notas = []
print("---calculadora de Media---")

while len(notas) < 4:
    nota = float(input(f"digite a {len(notas) + 1} nota: "))
    notas.append(nota)

soma_notas = 0

for n in notas:
    soma_notas = soma_notas + n

media = soma_notas / 4

print("\n---resultado final---")
print("notas digitadas:", notas)
print(f"media do aluno: {media:.1f}")

if media >= 7:
    print("aprovado")
else:
    print("reprovado")