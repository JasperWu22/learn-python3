import turtle
pen = turtle.Pen()
turtle.bgcolor("black")

colors = ["red", "green", "yellow", "blue", "orange", "purple", "white", "brown", "gray", "pink"]
family = []

name = turtle.textinput('my family', "enter a name")

while name != " ":
    family.append(name)
    name = turtle.textinput()