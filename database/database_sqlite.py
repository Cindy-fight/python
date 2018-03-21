# !/usr/bin/env python
# ! -*- coding:UTF-8 -*-

import sqlite3

conn = sqlite3.connect('test.db')

cursor = conn.cursor()

# cursor.execute('create TABLE user (id varchar(20) PRIMARY KEY , name varchar(20))')

# cursor.execute('insert INTO user (id, name) VALUES (\'1\', \'Michael\')')
# cursor.execute('insert INTO user (id, name) VALUES (\'2\', \'Cindy\')')

print(cursor.rowcount)

cursor.close()

conn.commit()

conn.close()



conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute('select * from user where id = ?',('2',))

values = cursor.fetchall()

print(values)

cursor.close()
conn.close()
