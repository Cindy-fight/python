# !/usr/bin/env python
# ! -*- coding:UTF-8 -*-

import mysql.connector

conn = mysql.connector.connect(user='root', password='Mtt2017', database='webapp')

cursor = conn.cursor()

cursor.execute(r"insert into users (id, email, passwd, admin, name, image, created_at) values(2, 'YRC@maimob.com', 123456, 1, 'BaoDan', '3333.jpg', '2018-03-21')")

print(cursor.rowcount)

cursor.execute('select * from users')

values = cursor.fetchall()

print(values)

cursor.close()

conn.commit()

conn.close()

