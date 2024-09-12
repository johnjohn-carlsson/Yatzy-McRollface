from gamelogic import *
import os

class UserInterface():
    def __init__(self) -> None:
        
        # Initialize classes
        self.logic = YatzyPlayer()
        self.dice = DiceDrawer()

    def screenclear(self):
        os.system('cls')

    def launch(self):
        self.setup_players()
        self.run_main_game()
        self.end_game()

    def setup_players(self):
        # ----------------------------------------------------
        # ------------ SET UP PLAYERS BEFORE GAME ------------
        # ----------------------------------------------------

        self.screenclear()
        print("Welcome to Yatzy McRollface!")
        print("Please enter amount of players:")
        amount_of_players = int(input())

        list_of_new_players = []
        
        # Create and store players with their names
        for n in range(amount_of_players):
            name = input(f"Enter name for player {n+1}:\n")

            new_player = Player(name)
            list_of_new_players.append(new_player)

        self.logic.set_players(list_of_new_players)

    def run_main_game(self):
        # ----------------------------------------------------
        # -------------- RUN MAIN PART OF GAME ---------------
        # ----------------------------------------------------

        for _ in range(13):
            self.play_turn()

    def play_turn(self):

        for player in self.logic.get_players():

            self.screenclear()
            player.play_turn(self.dice, self.screenclear)

    def end_game(self):
        # ----------------------------------------------------
        # -------------- CALCULATE FINAL SCORES --------------
        # ----------------------------------------------------

        self.logic.final_score_calculator()

            