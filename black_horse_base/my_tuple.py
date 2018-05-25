'''
tuple

1 index
2 len
3 if in
4 count

'''

my_tuple = (13, 5, 8, 5)
print(my_tuple)

tuple_index = my_tuple.index(5)
print(tuple_index)

tuple_len = len(my_tuple)
print(tuple_len)

if 5 in my_tuple:
    print('OK')

tuple_count = my_tuple.count(5)
print(tuple_count)