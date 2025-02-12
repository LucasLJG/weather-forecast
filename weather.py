import requests
from config import API_KEY, BASE_URL

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metrics", # Temperatura em Celsius
        "lang": "pt-br" # Descrições em pt-br
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status() # Lança erros para respostas não 200.

        data = response.json() 

        """
        Exemplo de formatação dos dados recebidos pela API no formato JSON e convertidos para um objeto Python do tipo dicionário.
        data = {
            "name": "São Paulo",
            "main": {"temp": 25, "humidity": 70},
            "weather": [{"description": "céu limpo"}]
        }
        """

        # Validação básica de dados
        if not all(key in data for key in ("main","weather")):
            raise ValueError("Resposta da API inválida.")
        
        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"].capitalize(),
            "humidity": data["main"]["humidity"]
        }
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
        return None
