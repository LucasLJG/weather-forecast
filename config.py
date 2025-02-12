import os
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"