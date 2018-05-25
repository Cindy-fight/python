'''
dict
1 pop
2 del
3 clear
4 dict[key] = val
5 update
6 setdefault
7 get
8 for key in dict
9 for key in dict.keys()
10 for value in dict.values()
11 for item in dict.items()

'''

my_dict = {'name':'Cindy', 'address':'SH', 'sex':'female'}
print(my_dict)

my_dict['age'] = 18
print(my_dict)

dict_pop = my_dict.pop('age')
print(dict_pop)
print(my_dict)

del my_dict['address']
print(my_dict)

my_dict.clear()
print(my_dict)

my_dict = {'name':'Cindy', 'age':18, 'address':'SH', 'sex':'female'}
print(my_dict)

my_dict.update({'age':22, 'height':1.8})
print(my_dict)

my_dict.setdefault('height', 1.7)
my_dict.setdefault('hobby', 'program')
print(my_dict)

print(my_dict['address'])

print(my_dict.get('name'))
print(my_dict.get('weight'))
print("====================================================")

for key in my_dict:
    print(key)

print("====================================================")

for key in my_dict.keys():
    print(key)

print("====================================================")

for value in my_dict.values():
    print(value)

print("====================================================")

for item in my_dict.items():
    print(item)
