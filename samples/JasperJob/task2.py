import random
w = []
e = []
while True:
    name1 = (input("your name:"))
    if name1 == "Q":
        break
    x = random.randint(1, 100)
    w.append(name1)
    e.append(x)
print(e)
print(w)
o = sum(e)
p = max(e)
a = min(e)
print("总和是:", o)
print("最大值是:", p)
print("最小值是:", a)