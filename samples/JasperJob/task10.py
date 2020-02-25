import turtle
t = turtle.Pen()
while True:
    answer = input("Do you want to see a thing if you do? Please press 'D-R-A-W'.")
    if answer == "draw":
        for x in range(100):
            t.forward(x * 5)
            t.left(86)
        break
    else:
        print("|  [ 7, oh no! ]       |")
        print("|     {O ^ O}          |")
        print("")
        print("You can try again!")
print("Thank you for playing the game!")