"""

搬家具

"""

class Item:
    """家具类"""
    def __init__(self, type, area):
        self.type = type
        self.area = int(area)

    def __str__(self):
        return "家具为%s,占用面积为%d" % (self.type, self.area)



class Home:
    """房子类"""
    def __init__(self, address, area):
        self.address = address
        self.area = int(area)
        self.free_area = int(area)
        self.item_list = []

    def __str__(self):
        result_str = "房子在%s,面积为%d,剩余面积为%d" % (self.address, self.area, self.free_area)
        if len(self.item_list) > 0:
            result_str += ", 包含的家具有: "
            item_types = [item.type for item in self.item_list]
            result_str += ", ".join(item_types)
        return result_str

    def add_item(self, item):
        """添加家具"""
        if self.free_area >= item.area:
            print("%s 添加成功" % item.type)
            self.free_area -= item.area
            self.item_list.append(item)
        else:
            print("房子面积不足，%s 添加失败" % item.type)



item1 = Item('双人床', 4)
home = Home('陆家嘴', 300)
home.add_item(item1)

item2 = Item('冰箱', 1)
home.add_item(item2)

item3 = Item('梳妆台', 3)
home.add_item(item3)

print(home)




print("=" * 50)


class Animal():
    def eat(self):
        print('---吃---')

    def run(self):
        print('---动物在跑---')


class Dog(Animal):
    def bark(self):
        print('---汪汪叫---')

    def run(self):
        print('---狗在跑---')


class XTQ(Dog):
    def bark(self):
        print('---嚎叫---')

    def see_host(self):
        print('---摇尾巴---')

        # 子类重写了父类的方法，仍然想执行父类中的方法，则可以在类中使用 super() 来调用方法 ， 需重点理解
        Dog.bark(self)      #方法一
        super(XTQ, self).bark()     # 方法二
        super().bark()       # 方法三


xtq = XTQ()
xtq.eat()
xtq.run()
xtq.bark()
xtq.see_host()


print("=" * 50)


class Dog2():
    def eat(self):
        print("吃东西")


class God():
    def eat(self):
        print("吃蟠桃")


class XTQ2(God, Dog2):
    pass


xtq2 = XTQ2()
xtq2.eat()

print(XTQ2.__mro__)   # 查看继承顺序


print()
print('*' * 50)

"""

多态：同类对象的多种形态（子类化）
实现多态的步骤：
    1、实现继承关系
    2、重写父类方法
    3、使用子类对象执行父类处理

"""

class People:
    def dance(self):
        print("跳舞")

    def play(self):
        self.dance()


class OldMan(People):
    def dance(self):
        print("跳广场舞")


class Boy(People):
    def dance(self):
        print("跳街舞")


people = People()
people.play()

oldMan = OldMan()
oldMan.play()

youngMan = Boy()
youngMan.play()


print('*' * 50)


"""
__new__

"""

class Cat:

    def __new__(cls, *args, **kwargs):
        return '123'

    def __init__(self):
        print('对象初始化')



cat = Cat()
print(cat)
print(type(cat))


print('*' * 50)


"""

单例模式:让类创建出的对象始终只有一个   需重点理解

"""

class ShoppingCart:

    __instance = None
    __has_init = False

    def __new__(cls, *args, **kwargs):

        if cls.__instance is None:
            new_obj = object.__new__(cls)

            cls.__instance = new_obj

        return cls.__instance


    def __init__(self):
        if not ShoppingCart.__has_init:
            self.total_price = 100
            ShoppingCart.__has_init = True




cart1 = ShoppingCart()
cart1.total_price += 100
print(cart1)
print(cart1.total_price)

cart2 = ShoppingCart()
cart2.total_price += 100
print(cart2)
print(cart2.total_price)






