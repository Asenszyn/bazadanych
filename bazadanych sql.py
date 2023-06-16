import sqlite3

# Utworzenie połączenia z bazą danych
conn = sqlite3.connect('baza_danych.db')
c = conn.cursor()

# Utworzenie tabel
c.execute('''CREATE TABLE IF NOT EXISTS tabela1
             (id INTEGER PRIMARY KEY,
             nazwa TEXT,
             cena REAL)''')

c.execute('''CREATE TABLE IF NOT EXISTS tabela2
             (id INTEGER PRIMARY KEY,
             marka TEXT,
             ilosc INTEGER)''')

c.execute('''CREATE TABLE IF NOT EXISTS tabela3
             (id INTEGER PRIMARY KEY,
             kategoria TEXT,
             opis TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS tabela4
             (id INTEGER PRIMARY KEY,
             producent TEXT,
             rok INTEGER)''')

# Wypełnienie tabel danymi
c.execute("INSERT INTO tabela1 (id, nazwa, cena) VALUES (1, 'Produkt 1', 10.99)")
c.execute("INSERT INTO tabela1 (id, nazwa, cena) VALUES (2, 'Produkt 2', 15.99)")
c.execute("INSERT INTO tabela1 (id, nazwa, cena) VALUES (3, 'Produkt 3', 20.50)")

c.execute("INSERT INTO tabela2 (id, marka, ilosc) VALUES (1, 'Marka A', 50)")
c.execute("INSERT INTO tabela2 (id, marka, ilosc) VALUES (2, 'Marka B', 100)")
c.execute("INSERT INTO tabela2 (id, marka, ilosc) VALUES (3, 'Marka C', 75)")

c.execute("INSERT INTO tabela3 (id, kategoria, opis) VALUES (1, 'Kategoria A', 'Opis kategorii A')")
c.execute("INSERT INTO tabela3 (id, kategoria, opis) VALUES (2, 'Kategoria B', 'Opis kategorii B')")
c.execute("INSERT INTO tabela3 (id, kategoria, opis) VALUES (3, 'Kategoria C', 'Opis kategorii C')")

c.execute("INSERT INTO tabela4 (id, producent, rok) VALUES (1, 'Producent X', 2019)")
c.execute("INSERT INTO tabela4 (id, producent, rok) VALUES (2, 'Producent Y', 2020)")
c.execute("INSERT INTO tabela4 (id, producent, rok) VALUES (3, 'Producent Z', 2021)")

# Zatwierdzenie zmian i zamknięcie połączenia
conn.commit()
conn.close()
