
user_number = int(input("Select a number between 1 and 100: "))

for i in range(1, user_number+1):
    if i % 5 == 0 and i % 3 == 0 :
        print("fizzbuzz")
    elif i % 5 == 0:
        print("buzz")
    elif i % 3 == 0:
        print("fizz")
    else:
        print(i)


