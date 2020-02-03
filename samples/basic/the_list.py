#!/usr/bin/env python3
# -*- coding: utf-8 -*-

classmates = ['Michael', 'Bob', 'Tracy', "Jasper"]

d = {
    "Michael": 100,
    "Bob": 90,
    "Tracy": 38,
    "Jasper": 100,
}

for x in d:
    if d[x] <= 40:
        print(x,"失败")
    else:
        print(x,"成功")

print('classmates =', classmates)
print('len(classmates) =', len(classmates))
print('classmates[0] =', classmates[0])
print('classmates[1] =', classmates[1])
print('classmates[2] =', classmates[2])
print('classmates[3] =', classmates[3])
print('classmates[-1] =', classmates[-1])
classmates.pop()
print('classmates =', classmates)
