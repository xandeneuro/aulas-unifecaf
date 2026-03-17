turma = [
    {"nome": "Joao", "idade": 20, "nota": 8.5},
    {"nome": "Maria", "idade": 22, "nota": 9.0},
    {"nome": "Pedro", "idade": 19, "nota": 7.0}
]

print(turma[0]["nome"])  # Acessando o primeiro aluno

novo_aluno = {"nome": "Ana", "idade": 21, "nota": 9.5}
turma.append(novo_aluno)    # Adiciona um novo aluno à lista

for aluno in turma:
    print(f"Nome: {aluno['nome']}, Idade: {aluno['idade']}, Nota: {aluno['nota']}")