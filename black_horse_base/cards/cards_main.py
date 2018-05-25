import cards_tool

"""

名片管理系统
1.新建名片
2.显示名片
3.查询名片

"""

cards_tool.load_data()
while True:

    # 1、显示菜单
    cards_tool.show_menu()

    # 2、获取用户的输入
    cmd_num = input("请选择执行的操作：")
    print("您选择的功能是： %s" % cmd_num)

    # 3、条件判断 根据用户输入，执行功能
    if cmd_num == "1":
        cards_tool.add_card()

    elif cmd_num == "2":
        cards_tool.show_all()

    elif cmd_num == "3":
        cards_tool.search_card()

    elif cmd_num == "0":
        print("欢迎再次使用【名片管理系统】")
        break
    else:
        print("输入错误，请重新输入.")