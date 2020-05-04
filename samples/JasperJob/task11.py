driving_age = int(input("tell me about how old enough to drive your car:"))
your_age = int(input("how old are you:"))
if your_age >= driving_age:
    print("you are old enough to drive!")
else:
    print("sorry, you can't drive a car with", your_age, "years old!")
    print("you need to be", driving_age, "years old  or more, so you can drive the car!")

