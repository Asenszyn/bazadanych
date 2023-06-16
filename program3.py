import tkinter as tk
import sqlite3
import csv

# Tworzenie połączenia z bazą danych SQLite
conn = sqlite3.connect("database.db")
c = conn.cursor()

# Tworzenie tabeli
c.execute('''CREATE TABLE IF NOT EXISTS tabela1
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             nazwa TEXT,
             data TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS tabela2
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             nazwa TEXT,
             ilosc INTEGER)''')

c.execute('''CREATE TABLE IF NOT EXISTS tabela3
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             nazwa TEXT,
             cena REAL)''')

c.execute('''CREATE TABLE IF NOT EXISTS tabela4
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             nazwa TEXT,
             opis TEXT)''')

# Dodawanie danych do tabeli
c.execute("INSERT INTO tabela1 (nazwa, data) VALUES ('Rekord1', '2023-04-01')")
c.execute("INSERT INTO tabela1 (nazwa, data) VALUES ('Rekord2', '2023-04-02')")
c.execute("INSERT INTO tabela2 (nazwa, ilosc) VALUES ('Produkt1', 10)")
c.execute("INSERT INTO tabela2 (nazwa, ilosc) VALUES ('Produkt2', 5)")
c.execute("INSERT INTO tabela3 (nazwa, cena) VALUES ('Produkt1', 10.99)")
c.execute("INSERT INTO tabela3 (nazwa, cena) VALUES ('Produkt2', 19.99)")
c.execute("INSERT INTO tabela4 (nazwa, opis) VALUES ('Rekord1', 'Opis rekordu 1')")
c.execute("INSERT INTO tabela4 (nazwa, opis) VALUES ('Rekord2', 'Opis rekordu 2')")

# Zatwierdzanie zmian w bazie danych
conn.commit()

# GUI aplikacji
def dodaj_rekord():
    nazwa = entry_nazwa.get()
    data = entry_data.get()
    c.execute("INSERT INTO tabela1 (nazwa, data) VALUES (?, ?)", (nazwa, data))
    conn.commit()
    entry_nazwa.delete(0, tk.END)
    entry_data.delete(0, tk.END)

def usun_rekord():
    id = entry_id.get()
    c.execute("DELETE FROM tabela1 WHERE id=?", (id,))
    conn.commit()
    entry_id.delete(0, tk.END)

def edytuj_rekord():
    id = entry_id.get()
    nazwa = entry_nazwa.get()
    data = entry_data.get()
    c.execute("UPDATE tabela1 SET nazwa=?, data=? WHERE id=?", (nazwa, data, id))
    conn.commit()
    entry_id.delete(0, tk.END)
    entry_nazwa.delete(0, tk.END)
    entry_data.delete(0, tk.END)

def wyswietl_rekordy():
    c.execute("SELECT * FROM tabela1")
    rows = c.fetchall()
    for row in rows:
        print(row)

def wyszukaj_rekordy():
    nazwa = entry_nazwa.get()
    c.execute("SELECT * FROM tabela1 WHERE nazwa=?", (nazwa,))
    rows = c.fetchall()
    for row in rows:
        print(row)

def sortuj_rekordy():
    c.execute("SELECT * FROM tabela1 ORDER BY nazwa")
    rows = c.fetchall()
    for row in rows:
        print(row)

def filtruj_rekordy():
    data = entry_data.get()
    c.execute("SELECT * FROM tabela1 WHERE data=?", (data,))
    rows = c.fetchall()
    for row in rows:
        print(row)

def eksportuj_do_csv():
    c.execute("SELECT * FROM tabela1")
    rows = c.fetchall()
    with open("export.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["ID", "Nazwa", "Data"])
        writer.writerows(rows)

def importuj_z_csv():
    with open("import.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Pomijanie nagłówka
        for row in reader:
            nazwa = row[0]
            data = row[1]
            c.execute("INSERT INTO tabela1 (nazwa, data) VALUES (?, ?)", (nazwa, data))
    conn.commit()

# Tworzenie GUI
root = tk.Tk()
root.title("Aplikacja bazodanowa")

label_nazwa = tk.Label(root, text="Nazwa:")
label_nazwa.pack()
entry_nazwa = tk.Entry(root)
entry_nazwa.pack()

label_data = tk.Label(root, text="Data:")
label_data.pack()
entry_data = tk.Entry(root)
entry_data.pack()

button_dodaj = tk.Button(root, text="Dodaj rekord", command=dodaj_rekord)
button_dodaj.pack()

label_id = tk.Label(root, text="ID:")
label_id.pack()
entry_id = tk.Entry(root)
entry_id.pack()

button_usun = tk.Button(root, text="Usuń rekord", command=usun_rekord)
button_usun.pack()

button_edytuj = tk.Button(root, text="Edytuj rekord", command=edytuj_rekord)
button_edytuj.pack()

button_wyswietl = tk.Button(root, text="Wyświetl rekordy", command=wyswietl_rekordy)
button_wyswietl.pack()

button_wyszukaj = tk.Button(root, text="Wyszukaj rekordy", command=wyszukaj_rekordy)
button_wyszukaj.pack()

button_sortuj = tk.Button(root, text="Sortuj rekordy", command=sortuj_rekordy)
button_sortuj.pack()

button_filtruj = tk.Button(root, text="Filtruj rekordy", command=filtruj_rekordy)
button_filtruj.pack()

button_eksportuj = tk.Button(root, text="Eksportuj do CSV", command=eksportuj_do_csv)
button_eksportuj.pack()

button_importuj = tk.Button(root, text="Importuj z CSV", command=importuj_z_csv)
button_importuj.pack()

root.mainloop()

# Zamykanie połączenia z bazą danych
conn.close()
