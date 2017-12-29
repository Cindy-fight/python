# print absolute value of an integer:
a = 100
if a >= 0:
    print(a)
else:
    print(-a)


# Test Boolean
age = input('please enter your age:')
age = int(age)
if age >= 18:
    print('Adult')
else:
    print('Teenager')


# calculate BMI
height = float(input('请输入你的身高，单位m：'))
weight = float(input('请输入你的体重，单位kg：'))
BMI = '%.1f' % (weight/(height * height))
BMI = float(BMI)
print('BMI值为:', BMI)
# method1
if(BMI > 32.0):
    print('严重肥胖')
elif(BMI >= 28.0):
    print('肥胖')
elif(BMI >= 25.0):
    print('过重')
elif(BMI >= 18.5):
    print('正常')
elif(BMI < 18.5):
    print('过轻')
else:
    print('不在检测范围内')

# method2
if(BMI < 18.5):
    print('过轻，亲，该加餐了哦')
elif(BMI >= 18.5 and BMI < 25.0):
    print('正常，亲，身材很好哦')
elif(BMI >= 25.0 and BMI < 28.0):
    print('过重，亲，有点肉肉了哈')
elif(BMI >= 28.0 and BMI <= 32.0):
    print('肥胖，亲，该减肥了')
elif(BMI > 32.0):
    print('严重肥胖，我的天，赶紧去减肥')






