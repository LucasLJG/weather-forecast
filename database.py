import sqlite3
from contextlib import closing

# Criação da tabela do histórico
def init_db():
    with closing(sqlite3.connect("weather_history.db")) as conn:
        with conn as db:
            db.execute('''
                       CREATE TABLE IF NOT EXISTS searches (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       city TEXT NOT NULL,
                       temperature REAL,
                       description TEXT,
                       search_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                       )
                       '''
            )

# Inserção de uma busca no histórico
def add_search(city, temperature, description):
    with closing(sqlite3.connect("weather_history.db")) as conn:
        with conn as db:
            db.execute(
                       "INSERT INTO searches (city, temperature, description) VALUES (?,?,?)",
                       (city, temperature, description)
            )

# Recuperação do histórico
def get_history(limit=5):
    with closing(sqlite3.connect("weather_history.db")) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT city, temperature, description, search_time FROM searches ORDER BY search_time DESC LIMIT ?", (limit,))
        return cursor.fetchall()
    
# Limpeza do histórico
def clear_history():
    with closing(sqlite3.connect("weather_history.db")) as conn:
        with conn as db:
            db.execute("DELETE FROM searches")
            db.execute("VACUUM") # Compacta o banco de dados após deletar
    

            


