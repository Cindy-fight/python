#!/usr/bin/env python
#！-*- coding:UTF-8 -*-

name = input('please enter your name:')
print('Hello,', name)
print('\n')
print('n = ', 123)
print('f = ', 456.789)
print('s1 = ',"'Hello, world'")
print('s2 = ',"'Hello, \\\'Admin\\\''")
print('s3 = ','r\'Hello, \"Bart\"\'')
print('s4 = ',"r\'\'\'Hello,")
print('Lisa!\'\'\'')
print("Lisa!'''")

# practice2
s1 = 72
s2 = 85
float = (s2-s1)/s2
percent = '百分比是 : %.1f %%' % (float*100)
print(percent)  

score1 = int(input('请输入你去年的成绩：'))
score2 = int(input('请输入你今年的成绩：'))
if(score1 > score2):
    r1 = (score1-score2) / score1 * 100
    print('Hi, %s. 你的成绩相比去年下降了 %.1f %% .' % (name, r1))
else:
    r1 = (score2-score1)/score2 * 100
    print('Hi, %s. 你的成绩相比去年提升了 %.1f %% .' % (name, r1))



# practice list and tuple
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0],'\n',L[1][1],'\n',L[2][2])
