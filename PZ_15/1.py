import sqlite3
conn = sqlite3.connect('qwe.db')
cur = conn.cursor()

cur.execute('''create table if not exists lol(
    id int primary key,
    t3 text not null,
    t4 text not null,
    t5 text not null,
    t6 text not null)
''')
conn.commit()

cur.execute("insert into lol values (2, 'rweq', 'wer', 'wedr', 'rew')")
conn.commit()

cur.execute("select * from lol")
for row in cur.fetchall():
    print(row)