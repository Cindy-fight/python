
"""

实现功能：文件拷贝

"""

file_name = input("请输入拷贝文件名：")

old_file= open(file_name, 'r')

dot_index = file_name.rfind('.')
# print(dot_index)

new_file_name = file_name[:dot_index] + "[复件]" + file_name[dot_index:]
# print(file_name[:dot_index])
# print(file_name[dot_index:])

new_file = open(new_file_name, 'w')

content = old_file.read()

new_file.write(content)

old_file.close()

new_file.close()