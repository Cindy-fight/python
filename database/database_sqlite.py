# 导入SQLite驱动:
import sqlite3

# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建:
conn = sqlite3.connect('test.db')

# 创建一个Cursor:
cursor = conn.cursor()

# 执行一条SQL语句，创建user表:
# cursor.execute('create TABLE user (id varchar(20) PRIMARY KEY , name varchar(20))')

# 继续执行一条SQL语句，插入一条记录:
# cursor.execute('insert INTO user (id, name) VALUES (\'1\', \'Michael\')')
# <sqlite3.Cursor object at 0x105974810>

# 通过rowcount获得插入的行数:
cursor.rowcount
# 1

# 关闭Cursor:
cursor.close()

# 提交事务:
conn.commit()

# 关闭Connection:
conn.close()



# 每次执行都需要重新打开
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# 执行查询语句:
cursor.execute('select * from user where id =?', ('1', ))
# <sqlite3.Cursor object at 0x105974880>

# 获得查询结果集:
values = cursor.fetchall()

print(values)
# [('1', 'Michael')]

cursor.close()
conn.close()
