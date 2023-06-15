import sqlite3
from tkinter import *
import csv

# Funkcja dodająca nowy rekord do bazy danych
def dodaj_rekord():
    conn = sqlite3.connect('baza_danych.db')
    c = conn.cursor()
    c.execute("INSERT INTO tabela1 (kolumna1, kolumna2) VALUES (?, ?)", (pole1.get(), pole2.get()))
    conn.commit()
    conn.close()

# Funkcja usuwająca rekord z bazy danych
def usun_rekord():
    conn = sqlite3.connect('baza_danych.db')
    c = conn.cursor()
    c.execute("DELETE FROM tabela1 WHERE id=?", (pole_id.get(),))
    conn.commit()
    conn.close()

# Funkcja edytująca rekord w bazie danych
def edytuj_rekord():
    conn = sqlite3.connect('baza_danych.db')
    c = conn.cursor()
    c.execute("UPDATE tabela1 SET kolumna1=?, kolumna2=? WHERE id=?", (pole1.get(), pole2.get(), pole_id.get()))
    conn.commit()
    conn.close()

# Funkcja wyświetlająca rekordy z bazy danych
def wyswietl_rekordy():
    conn = sqlite3.connect('baza_danych.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tabela1")
    rekordy = c.fetchall()
    for rekord in rekordy:
        print(rekord)
    conn.close()

# Funkcja wyszukująca rekordy w bazie danych
def wyszukaj_rekordy():
    conn = sqlite3.connect('baza_danych.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tabela1 WHERE kolumna1=?", (pole1.get(),))
    rekordy = c.fetchall()
    for rekord in rekordy:
        print(rekord)
    conn.close()

# Funkcja sortująca rekordy w bazie danych
def sortuj_rekordy():
    conn = sqlite3.connect('baza_danych.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tabela1 ORDER BY kolumna1")
    rekordy = c.fetchall()
    for rekord in rekordy:
        print(rekord)
    conn.close()

# Funkcja filtrowania rekordów w bazie danych
def filtrowanie_rekordy():
    conn = sqlite3.connect('baza_danych.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tabela1 WHERE kolumna1 LIKE ?", (f"%{pole1.get()}%",))
    rekordy = c.fetchall()
    for rekord in rekordy:
        print(rekord)
    conn.close()

# Funkcja eksportująca rekordy z bazy danych do pliku CSV
def eksportuj_do_csv():
    conn = sqlite3.connect('baza_danych.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tabela1")
    rekordy = c.fetchall()
    with open('eksport.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['kolumna1', 'kolumna2'])
        writer.writerows(rekordy)
    conn.close()

# Funkcja importująca rekordy z pliku CSV do bazy danych
def importuj_z_csv():
    conn = sqlite3.connect('baza_danych.db')
    c = conn.cursor()
    with open('import.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            c.execute("INSERT INTO tabela1 (kolumna1, kolumna2) VALUES (?, ?)", (row[0], row[1]))
    conn.commit()
    conn.close()


# Tworzenie interfejsu użytkownika przy użyciu biblioteki Tkinter
root = Tk()

pole1 = Entry(root)
pole1.pack()

pole2 = Entry(root)
pole2.pack()

pole_id = Entry(root)
pole_id.pack()

przycisk_dodaj = Button(root, text="Dodaj rekord", command=dodaj_rekord)
przycisk_dodaj.pack()

przycisk_usun = Button(root, text="Usuń rekord", command=usun_rekord)
przycisk_usun.pack()

przycisk_edytuj = Button(root, text="Edytuj rekord", command=edytuj_rekord)
przycisk_edytuj.pack()

przycisk_wyswietl = Button(root, text="Wyświetl rekordy", command=wyswietl_rekordy)
przycisk_wyswietl.pack()

przycisk_wyszukaj = Button(root, text="Wyszukaj rekordy", command=wyszukaj_rekordy)
przycisk_wyszukaj.pack()

przycisk_sortuj = Button(root, text="Sortuj rekordy", command=sortuj_rekordy)
przycisk_sortuj.pack()

przycisk_filtruj = Button(root, text="Filtruj rekordy", command=filtrowanie_rekordy)
przycisk_filtruj.pack()

przycisk_eksportuj = Button(root, text="Eksportuj do CSV", command=eksportuj_do_csv)
przycisk_eksportuj.pack()

przycisk_importuj = Button(root, text="Importuj z CSV", command=importuj_z_csv)
przycisk_importuj.pack()

root.mainloop()

# Funkcja tworząca tabele w bazie danych
def utworz_tabele():
    conn = sqlite3.connect('baza_danych.db')
    c = conn.cursor()

    # Tabela 1
    c.execute('''CREATE TABLE IF NOT EXISTS tabela1
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 kolumna1 TEXT,
                 kolumna2 TEXT)''')

    # Tabela 2
    c.execute('''CREATE TABLE IF NOT EXISTS tabela2
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 kolumna1 TEXT,
                 kolumna2 TEXT)''')

    # Tabela 3
    c.execute('''CREATE TABLE IF NOT EXISTS tabela3
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 kolumna1 TEXT,
                 kolumna2 TEXT)''')

    # Tabela 4
    c.execute('''CREATE TABLE IF NOT EXISTS tabela4
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 kolumna1 TEXT,
                 kolumna2 TEXT)''')

    conn.commit()
    conn.close()

# Funkcja wypełniająca tabele danymi
def wypelnij_tabele():
    conn = sqlite3.connect('baza_danych.db')
    c = conn.cursor()

    # Tabela 1
    c.execute("INSERT INTO tabela1 (kolumna1, kolumna2) VALUES ('Akcesorium 1', 'Kategoria A')")
    c.execute("INSERT INTO tabela1 (kolumna1, kolumna2) VALUES ('Akcesorium 2', 'Kategoria B')")
    c.execute("INSERT INTO tabela1 (kolumna1, kolumna2) VALUES ('Akcesorium 3', 'Kategoria A')")
    c.execute("INSERT INTO tabela1 (kolumna1, kolumna2) VALUES ('Akcesorium 4', 'Kategoria C')")

    # Tabela 2
    c.execute("INSERT INTO tabela2 (kolumna1, kolumna2) VALUES ('Akcesorium 5', 'Kategoria B')")
    c.execute("INSERT INTO tabela2 (kolumna1, kolumna2) VALUES ('Akcesorium 6', 'Kategoria A')")
    c.execute("INSERT INTO tabela2 (kolumna1, kolumna2) VALUES ('Akcesorium 7', 'Kategoria C')")
    c.execute("INSERT INTO tabela2 (kolumna1, kolumna2) VALUES ('Akcesorium 8', 'Kategoria B')")

    # Tabela 3
    c.execute("INSERT INTO tabela3 (kolumna1, kolumna2) VALUES ('Akcesorium 9', 'Kategoria C')")
    c.execute("INSERT INTO tabela3 (kolumna1, kolumna2) VALUES ('Akcesorium 10', 'Kategoria B')")
    c.execute("INSERT INTO tabela3 (kolumna1, kolumna2) VALUES ('Akcesorium 11', 'Kategoria A')")
    c.execute("INSERT INTO tabela3 (kolumna1, kolumna2) VALUES ('Akcesorium 12', 'Kategoria C')")

    # T# Tabela 4
    c.execute("INSERT INTO tabela4 (kolumna1, kolumna2) VALUES ('Akcesorium 13', 'Kategoria A')")
    c.execute("INSERT INTO tabela4 (kolumna1, kolumna2) VALUES ('Akcesorium 14', 'Kategoria C')")
    c.execute("INSERT INTO tabela4 (kolumna1, kolumna2) VALUES ('Akcesorium 15', 'Kategoria B')")
    c.execute("INSERT INTO tabela4 (kolumna1, kolumna2) VALUES ('Akcesorium 16', 'Kategoria A')")

    conn.commit()
    conn.close()

# Funkcja sortująca rekordy w bazie danych według kategorii dla każdej tabeli
def sortuj_rekordy_kategoria():
    conn = sqlite3.connect('baza_danych.db')
    c = conn.cursor()

    # Tabela 1
    c.execute("SELECT * FROM tabela1 ORDER BY kolumna2")
    rekordy_tabela1 = c.fetchall()
    print("Tabela 1 - Posortowana według kategorii:")
    for rekord in rekordy_tabela1:
        print(rekord)

    # Tabela 2
    c.execute("SELECT * FROM tabela2 ORDER BY kolumna2")
    rekordy_tabela2 = c.fetchall()
    print("Tabela 2 - Posortowana według kategorii:")
    for rekord in rekordy_tabela2:
        print(rekord)

    # Tabela 3
    c.execute("SELECT * FROM tabela3 ORDER BY kolumna2")
    rekordy_tabela3 = c.fetchall()
    print("Tabela 3 - Posortowana według kategorii:")
    for rekord in rekordy_tabela3:
        print(rekord)

    # Tabela 4
    c.execute("SELECT * FROM tabela4 ORDER BY kolumna2")
    rekordy_tabela4 = c.fetchall()
    print("Tabela 4 - Posortowana według kategorii:")
    for rekord in rekordy_tabela4:
        print(rekord)

    conn.close()

# Tworzenie interfejsu użytkownika przy użyciu biblioteki Tkinter
root = Tk()

utworz_tabele()
wypelnij_tabele()

przycisk_sortuj_kategorie = Button(root, text="Sortuj rekordy według kategorii", command=sortuj_rekordy_kategoria)
przycisk_sortuj_kategorie.pack()

root.mainloop()
