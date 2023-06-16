import sqlite3

# Tworzenie połączenia z bazą danych SQLite
conn = sqlite3.connect("database.db")
c = conn.cursor()

# Tworzenie tabeli tabela1
c.execute('''CREATE TABLE IF NOT EXISTS tabela1
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             nazwa TEXT,
             data TEXT)''')

# Tworzenie tabeli tabela2
c.execute('''CREATE TABLE IF NOT EXISTS tabela2
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             nazwa TEXT,
             ilosc INTEGER)''')

# Tworzenie tabeli tabela3
c.execute('''CREATE TABLE IF NOT EXISTS tabela3
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             nazwa TEXT,
             cena REAL)''')

# Tworzenie tabeli tabela4
c.execute('''CREATE TABLE IF NOT EXISTS tabela4
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             nazwa TEXT,
             opis TEXT)''')

# Dodawanie danych do tabeli tabela1
c.execute("INSERT INTO tabela1 (nazwa, data) VALUES ('Rekord1', '2023-04-01')")
c.execute("INSERT INTO tabela1 (nazwa, data) VALUES ('Rekord2', '2023-04-02')")

# Dodawanie danych do tabeli tabela2
c.execute("INSERT INTO tabela2 (nazwa, ilosc) VALUES ('Produkt1', 10)")
c.execute("INSERT INTO tabela2 (nazwa, ilosc) VALUES ('Produkt2', 5)")

# Dodawanie danych do tabeli tabela3
c.execute("INSERT INTO tabela3 (nazwa, cena) VALUES ('Produkt1', 10.99)")
c.execute("INSERT INTO tabela3 (nazwa, cena) VALUES ('Produkt2', 19.99)")

# Dodawanie danych do tabeli tabela4
c.execute("INSERT INTO tabela4 (nazwa, opis) VALUES ('Rekord1', 'Opis rekordu 1')")
c.execute("INSERT INTO tabela4 (nazwa, opis) VALUES ('Rekord2', 'Opis rekordu 2')")

# Zatwierdzanie zmian w bazie danych
conn.commit()

# Zamykanie połączenia z bazą danych
conn.close()
