# _*_ coding:utf-8 _*_
# Quick Python Script Explanation for Programmers

import os

def main():
    print('Hello World！')

    print("这是Alice\'的问候.")
    print('这是Bob\'的问候')

    foo(5, 10)

    print('=' * 10)
    print('这是直接执行'+os.getcwd())

    counter = 0
    counter += 1

    food = ['apple', 'pear', 'orange', 'grape', 'strawberry', 'watermelon']
    for i in food:
        print('my favorite fruit is %s' % i)

    print('数到10')
    for i in range(11):
        print(i)

def foo(param1, secondParam):
    res = param1 + secondParam
    print('%s + %s = %s' % (param1, secondParam, res))
    if (res < 50):
        print('this one')
    elif (res >= 50) and ((param1 == 42) or (secondParam == 24)):
        print('that one')
    else:
        print('okay')
    return res

'''
这是多行注释
'''

if __name__ == '__main__':
    main()






