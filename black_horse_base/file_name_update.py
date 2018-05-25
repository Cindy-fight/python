"""

实现功能：批量修改文件名

"""

import os

path = input("请输入需要批量修改文件名的文件夹名称：")

os.chdir(path)

full_path = os.getcwd()
print(full_path)

for subpath_name in os.listdir():
    # new_file_name = subpath_name[10:]
    new_file_name = "[wtt]" + subpath_name
    os.rename(subpath_name, new_file_name)
