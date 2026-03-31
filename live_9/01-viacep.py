import requests

def consultar_cep(cep):
    end_point = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(end_point)
    if response.status_code == 200:
        if 'erro' in response.json():
            return None
        return response.json()
    else:
        return None

cep = input('Digite o CEP: ')
info = consultar_cep(cep)

if info:
    print(f"CEP: {info['cep']}")
    print(f"Logradouro: {info['logradouro']}")
    print(f"Bairro: {info['bairro']}")
    print(f"Cidade: {info['localidade']}")
    print(f"Estado: {info['uf']}")
else:
    print('CEP não encontrado.')