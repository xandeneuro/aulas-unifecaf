from escola import *

turma = [
    {"nome": "Joao", "idade": 20, "nota1": 5.5, "nota2": 6.5},
    {"nome": "Maria", "idade": 22, "nota1": 9.0, "nota2": 6.0},
    {"nome": "Pedro", "idade": 19, "nota1": 7.0, "nota2":8.0}
]

print(turma[0]["nome"])  # Acessando o primeiro aluno

novo_aluno = {"nome": "Ana", "idade": 21, "nota1": 9.5, "nota2": 7.5}
turma.append(novo_aluno)    # Adiciona um novo aluno à lista

for aluno in turma:
    media = calcular_media(aluno['nota1'], aluno['nota2'])
    situacao = verificar_aprovacao(media)
    print(f"Nome: {aluno['nome']}, Idade: {aluno['idade']},  Média: {media}, Situação: {situacao}")

medias = [calcular_media(aluno['nota1'], aluno['nota2']) for aluno in turma]
media_turma = calcularMediaTurma(medias)
print(f"Média da turma: {media_turma}")