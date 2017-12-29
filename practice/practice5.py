import os

print([x for x in os.listdir('.') if os.path.isdir(x)])

print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])

for x in os.listdir('.'):
    if os.path.isfile(x):
        print(x, 'is file')
    elif os.path.isdir(x):
        print(x, 'is dir')
    else:
        print(x, 'is what?')
        