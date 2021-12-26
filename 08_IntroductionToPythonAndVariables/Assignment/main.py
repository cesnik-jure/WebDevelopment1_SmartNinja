import random

print("Guess the secret number between 1 and 10.")
secret_number = random.randint(1, 10)
print(secret_number)

guess_number = int(input("Your guess: "))

if secret_number == guess_number:
    print("You've guessed the secret number!")
else:
    print(f"Your guess is not correct. The secret number was {secret_number}")

