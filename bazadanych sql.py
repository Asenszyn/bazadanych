import sqlite3

# Utworzenie połączenia z bazą danych
conn = sqlite3.connect('baza_danych.db')
c = conn.cursor()

# Utworzenie tabel
c.execute('''CREATE TABLE IF NOT EXISTS tabela1
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             kolumna1 TEXT,
             kolumna2 TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS tabela2
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             kolumna1 TEXT,
             kolumna2 TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS tabela3
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             kolumna1 TEXT,
             kolumna2 TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS tabela4
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             kolumna1 TEXT,
             kolumna2 TEXT)''')

# Wypełnienie tabel danymi
c.execute("INSERT INTO tabela1 (kolumna1, kolumna2) VALUES ('Akcesorium 1', 'Kategoria A')")
c.execute("INSERT INTO tabela1 (kolumna1, kolumna2) VALUES ('Akcesorium 2', 'Kategoria B')")
c.execute("INSERT INTO tabela1 (kolumna1, kolumna2) VALUES ('Akcesorium 3', 'Kategoria A')")
c.execute("INSERT INTO tabela1 (kolumna1, kolumna2) VALUES ('Akcesorium 4', 'Kategoria C')")

c.execute("INSERT INTO tabela2 (kolumna1, kolumna2) VALUES ('Akcesorium 5', 'Kategoria B')")
c.execute("INSERT INTO tabela2 (kolumna1, kolumna2) VALUES ('Akcesorium 6', 'Kategoria A')")
c.execute("INSERT INTO tabela2 (kolumna1, kolumna2) VALUES ('Akcesorium 7', 'Kategoria C')")
c.execute("INSERT INTO tabela2 (kolumna1, kolumna2) VALUES ('Akcesorium 8', 'Kategoria B')")

c.execute("INSERT INTO tabela3 (kolumna1, kolumna2) VALUES ('Akcesorium 9', 'Kategoria C')")
c.execute("INSERT INTO tabela3 (kolumna1, kolumna2) VALUES ('Akcesorium 10', 'Kategoria B')")
c.execute("INSERT INTO tabela3 (kolumna1, kolumna2) VALUES ('Akcesorium 11', 'Kategoria A')")
c.execute("INSERT INTO tabela3 (kolumna1, kolumna2) VALUES ('Akcesorium 12', 'Kategoria C')")

c.execute("INSERT INTO tabela4 (kolumna1, kolumna2) VALUES ('Akcesorium 13', 'Kategoria A')")
c.execute("INSERT INTO tabela4 (kolumna1, kolumna2) VALUES ('Akcesorium 14', 'Kategoria C')")
c.execute("INSERT INTO tabela4 (kolumna1, kolumna2) VALUES ('Akcesorium 15', 'Kategoria B')")
c.execute("INSERT INTO tabela4 (kolumna1, kolumna2) VALUES ('Akcesorium 16', 'Kategoria A')")

# Zatwierdzenie zmian i zamknięcie połączenia
conn.commit()
conn.close()