import random
a = random.randint(1, 15)
time = 1
while True:
    d = int(input('输入距离:'))
    if d == a:
        print('猜对了')
        print('你用了', time, "次去击中这个数字", a, "!")
        break
    if d > a:
        print('太大了')
        print('')
        time += 1
    if d < a:
        print('太小了')
        print('')
        time += 1