import random
import os

class YatzyPlayer():
    def __init__(self) -> None:
        pass

    def set_players(self, players:list):
        self.amount_of_players = len(players)
        self.players = players

    def get_players(self):
        return self.players
    
    def final_score_calculator(self, scores:list):
        # Here we iterate through each players score dictionary and calculate totals
        pass



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
        self.scores = {
            "ones":None,
            "twos":None,
            "threes": None,
            "fours": None,
            "fives": None,
            "sixes": None,
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

    def get_saved_dice(self):
        saved_dice_values = []

        for key,value in self.saved_dice.items():
            if value is not None:
                saved_dice_values.append(value)

        return saved_dice_values

    def play_turn(self, dice, screenclear):
        
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

            # Check if user saves dice
            new_dice_to_save = input("Select dice 1 - 5 to save (eg '123'):\n")
            if new_dice_to_save:

                list_of_dice_to_save = []
                for number in new_dice_to_save:
                    list_of_dice_to_save.append(rolled_dice[int(number)-1])

                self.save_dice(list_of_dice_to_save)

        # Logic for the final scoring round
        screenclear()

        saved_dice = self.get_saved_dice()
        rolled_dice = self.roll_dice(saved_dice)

        print(f"Final round - {self.name}")
        dice.print_dice(rolled_dice)
        available_scores_dictionary = self.print_available_scores()
        selected_score = input("")

        self.set_new_score(available_scores_dictionary, selected_score, rolled_dice)  

        print("UPDATED SCORE:")
        for key,value in self.scores.items():
            print(key, value)
        input()

    def set_new_score(self, available_scores_dictionary, selected_score, final_dice):
        for key, value in available_scores_dictionary.items():
            if key == int(selected_score):
                self.scores[value.lower()] = final_dice

    def print_available_scores(self):
        available_scores_dictionary = {}
        n = 1

        for key,value in self.scores.items():
            if value == None:
                available_scores_dictionary[n] = key
                print(f"{n}: {key.title()}")
                n += 1

        return available_scores_dictionary

    def roll_dice(self, saved_dice:list) -> list:
        # If there are saved dice, we make 5 - saved_dice new rolls
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
        # Visual graphics of the dice
        self.dice_faces = {
            1: ["-----", "|   |", "| * |", "|   |", "-----"],
            2: ["-----", "|*  |", "|   |", "|  *|", "-----"],
            3: ["-----", "|*  |", "| * |", "|  *|", "-----"],
            4: ["-----", "|* *|", "|   |", "|* *|", "-----"],
            5: ["-----", "|* *|", "| * |", "|* *|", "-----"],
            6: ["-----", "|* *|", "|* *|", "|* *|", "-----"]
        }

    def print_dice(self, results: list):
        dice_rows = ["", "", "", "", ""]

        for result in results:
            face = self.dice_faces[result]
            for i in range(5):  # Each die has 5 rows
                dice_rows[i] += face[i] + "  "  # Spacing between dice

        for row in dice_rows:
            print(row)