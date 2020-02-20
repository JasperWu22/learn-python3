import turtle
t = turtle.Pen()
turtle.bgcolor("black")

colors = ["red", "green", "yellow", "blue", "orange", "purple", "white", "brown", "gray", "pink"]
family = []

name = turtle.textinput('my family', "enter a name")

while name != "":
    family.append(name)
    name = turtle.textinput("my family'", "enter a name")

for x in range(100):
    t.pencolor(colors[x % len(family)])
    t.penup()
    t.forward(x * 4)
    t.pendown()
    t.write(family[x % len(family)], font = ("Arial", int((x + 4) / 4), "bold"))
    t.left(360 / len(family) + 2)