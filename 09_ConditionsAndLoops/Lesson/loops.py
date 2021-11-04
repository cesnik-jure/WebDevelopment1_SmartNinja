# secret = 22

# guess = int(input("Guess the secret number (between 1 and 30): "))
#
# if guess == secret:
#     print("You've guessed it - congratulations! It's number 22.")
# else:
#     print("Sorry, your guess is not correct... The secret number is not " + str(guess))
#
# while guess != secret:
#     guess = int(input("Guess the secret number (between 1 and 30): "))
#
#     if guess == secret:
#         print("You guessed it - congratulations! It's number 22.")
#     else:
#         print("Sorry, your guess is not correct... The secret number is not " + str(guess))
#
# for x in range(5):
#     guess = int(input("Guess the secret number (between 1 and 30): "))
#
#     if guess == secret:
#         print("You've guessed it - congratulations! It's number 22.")
#         break
#     else:
#         print("Sorry, your guess is not correct... The secret number is not " + str(guess))

# while True:
#     guess = int(input("Guess the secret number (between 1 and 30): "))
#
#     if guess == secret:
#         print("You've guessed it - congratulations! It's number 22.")
#         break
#     elif guess > secret:
#         print("Your guess is not correct... try something smaller")
#     elif guess < secret:
#         print("Your guess is not correct... try something bigger")


import random


secret = random.randint(1, 30)

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))

    if guess == secret:
        print("You've guessed it - congratulations! It's number " + str(secret))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")