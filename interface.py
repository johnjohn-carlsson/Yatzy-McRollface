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

        # ----------------------------------------------------
        # -------------- RUN MAIN PART OF GAME ---------------
        # ----------------------------------------------------

        self.run_main_game()

    def run_main_game(self):

        while True:
            self.play_turn()

    def play_turn(self):

        for player in self.logic.get_players():

            self.screenclear()
            player.play_turn(self.dice, self.screenclear)

            