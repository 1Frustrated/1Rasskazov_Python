# Вариант 26
# Приложение ЮВЕЛИРНАЯ МАСТЕРСКАЯ для некоторой организации. БД
# должна содержать таблицу Изделие со следующей структурой записи: ФИО клиента,
# ФИО мастера, вид изделия, материал, стоимость работ
import sqlite3

conn = sqlite3.connect('jewelry_workshop.db')
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


def add_izdelie(fio_klienta, fio_mastera, vid_izdeliya, material, stoimost_rabot):
    cursor.execute('''
    INSERT INTO Izdelie (fio_klienta, fio_mastera, vid_izdeliya, material, stoimost_rabot)
    VALUES (?, ?, ?, ?, ?)
    ''', (fio_klienta, fio_mastera, vid_izdeliya, material, stoimost_rabot))
    conn.commit()
    print("Запись добавлена успешно!")


def list_izdelia():
    cursor.execute('SELECT * FROM Izdelie')
    rows = cursor.fetchall()
    for row in rows:
        print(f"ID: {row[0]}, Клиент: {row[1]}, Мастер: {row[2]}, Изделие: {row[3]}, Материал: {row[4]}, Стоимость: {row[5]}")


def main():
    while True:
        print("\nЮВЕЛИРНАЯ МАСТЕРСКАЯ")
        print("1. Добавить изделие")
        print("2. Показать все изделия")
        print("3. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            fio_klienta = input("ФИО клиента: ")
            fio_mastera = input("ФИО мастера: ")
            vid_izdeliya = input("Вид изделия: ")
            material = input("Материал: ")
            stoimost_rabot = float(input("Стоимость работ: "))
            add_izdelie(fio_klienta, fio_mastera, vid_izdeliya, material, stoimost_rabot)
        elif choice == '2':
            list_izdelia()
        elif choice == '3':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор, попробуйте снова.")


main()

conn.close()

