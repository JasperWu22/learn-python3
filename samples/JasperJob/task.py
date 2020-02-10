import turtle
import random
t = turtle.Pen()
t.shape("turtle")
t.speed(0)
for i in range(100):
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    t.begin_fill()
    t.circle(100)
    t.left(90)
    t.end_fill()
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.clear()