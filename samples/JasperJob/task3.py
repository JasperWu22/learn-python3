# 抽奖环节。
import random
# 定义gift, encourage列表。
gift = ["未抽中礼物", "获得水杯", "获得陀螺", "获得乐高", "获得书本", "获得彩笔"]
encourage = ["再来一次吧！"]
while True:
    # 询问名字。
    name = input("名字:")
    # 判断name是否等于大写Q，是的话就跳出循环。
    if name == "Q":
        break
    # 生成随机数。
    t = random.randint(0, 5)

    # 打印礼物，判断t是否等于0如果是的话就打印"未抽中礼物,再来一次吧！"否则就打印礼物并跳出循环。
    if t == 0:
        print(gift[0])
        print(encourage[0])
    else:
        print(name, gift[t])
        break


