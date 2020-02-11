import turtle
import random
import time
t = turtle.Pen()
name = input("your name:")
how_many_circle = int(input("how many circles do you want?"))
for x in range(1, 100):
    xcon = random.randint(1, 100)
    ycon = random.randint(1, 100)
    t.circle(100)
    t.left(360/how_many_circle)
    t.penup()
    t.goto(xcon, ycon)
    t.pendown()
    t.write(name)
    time.sleep(3)