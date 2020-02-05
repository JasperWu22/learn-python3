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