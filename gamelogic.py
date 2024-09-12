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



class Player():
    def __init__(self, name: str) -> None:
        self.name = name
        self.all_dice = [0] * 6
        self.saved_dice = []
        self.score = 0

    def __repr__(self) -> str:
        return self.name

    def play_turn(self, dice, screenclear):
        # Reset saved dice for this turn
        self.saved_dice = []

        rolled_dice = []

        # Three dice throws per turn (including final result)
        for turn in range(2):
            screenclear()

            print(f"{self.name}, turn {turn + 1}")

            # Show saved dice if any
            if self.saved_dice:
                print("Saved dice:", self.saved_dice)

            # Roll unsaved dice
            remaining_dice = 6 - len(self.saved_dice)
            rolled_dice = self.roll_dice(remaining_dice)

            # Display both saved and newly rolled dice
            dice.print_dice(self.saved_dice + rolled_dice)

            # Ask player which dice to save
            dice_to_save = input("Select which dice to save (eg. '1,2,3'):\n")

            if dice_to_save:
                dice_to_save = dice_to_save.split(",")

                # Update saved_dice based on player's input
                new_saved_dice = []
                for n in dice_to_save:
                    new_saved_dice.append(rolled_dice[int(n) - 1])

                self.saved_dice.extend(new_saved_dice)

        # After three turns, the final dice are the saved dice plus any unsaved dice from the last roll
        self.all_dice = self.saved_dice + rolled_dice[:6 - len(self.saved_dice)]

        screenclear()

        print(f"Final dice for {self.name}:")
        dice.print_dice(self.all_dice)
        input()

    def roll_dice(self, amount_of_dice: int = 6) -> list:
        return [random.randint(1, 6) for _ in range(amount_of_dice)]

    def save_dice(self, values: list):
        self.saved_dice = values[:]

    def get_saved_dice(self) -> list:
        return self.saved_dice if self.saved_dice else None


    
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
        dice_rows = ["", "", "", "", "", ""]

        for result in results:
            face = self.dice_faces[result]
            for i in range(5):  # Each die has 5 rows
                dice_rows[i] += face[i] + "  "  # Spacing between dice

        for row in dice_rows:
            print(row)