turma = [
    {"nome": "Joao", "idade": 20, "nota": 8.5},
    {"nome": "Maria", "idade": 22, "nota": 9.0},
    {"nome": "Pedro", "idade": 19, "nota": 7.0}
]

def mensagem(nome):
    print(f"Bem-vindo à turma, {nome}!")
    
for aluno in turma:
    mensagem(aluno["nome"])  # Chama a função para exibir a mensagem