import sqlite3

conn = sqlite3.connect('jewelry_workshop.db')
cursor = conn.cursor()

# Создание таблицы, если не существует
cursor.execute('''
CREATE TABLE IF NOT EXISTS izdelie (
    id INTEGER PRIMARY KEY,
    fio_klienta TEXT NOT NULL,
    fio_mastera TEXT NOT NULL,
    vid_izdeliya TEXT NOT NULL,
    material TEXT NOT NULL,
    stoimost_rabot REAL NOT NULL
)
''')
conn.commit()

# Данные для вставки — 10 записей
info = [
    (1, "Иванов Иван Иванович", "Петров Петр Петрович", "Кольцо", "Золото", 15000),
    (2, "Сидорова Мария Алексеевна", "Кузнецов Алексей Сергеевич", "Серьги", "Серебро", 8000),
    (3, "Кузнецова Ольга Викторовна", "Иванов Иван Иванович", "Подвеска", "Платина", 12000),
    (4, "Петров Алексей Николаевич", "Смирнова Наталья Владимировна", "Браслет", "Золото", 20000),
    (5, "Смирнова Наталья Владимировна", "Петров Петр Петрович", "Кольцо", "Платина", 18000),
    (6, "Васильев Дмитрий Сергеевич", "Кузнецов Алексей Сергеевич", "Часы", "Титан", 25000),
    (7, "Морозова Елена Ивановна", "Иванов Иван Иванович", "Серьги", "Золото", 9000),
    (8, "Новиков Сергей Павлович", "Смирнова Наталья Владимировна", "Подвеска", "Серебро", 7000),
    (9, "Федорова Анна Михайловна", "Петров Петр Петрович", "Кольцо", "Платина", 22000),
    (10, "Лебедев Николай Викторович", "Кузнецов Алексей Сергеевич", "Браслет", "Титан", 16000)
]

# Вставляем данные
cursor.executemany(
    "INSERT OR IGNORE INTO izdelie (id, fio_klienta, fio_mastera, vid_izdeliya, material, stoimost_rabot) VALUES (?, ?, ?, ?, ?, ?)",
    info
)
conn.commit()
print("Вывод всех записей:")
cursor.execute("SELECT * FROM izdelie")
for row in cursor.fetchall():
    print(row)

print("\nВывод записей, где стоимость работ больше 30000:")
cursor.execute("SELECT * FROM izdelie WHERE stoimost_rabot > 30000")
for row in cursor.fetchall():
    print(row)

print("\nВывод fio_klienta, fio_mastera, vid_izdeliya:")
cursor.execute("SELECT fio_klienta, fio_mastera, vid_izdeliya FROM izdelie")
for row in cursor.fetchall():
    print(row)

print("\nУдаление записи по id 1")
record_id = 1
cursor.execute("DELETE FROM izdelie WHERE id = ?", (record_id,))
conn.commit()

print("Удаление записи где stoimost_rabot < 14000")
min_stoimost = 14000
cursor.execute("DELETE FROM izdelie WHERE stoimost_rabot < ?", (min_stoimost,))
conn.commit()

print("Удаление записи где fio_klienta = 'Васильев Дмитрий Сергеевич'")
fio_klienta = "Васильев Дмитрий Сергеевич"
cursor.execute("DELETE FROM izdelie WHERE fio_klienta = ?", (fio_klienta,))
conn.commit()

print("\nИзменение записи с id 10 (обновление fio_klienta):")
new = "qwert"
record_id = 10
cursor.execute(
    "UPDATE izdelie SET fio_klienta = ? WHERE id = ?",
    (new, record_id)
)
conn.commit()

print("Изменение записи с id 10 (обновление fio_klienta, fio_mastera, material):")
new_master = "Иван"
new_material = "Золото"
cursor.execute(
    "UPDATE izdelie SET fio_klienta = ?, fio_mastera = ?, material = ? WHERE id = ?",
    (new, new_master, new_material, record_id)
)
conn.commit()

print("Изменение стоимости работ для изделий вида 'Кольцо' на 2000:")
cursor.execute(
    "UPDATE izdelie SET stoimost_rabot = ? WHERE vid_izdeliya = ?",
    (2000, "Кольцо")
)
conn.commit()

# Итоговый вывод таблицы после всех операций
print("\nИтоговая таблица после всех операций:")
cursor.execute("SELECT * FROM izdelie")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
conn.close()
