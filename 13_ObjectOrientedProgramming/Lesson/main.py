class Player:
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg

    def weight_to_lbs(self):
        pounds = self.weight_kg * 2.20462262
        return pounds


class BasketballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists


class FootballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards


kev_dur = BasketballPlayer(first_name="Kevin", last_name="Durant", height_cm=210, weight_kg=108, points=27.2, rebounds=7.1, assists=4)

print(kev_dur.last_name)
print(kev_dur.rebounds)
print(kev_dur.weight_to_lbs())

messi = FootballPlayer(first_name="Lionel", last_name="Messi", height_cm=170, weight_kg=67, goals=575, yellow_cards=67, red_cards=0)

print(messi.first_name)
print(messi.goals)
print(messi.weight_to_lbs())


print("Enter some football player's data!")

f_name = input("Enter player's first name: ")
l_name = input("Enter player's last name: ")
height = input("Enter player's height: ")
weight = input("Enter player's weight: ")
goals = input("Enter the number of player's goals: ")
y_cards = input("Enter the number of player's yellow cards: ")
r_cards = input("Enter the number of player's red cards: ")

new_player = FootballPlayer(first_name=f_name, last_name=l_name, height_cm=float(height), weight_kg=float(weight),
                            goals=int(goals), yellow_cards=int(y_cards), red_cards=int(r_cards))

with open("football_players.json", "w") as football_file:
    football_file.write(str(new_player.__dict__))

print("Player successfully entered!")
print("Player's data: {0}".format(new_player.__dict__))
