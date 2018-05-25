card_list = []

def show_menu():
    """显示菜单"""
    print('*' * 30)
    print('欢迎使用【名片管理系统】 V1.0')
    print()
    print('1.新建名片')
    print('2.显示全部')
    print('3.查询名片')
    print()
    print('0.退出系统')
    print('*' * 30)



def add_card():
    """新增名片"""
    print("功能：新增名片")
    name = input("请输入姓名：")
    age = input("请输入年龄：")
    card_dict = {'name':name, 'age':age}
    card_list.append(card_dict)
    save_data(card_list)
    print("名片添加成功")



def show_all():
    """显示全部"""
    print("功能：显示全部")
    card_len = len(card_list)
    if card_len > 0:
        show_table_head()
        for card_dict in card_list:
            print("%s\t\t%s" % (card_dict['name'], card_dict['age']))
        show_table_tail()
    else:
        print("提示：没有任何名片记录")
        return



def search_card():
    """查询名片"""
    print("功能：查询名片")
    search_name = input("请输入要查询的姓名：")
    for card_dict in card_list:
        if search_name == card_dict['name']:
            show_table_head()
            print("%s\t\t%s" % (card_dict['name'], card_dict['age']))
            show_table_tail()
            deal_card(card_dict)  # 处理名片
            break
    else:
        print("没有找到 %s" % search_name)



def show_table_head():
    """显示表头"""
    print("姓名\t\t年龄")
    print('*' * 30)



def show_table_tail():
    """显示结尾"""
    print('*' * 30)



def deal_card(card):
    """处理名片"""
    while True:
        cmd_num = input("请输入对名片的操作：1、修改  2、删除  0、返回上一级 ")
        if cmd_num == "1":
            print("修改名片")
            card['name'] = input("请输入姓名：")
            card['age'] = input("请输入年龄：")
            save_data(card_list)
            print("名片修改成功")
            break
        elif cmd_num == "2":
            print("删除名片")
            card_list.remove(card)
            save_data(card_list)
            print("名片删除成功")
            break
        elif cmd_num == "0":
            break
        else:
            print("输入错误，请重新输入")




def save_data(data):
    """保存数据"""
    print("功能：保存数据")
    f = open("cards.data", "w")
    f.write(str(data))
    f.close()
    print("数据保存成功")



import os
def load_data():
    """读取数据"""
    if os.path.exists("cards.data"):
        f = open("cards.data", 'r')
        data = eval(f.read())
        print("保存的数据有：")
        print(data)
        f.close()




