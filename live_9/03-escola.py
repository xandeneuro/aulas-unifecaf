import requests

def listar_alunos():
    end_point = 'https://lion-school-phbo.onrender.com/alunos'
    response = requests.get(end_point)
    if response.status_code == 200:
        return response.json()
    else:
        return None
    
def listar_cursos():
    end_point = 'https://lion-school-phbo.onrender.com/cursos'
    response = requests.get(end_point)
    if response.status_code == 200:
        return response.json()
    else:
        return None     
    
alunos = listar_alunos()

if alunos:
    for aluno in alunos:
        print(f"ID: {aluno['id']}")
        print(f"Nome: {aluno['nome']}")
        print(f"Idade: {aluno['foto']}")
        print(f"Curso: {aluno['curso_id']}")
        print('---')    
else:    print('Erro ao listar alunos.')

cursos = listar_cursos()

if cursos:
    for curso in cursos:
        print(f"ID: {curso['id']}")
        print(f"Nome: {curso['nome']}")
        print('---')    
else:    print('Erro ao listar cursos.')
