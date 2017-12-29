std1 = {'name':'Michael', 'score':98}
std2 = {'name':'Bob', 'score':88}

def print_score(std):
    print('%s %s' % (std['name'], std['score']))

print_score(std1)
print_score(std2)

# 封装
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 98)
bart.print_score()
print(bart.get_grade())
lisa.print_score()
print(lisa.get_grade())


# 封装之private attribute
class Stu(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_name(self, name):
        self.__name = name

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def print_score(self):
        print('%s %s' % self.__name, self.__score)

cindy = Stu('Cindy', 100)
print(cindy._Stu__name)  # 强制访问
print(cindy.get_name())
cindy.set_name('Bao dan')
print(cindy.get_name())

# 继承
class Animal(object):
    def run(self):
        print('Animal is running ...')

class Dog(Animal):
    def run(self):
        print('Dog is running ...')

class Cat(Animal):
    def run(self):
        print('Cat is running ...')

dog = Dog()
dog.run()
cat = Cat()
cat.run()

a = list()
b = Animal()
c = Dog()

print(isinstance(a, list))
print(isinstance(b, Animal))
print(isinstance(c, Dog))
print(isinstance(c, Animal))


# 多态
def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
run_twice(Dog())
run_twice(Cat())

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

run_twice(Tortoise())

# 获取对象属性

class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()
print(obj.power())
print(hasattr(obj, 'x'))
print(hasattr(obj, 'y'))
setattr(obj, 'y', 18)
print(hasattr(obj, 'y'))
print(getattr(obj, 'y'))
print(obj.y)
print(getattr(obj, 'z', 404))

print(hasattr(obj, 'power'))
print(getattr(obj, 'power'))
fn = getattr(obj, 'power')
print(fn)
print(fn())


# 实例属性 和 类属性

class Teacher(object):
    name = 'Cindy'
    def __init__(self, name):
        self.name = name

t = Teacher('Michael')
t.score = 98
print(getattr(t, 'name', 404))
print(t.score)
print(Teacher.name)

class TeacherTest(object):
    name = 'Teacher'

# 注意区别 实例属性 和 类属性
test = TeacherTest()
print(test.name)
print(TeacherTest.name)
test.name = 'Student'
print(test.name)
print(TeacherTest.name)
del test.name
print(test.name)