import keyword

print(keyword.kwlist)

price = 9.00
weight = 5.00
total_price = price * weight
print("苹果单价是 %.02f 元/斤， 购买 %.02f 斤, 需要支付 %.02f 元." % (price, weight, total_price))

import random
print(random.randint(10,20))
print(random.random() * 10)
print(random.randrange(0, 100, 5))


# practice list
# 开发姓名管理系统，完成添加姓名、删除姓名、显示全部姓名功能
# 提示  请输入操作：1、添加姓名 2、删除姓名   3、显示全部姓名 4、退出程序

name_list = []

while True:
    cmd_num = input("请输入操作：1、添加姓名/ 2、删除姓名/ 3、显示全部姓名/ 4、退出程序")

    if cmd_num == "1":
        add_name = input("请输入添加的姓名：")
        name_list.append(add_name)
        print("姓名添加成功.")
    elif cmd_num == "2":
        del_name = input("请输入要删除的姓名:")
        if del_name in name_list:
            name_list.remove(del_name)
            print("姓名删除成功.")
        else:
            print("列表中不包含 %s" % del_name)
    elif cmd_num == "3":
        if len(name_list) == 0:
            print("没有记录任何名片.")
        else:
            result_str = ""
            for name in name_list:
                result_str += name + " "
            print(result_str)
    elif cmd_num == "4":
        print("退出程序.")
        break
    else:
        print("输入错误，请重新输入.")



# practice dict
# 开发登录注册系统，完成用户注册、用户登录功能
# 提示  请输入操作：1、用户注册 2、用户登录 3、退出程序

user_list = []

while True:
    cmd_num = input("请输入操作：1、用户注册 2、用户登录 3、退出程序 ：")

    if cmd_num == "1":
        reg_name = input("请输入用户名：")
        for user in user_list:
            if user["name"] == reg_name:
                print("用户已注册.")
                break
        else:
            reg_pwd = input("请输入密码：")
            user = {"name":reg_name, "pwd":reg_pwd}
            user_list.append(user)
            print("注册成功.")
    elif cmd_num == "2":
        log_user = input("请输入用户名：")
        log_pwd = input("请输入密码：")
        for user in user_list:
            if user['name'] == log_user and user['pwd'] == log_pwd:
                print("登陆成功.")
                break
        else:
            print("登录失败.")
    elif cmd_num == "3":
        print("退出程序.")
        break
    else:
        print("输入错误，请重新输入.")



my_str = 'Hello World!'
print(my_str)

#  字符串的逆序
print(my_str[::-1])   # !dlroW olleH

# set 1去重 2无序
print(set(my_str))
