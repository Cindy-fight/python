import pickle

d = dict(name='Bob', age=20, score=98)
pickle.dumps(d)

f = open('test.txt', 'wb')
pickle.dump(d, f)
f.close()

fr = open('test.txt', 'rb')
d1 = pickle.load(fr)
fr.close()

print(d)
print(d1)



import json

d_json = dict(name='Lucy', age=22, score=100)
d_str = json.dumps(d_json)
print(d_str)

print(json.loads(d_str))

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def student2dict(std):
    return {
        'name': std.name,
        'age':std.age,
        'score':std.score
    }

s = Student('Cindy', '23', '88')
print(json.dumps(s, default=student2dict))

print(json.dumps(s, default=lambda obj: obj.__dict__))

class Teacher(object):
    def __init__(self, name, sex, address, mobile):
        self.name = name
        self.sex = sex
        self.address = address
        self.mobile = mobile

t = Teacher('baoDan', 'male', 'shangHai', '1314520')
print(json.dumps(t, default=lambda obj: obj.__dict__))
print(json.dumps(t.__dict__))

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

studentStr = '{"name": "Lucy", "age": 22, "score": 100}'
print(json.loads(studentStr, object_hook=dict2student))
# print(json.loads(studentStr.dict2student()))
# print(json.dumps(s.student2dict()))
# json.dumps(s.student2dict())



