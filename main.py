import argparse
from weather import get_weather
from database import init_db, add_search, get_history, clear_history

def main():
    init_db() # Garante que o banco de dados existe.

    parser = argparse.ArgumentParser(description="Consulta a previsão do tempo")
    parser.add_argument("city", nargs="?", help="Nome da cidade para consulta")
    parser.add_argument("--history", action="store_true", help="Exibe o histórico de buscas")
    parser.add_argument("--clear", action="store_true", help="Limpa o histórico de buscas")

    args = parser.parse_args()

    if args.history:
        print("\n Histórico de buscas (últimas 5):")
        history = get_history()
        if not history:
            print("Nenhuma busca registrada.")
        else:
            for city, temp, desc, time in history:
                print(f"[{time}] {city}: {temp}°C, {desc}")
        return
    
    if args.clear:
        confirm = input("Tem certeza que seja limpar todo o histórico? (S/N)").strip().lower()
        if confirm == "s":
            clear_history()
            print("Histórico limpo com sucesso.")
        else:
            print("Operação cancelada.")
        return
    
    if not args.city:
        parser.print_help()
        return
    
    weather_data = get_weather(args.city)
    if weather_data:
        print(f"\nPrevisão para {weather_data['city']}:")
        print(f"Temperatura: {weather_data['temperature']}°C")
        print(f"Descrição: {weather_data['description']}")
        print(f"Umidade: {weather_data['humidity']}%")

        add_search(args.city, weather_data['temperature'], weather_data['description'])

if __name__ == "__main__":
    main()