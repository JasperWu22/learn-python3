import random
def throw(num):
    s = 0
    for i in range(num):
        x = random.randint(1, 6)
        s += x
    return s

n = int(input("输入要用的骰子的数量:"))
print(" ")

name1 = input("玩家1的名字:")
r = throw(n)
print('点数和是:', r)

name2 = input("玩家2的名字:")
s = throw(n)
print('点数和是:', s)

name3 = input("玩家3的名字:")
t = throw(n)
print('点数和是:', t)

if r > s and r > t:
    print(name1, '赢了')
elif s > r and s > t:
    print(name2, '赢了')
elif t > s and t > r:
    print(name3, '赢了')