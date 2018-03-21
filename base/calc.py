#!/usr/bin/env python3
# ! -*- coding:UTF-8 -*-

print(100+200+300)
print('100+200+300 = ', 100+200+300)
print(1024 * 768)
print('1024 * 768 = ', 1024 * 768)

import math

area = math.pi * 3 * 3
print(area)

value = math.sqrt(18)
print(value)

def move(x, y, step, angle = 0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
 
r = move(100, 100, 60, math.pi / 6)
print(r)

def quadratic(a, b, c):
	if a == 0 and b == 0:
		x = '无解'
		return x
	elif a == 0 and b != 0:
		x = - (c / b)
		return x
	else:
		delta = (b * b) - (4 * a * c)
		if delta < 0:
			x = 'x没有实数解'
			return x
		elif delta == 0:
			x = - (b / 2 * a)
			return x
		else:
			x1 = (-b + math.sqrt(delta)) / (2 * a)
			x2 = (-b - math.sqrt(delta)) / (2 * a)
			return x1,x2

print(quadratic(1, 3, -4))
print(quadratic(2, 3, 1))
print(quadratic(1, 2, 1))
