import requests

nome_filme = input('Digite o nome do filme: ')

def buscar_filme(nome):
    end_point = f'http://www.omdbapi.com/?t={nome}&apikey=b49580ba'
    response = requests.get(end_point)
    if response.status_code == 200:
        data = response.json()
        if data['Response'] == 'True':
            return data
    return None 

info = buscar_filme(nome_filme)

if info:
    print(f"Título: {info['Title']}")
    print(f"Ano: {info['Year']}")
    print(f"Gênero: {info['Genre']}")
    print(f"Diretor: {info['Director']}")
    print(f"Atores: {info['Actors']}")
    print(f"Sinopse: {info['Plot']}")
else:    print('Filme não encontrado.')
