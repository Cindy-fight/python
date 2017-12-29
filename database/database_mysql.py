# 导入MySQL驱动:
import mysql.connector

conn = mysql.connector.connect(user='root', password='Mtt2017', database='webapp')

cursor = conn.cursor()

cursor.execute(r"insert into users (id, email, passwd, admin, name, image, created_at) values(2, 'wtt@163.com', 66666, 1, 'BaoDan', '3333.jpg', '2017-11-15')")

print(cursor.rowcount)

cursor.execute('select * from users')

values = cursor.fetchall()

print(values)

cursor.close()

conn.commit()

conn.close()

