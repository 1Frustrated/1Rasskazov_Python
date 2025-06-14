# Вариант 26
# Приложение ЮВЕЛИРНАЯ МАСТЕРСКАЯ для некоторой организации. БД
# должна содержать таблицу Изделие со следующей структурой записи: ФИО клиента,
# ФИО мастера, вид изделия, материал, стоимость работ.
import sqlite3

conn = sqlite3.connect('jewelry.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Izdelie (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fio_klienta TEXT NOT NULL,
    fio_mastera TEXT NOT NULL,
    vid_izdeliya TEXT NOT NULL,
    material TEXT NOT NULL,
    stoimost_rabot REAL NOT NULL
)
''')
conn.commit()

ww = ('Fio', 'master', 'kart', 'derevo', 12.0) #ВВОДИТЬ ТУТ

cursor.execute('''
INSERT INTO Izdelie (fio_klienta, fio_mastera, vid_izdeliya, material, stoimost_rabot)
VALUES (?, ?, ?, ?, ?)
''', ww)

conn.commit()

cursor.execute('SELECT * FROM Izdelie')
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
