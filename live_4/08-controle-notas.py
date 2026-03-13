notas = [8.5, 7.0, 9.5, 6.0, 8.0]

for i, nota in enumerate(notas): # enumera as notas:
    if nota >= 9:
        print(f'Aluno {i + 1} - Nota: {nota} - Excelente')
    elif nota >= 7:
        print(f'Aluno {i + 1} - Nota: {nota} - Bom')
    elif nota >= 5:
        print(f'Aluno {i + 1} - Nota: {nota} - Regular')
    else:
        print(f'Aluno {i + 1} - Nota: {nota} - Insuficiente')