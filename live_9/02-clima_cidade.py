import requests

def consulta_clima(cidade):
    end_point = f'http://geocoding-api.open-meteo.com/v1/search?name={cidade}'
    response = requests.get(end_point)
    if response.status_code == 200:
        data = response.json()
        if 'results' in data and len(data['results']) > 0:
            latitude = data['results'][0]['latitude']
            longitude = data['results'][0]['longitude']
            clima_end_point = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true'
            clima_response = requests.get(clima_end_point)
            if clima_response.status_code == 200:
                return clima_response.json()
    return None

cidade = input('Digite o nome da cidade: ')

info = consulta_clima(cidade)

if info and 'current_weather' in info:
    clima = info['current_weather']
    print(f"Temperatura: {clima['temperature']}°C")
    print(f"Vento: {clima['windspeed']} km/h")
    print(f"Direção do vento: {clima['winddirection']}°")
else:    print('Cidade não encontrada ou erro ao consultar o clima.')