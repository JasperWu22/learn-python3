import turtle
t = turtle.Pen()
t.penup()
turtle.bgcolor("black")
sides = int(turtle.numinput("How many sides", "How many sides do you want? (2 ~ 6)", 4, 2, 6))
colors = ["red", "orange", "yellow", "green", "blue", "purple", "gold"]
t.pendown()
def draw_cube(num):
    t.color(colors[num % len(colors)])
    for x in range(4):
        t.forward(num)
        t.left(90)
for m in range(100):
    draw_cube(m * 5)