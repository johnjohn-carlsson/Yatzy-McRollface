import random
from collections import Counter

class YatzyPlayer():
    def __init__(self) -> None:
        pass

    def set_players(self, players:list):
        self.amount_of_players = len(players)
        self.players = players

    def get_players(self):
        return self.players
    
    def final_score_calculator(self) -> dict:
        # Return final score dictionary in the form of [Player Name] = Score

        final_scores_dictionary = {}

        for player in self.players:
            bonus_score_counter = 0
            score = 0

            for key, value in player.scores.items():

                if key == "ones":
                    points = sum([x for x in value if x == 1])
                    score += points
                    bonus_score_counter += points

                elif key == "twos":
                    points = sum([x for x in value if x == 2])
                    score += points
                    bonus_score_counter += points

                elif key == "threes":
                    points = sum([x for x in value if x == 3])
                    score += points
                    bonus_score_counter += points

                elif key == "fours":
                    points = sum([x for x in value if x == 4])
                    score += points
                    bonus_score_counter += points

                elif key == "fives":
                    points = sum([x for x in value if x == 5])
                    score += points
                    bonus_score_counter += points

                elif key == "sixes":
                    points = sum([x for x in value if x == 6])
                    score += points
                    bonus_score_counter += points

                elif key == "one pair":
                    dice_counts = Counter(value)
                    pairs = [die for die, count in dice_counts.items() if count >= 2]
                    if pairs:
                        score += max(pairs) * 2  # Add the highest pair

                elif key == "two pairs":
                    dice_counts = Counter(value)
                    pairs = [die for die, count in dice_counts.items() if count >= 2 and count <= 3]
                    if len(pairs) >= 2:
                        score += sum(p * 2 for p in pairs[:2])  # Add the sum of both pairs

                elif key == "three of a kind":
                    dice_counts = Counter(value)  # Count occurrences of each die value
                    if any(count >= 3 for count in dice_counts.values()):
                        score += sum(value)

                elif key == "four of a kind":
                    dice_counts = Counter(value)
                    if any(count >= 4 for count in dice_counts.values()):
                        score += sum(value)

                elif key == "full house":
                    dice_counts = Counter(value) 
                    if sorted(dice_counts.values()) == [2, 3]:  # Check for one pair and one triplet
                        score += sum(value)

                elif key == "small straight":
                    if sorted(set(value)) == [1, 2, 3, 4, 5]:
                        score += 15

                elif key == "large staight":
                    if sorted(set(value)) == [2, 3, 4, 5, 6]:
                        score += 20

                elif key == "chance":
                    score += sum(value)

                elif key == "yatzy mcrollface!":
                    if len(set(value)) == 1:  # All dice must be the same
                        score += 50

            # If your upper score was more than 63 you get 50 extra points
            if bonus_score_counter >= 63: score += 50

            final_scores_dictionary[player.name] = score

        return final_scores_dictionary




class Player():
    def __init__(self, name: str) -> None:
        self.name = name
        self.saved_dice = {
            1:None,
            2:None,
            3:None,
            4:None,
            5:None
        }

        # For each round we replace None with a set of dice values
        self.scores = {
            "ones":None,
            "twos":None,
            "threes": None,
            "fours": None,
            "fives": None,
            "sixes": None,
            "one pair": None,
            "two pairs": None,
            "three of a kind": None,
            "four of a kind": None,
            "full house": None,
            "small straight": None,
            "large straight": None,
            "chance": None,
            "yatzy mcrollface!": None
        }
        

    def __repr__(self) -> str:
        return self.name
    
    def reset_saved_dice(self):
        self.saved_dice = {
            1:None,
            2:None,
            3:None,
            4:None,
            5:None
        }

    def get_saved_dice(self) -> list:
        # If there are dice that are not None; we return them in a list.

        saved_dice_values = []

        for key,value in self.saved_dice.items():
            if value is not None:
                saved_dice_values.append(value)

        return saved_dice_values

    def play_turn(self, dice, screenclear):
        
        # Make sure no saved dice from last round are counted
        self.reset_saved_dice()

        # Logic for two reroll rounds
        for round in range(2):
            
            screenclear()

            # Make a new roll with saved dice if there are any
            saved_dice = self.get_saved_dice()
            rolled_dice = self.roll_dice(saved_dice)

            # Print out round and dice info
            print(f"Round {round+1} - {self.name}")
            dice.print_dice(rolled_dice)

            new_dice_to_save = input("Select dice 1 - 5 to save (eg '123'):\n")

            if new_dice_to_save:
                valid_numbers = {'1', '2', '3', '4', '5'}
                valid_input = True

                # Check if input is valid
                for number in new_dice_to_save:
                    if number not in valid_numbers:
                        valid_input = False
                        break

                if valid_input:
                    # Save selected dice if valid input

                    list_of_dice_to_save = []
                    for number in new_dice_to_save:
                        list_of_dice_to_save.append(rolled_dice[int(number) - 1])

                    self.save_dice(list_of_dice_to_save)

        # Logic for the final scoring round
        screenclear()

        saved_dice = self.get_saved_dice()
        rolled_dice = self.roll_dice(saved_dice)

        print(f"Points round - {self.name}")
        dice.print_dice(rolled_dice)

        available_scores_dictionary = self.print_available_scores()
        valid_scores = [str(key) for key in available_scores_dictionary.keys()]

        print("Select points category:")
        selected_score = input("")
        
        # Check that input is valid
        while selected_score not in valid_scores:
            print(f"Invalid selection.")
            selected_score = input("")

        
        # Insert score at chosen category
        self.set_new_score(available_scores_dictionary, selected_score, rolled_dice)  

        # Display all categories
        screenclear()
        print("UPDATED SCORE:")
        for key,value in self.scores.items():
            if value == None:
                print(key)
            else:
                print(key, value)
        input()

    def set_new_score(self, available_scores_dictionary, selected_score, final_dice):
        # Find the correct category in scores and insert the final dice score

        for key, value in available_scores_dictionary.items():
            if key == int(selected_score):
                self.scores[value.lower()] = final_dice

    def print_available_scores(self):
        # Print the scores that are still set as None
        available_scores_dictionary = {}
        n = 1

        for key,value in self.scores.items():
            if value == None:
                available_scores_dictionary[n] = key
                print(f"{n}: {key.title()}")
                n += 1

        return available_scores_dictionary

    def roll_dice(self, saved_dice:list) -> list:
        # If there are saved dice, we make (5 - saved dice) new rolls

        if saved_dice:
            new_dicevalues = [random.randint(1, 6) for _ in range((5-len(saved_dice)))]
            for value in new_dicevalues:
                saved_dice.append(value)

            return saved_dice

        # If there are no saved dice we make 6 new rolls
        return [random.randint(1, 6) for _ in range(5)]

    def save_dice(self, values: list):
        self.reset_saved_dice()

        for n, value in enumerate(values):
            self.saved_dice[n+1] = value


    def get_saved_dice(self) -> list:
        return [value for key, value in self.saved_dice.items() if value != None]


    
class DiceDrawer():
    def __init__(self) -> None:
        # Visual graphics of the dice, one row per full die

        self.dice_faces = {
            1: [".---------.", "|         |", "|    o    |", "|         |", "'---------'"],
            2: [".---------.", "|  o      |", "|         |", "|      o  |", "'---------'"],
            3: [".---------.", "|  o      |", "|    o    |", "|      o  |", "'---------'"],
            4: [".---------.", "|  o   o  |", "|         |", "|  o   o  |", "'---------'"],
            5: [".---------.", "|  o   o  |", "|    o    |", "|  o   o  |", "'---------'"],
            6: [".---------.", "|  o   o  |", "|  o   o  |", "|  o   o  |", "'---------'"]
        }

    def print_dice(self, results: list):
        dice_rows = ["", "", "", "", ""]

        for result in results:
            face = self.dice_faces[result]
            for i in range(5):  # Each die has 5 rows
                dice_rows[i] += face[i] + "  "  # Spacing between dice

        for row in dice_rows:
            print(row)