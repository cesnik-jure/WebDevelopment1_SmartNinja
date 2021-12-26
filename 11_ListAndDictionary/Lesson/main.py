import random
import json
import datetime

secret = random.randint(1, 30)
attempts = 0
wrong_guess_list = []

with open("score_list.json", "r") as score_file:
    score_list = json.loads(score_file.read())

print("Top score:")
score_list_sorted = sorted(score_list, key=lambda item: item["attempts"])[:3]
for score_dict in score_list_sorted:
    print(score_dict.get("name") + ", " + str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date"))

player_name = input("Enter name: ")

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))

        score_list.append({"attempts": attempts,
                           "date": str(datetime.datetime.now()),
                           "name": player_name,
                           "secret_number": secret,
                           "wrong_guesses": wrong_guess_list})

        with open("score_list.json", "w") as score_file:

            score_file.write(json.dumps(score_list))

        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
        wrong_guess_list.append(guess)
    elif guess < secret:
        print("Your guess is not correct... try something bigger")
        wrong_guess_list.append(guess)
