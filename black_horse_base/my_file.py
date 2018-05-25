import os

"""
文件相关操作
"""

# os.rename('123.txt', '333.txt')   # 重命名
# os.remove('333.txt')   # 删除
# os.mkdir('wtt')    # 新建文件夹
os.getcwd()        # 获取当前目录
print(os.getcwd())
# os.chdir('test')   # 改变默认目录
os.listdir()       # 获取目录列表
print(os.listdir())
# os.rmdir()         # 删除文件夹