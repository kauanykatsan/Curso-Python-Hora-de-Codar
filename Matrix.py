# Matriz de notas
notas = [
    [8.0, 7.5],
    [9.0, 8.5],
    [6.5, 7.0]
]

for i in range(len(notas)):
    media = (notas[i][0] + notas[i][1]) / 2
    print(f"Aluno {i+1} - Média: {media:.1f}")

    