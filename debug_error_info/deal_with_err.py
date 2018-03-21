#正常的捕获异常
try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')


#多个except捕获不同类型的错误
try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
finally:
    print('finally...')
print('END')


# 在except后面增加else  没有异常时执行else
try:
    print('try...')
    r = 10 / 4
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')


#except 跨越多层调用
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        res = bar(2)
        print(res)
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')

main()


#记录错误
import logging

def main_1():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main_1()

print('Over!')