import turtle
t = turtle.Pen()
draw = int(input("圆圈数:"))
for x in range(draw):
    t.circle(100)
    t.left(360/draw)