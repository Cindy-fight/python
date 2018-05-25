"""

反恐精英游戏

"""



class Gun:
    """

    枪类
    参数：型号modal  str
         杀伤力 damage  int
         子弹数量 bullet_count int 枪初始没有子弹

    """

    def __init__(self, modal, damage):
        self.modal = modal
        self.damage = damage
        self.bullet_count = 0


    def __str__(self):
        return "枪的型号是%s,杀伤力是%d,剩余子弹数量是%d" % (self.modal, self.damage, self.bullet_count)


    def add_bullets(self, count):
        """
        装填子弹
        :param count: 装填子弹数量
        """
        self.bullet_count += count
        print("装填子弹完成，剩余子弹数量:%d" % self.bullet_count)


    def shoot(self, enemy):
        """
        射击敌人

        思路：
        1、如果没有子弹，则提示玩家并且返回
        2、子弹数量减少
        3、如果有子弹，则  调用敌人的 hurt 方法，给敌人造成伤害

        :param enemy:瞄准的敌人

        """
        if self.bullet_count <= 0:
            print("子弹不足，无法射击")
            return

        self.bullet_count -= 1
        print("发射1颗子弹，剩余：%d" % self.bullet_count)

        if enemy is not None:
            enemy.hurt(self)




class Player:
    """

    玩家类

    参数： 姓名 name  str
          血量  hp   int
          枪 gun 初始没有枪    使用Gun类 创建的对象

    """
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.gun = None

    def __str__(self):
        if self.hp <= 0:
            return "%s 已经挂了..." % self.name

        if self.gun is None:
            return "%s[%d] 没有武器" % (self.name, self.hp)

        return "%s[%d] 武器：{%s}" % (self.name, self.hp, self.gun)

    def hurt(self, enemy_gun):
        """
        玩家被 enemy_gun 击中
        :param enemy_gun: 敌人的枪

        思路：
        1、玩家血量 减去 枪对象 的 damage 伤害度
        2、判断修改后的玩家血量  如果 血量 <= 0, 提示 玩家  挂了，  否则， 提示 玩家受伤 以及当前血量

        """

        self.hp -= enemy_gun.damage

        if self.hp <= 0:
            print("%s 被 %s 击毙！！！" % (self.name, enemy_gun.modal))
        else:
            print("%s 被 %s 击中，剩余血量：%d" % (self.name, enemy_gun.modal, self.hp))


    def fire(self, enemy):

        """
        开火 思路：
        1、判断自己是否有武器，如果没有直接返回
        2、检查自己的枪是否有子弹，如果没有，自动装填子弹
        3、让自己的枪 调用 shoot 方法， 并传递 要射击的敌人对象
        :param enemy:
        """

        if self.gun is None:
            print("%s 没有武器，请先装配武器" % self.name)
            return

        if self.gun.bullet_count <= 0:
            self.gun.add_bullets(10)

        print("%s 正在向 %s 开火" % (self.name, enemy.name))
        self.gun.shoot(enemy)






def test():
    """
    主程序流程：
    1、创建 枪对象 并测试 装填和发射子弹
    2、创建 警察对象 policeman 和 匪徒对象 badman
    3、将 枪交给警察， 警察 向 匪徒 开火
    4、利用 循环 消灭匪徒

    """
    print('*' * 20 + "枪类测试开始" + '*' * 20)
    ak47 = Gun('ak47', 50)
    print(ak47)
    ak47.add_bullets(20)
    print(ak47)
    ak47.shoot(None)
    print(ak47)
    print('*' * 20 + "枪类测试完成" + '*' * 20)
    print()

    print('*' * 20 + "玩家类测试开始" + '*' * 20)
    policeman = Player('警察')
    print(policeman)

    badman = Player('匪徒')
    print(badman)

    policeman.gun = ak47
    print(policeman)

    badman.hurt(ak47)
    print(badman)

    badman.hurt(ak47)
    print(badman)


    policeman.fire(badman)
    print(policeman)
    print(badman)

    policeman.fire(badman)
    print(policeman)
    print(badman)

    print('*' * 20 + "玩家类测试完成" + '*' * 20)



def main():
    """
    主程序流程：
    1、创建 枪对象 并测试 装填和发射子弹
    2、创建 警察对象 policeman 和 匪徒对象 badman
    3、将 枪交给警察， 警察 向 匪徒 开火
    4、利用 循环 消灭匪徒

    """

    ak47 = Gun('ak47', 50)

    policeman = Player('警察')
    print(policeman)

    badman = Player('匪徒')
    print(badman)

    policeman.gun = ak47

    while badman.hp > 0:
        policeman.fire(badman)

    print(policeman)
    print(badman)


if __name__ == '__main__':
    main()
