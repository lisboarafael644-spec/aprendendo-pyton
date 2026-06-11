notas = [
    [7.0, 8.5, 6.0, 7.5],
    [9.0, 9.5, 10.0, 8.5],
    [5.0, 6.0, 5.5, 4.0]
]

medias = []

for aluno in notas:
    media = sum(aluno) / len(aluno)
    medias.append(media)

for i in range(len(medias)):
    print(f"Média do aluno {i + 1}: {medias[i]:.2f}")

