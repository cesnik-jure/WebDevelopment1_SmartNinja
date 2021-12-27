import random
import json
import datetime


def play_game(level="easy", score_list="[]"):
    secret = random.randint(1, 30)
    attempts = 0
    wrong_guess_list = []

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
        elif guess > secret and level == "easy":
            print("Your guess is not correct... try something smaller")
            wrong_guess_list.append(guess)
        elif guess < secret and level == "easy":
            print("Your guess is not correct... try something bigger")
            wrong_guess_list.append(guess)


def get_score_list():
    with open("score_list.json", "r") as file:
        results_list = json.loads(file.read())

        return results_list


def get_top_scores(score_list):
    print("Top score:")
    score_list_sorted = sorted(score_list, key=lambda item: item["attempts"])[:3]
    for score_dict in score_list_sorted:
        print(
            score_dict.get("name") + ", " + str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date"))


def main():
    score_list = get_score_list()
    get_top_scores(score_list)

    player_continue = "Y"
    game_level = input("Game level? hard/easy ").lower()

    while player_continue.upper() == "Y":
        play_game(game_level, score_list)
        player_continue = input("Continue? (Y/N) ")


if __name__ == "__main__":
    main()
