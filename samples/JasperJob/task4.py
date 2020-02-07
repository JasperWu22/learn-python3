# Import turtle
import turtle
t = turtle.Pen()
# Asked player to write how many circles.
draw = int(input("圆圈数:"))
# Draw the circles.
for x in range(draw):
    t.circle(100)
    t.left(360/draw)