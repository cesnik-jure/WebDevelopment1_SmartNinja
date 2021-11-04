print("Hello world")

# integers
x = 5
y = 6
sum_all = x + y
print(sum_all)

name = input("Your name is: ")

print("Your name is:", name)

x = float(input("First number: "))
y = float(input("Second number: "))

sum_all = x + y
print("Sum of both numbers:", sum_all)

mood = None
while mood != "happy":
    mood = input("How do you feel today? ")

    if mood == "happy":
        print("Great to see you happy!")
    elif mood == "nervous":
        print("Just chill dude!")
    else:
        print("Are you happy or nervous?")




