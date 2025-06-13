import sqlite3

conn = sqlite3.connect('memory')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE Izdelie (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fio_klienta TEXT NOT NULL,
    fio_mastra TEXT NOT NULL,
    vid_izdeliya TEXT NOT NULL,
    material TEXT NOT NULL,
    stoimost_rabot REAL NOT NULL
)
''')
