name = input("what is your name?")
name1 = int(input("How many names do you want?"))
while name != "":
    for x in range(name1):
        print(name, end = " ")
    print()
    name = input("Type another name or none thing:")
    name1 = int(input("How many names do you want?"))
print("Thanks for playing the game!")