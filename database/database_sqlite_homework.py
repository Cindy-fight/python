# !/usr/bin/env python
# ! -*- coding:UTF-8 -*-

import sqlite3
import os

db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")

cursor.close()
conn.commit()
conn.close()



def get_score_in(low, high):
    try:
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM user where score >= ? AND score <= ? ORDER BY score ASC', (low, high))
        values = cursor.fetchall()
    finally:
        cursor.close()
    conn.commit()
    conn.close()
    return values

if __name__ == '__main__':
    r1 = get_score_in(80, 95)
    print('the score between 80 and 95 are：')
    print(r1)
    r2 = get_score_in(60, 80)
    print('the score between 60 and 80 are：：')
    print(r2)
    r3 = get_score_in(60, 100)
    print('the score between 60 and 100 are：：')
    print(r3)


