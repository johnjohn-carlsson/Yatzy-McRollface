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
        self.print_logo()
        amount_of_players = int(input(
            "                      PLEASE ENTER AMOUNT OF PLAYERS: "
            ))

        list_of_new_players = []
        
        self.screenclear()

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

        for _ in range(15):
            self.play_turn()

    def play_turn(self):

        for player in self.logic.get_players():

            self.screenclear()
            player.play_turn(self.dice, self.screenclear)

    def end_game(self):
        # ----------------------------------------------------
        # -------------- CALCULATE FINAL SCORES --------------
        # ----------------------------------------------------

        final_scores = self.logic.final_score_calculator()
        sorted_scores = sorted(final_scores.items(), key=lambda item: item[1], reverse=True)

        self.screenclear()
        print("FINAL RESULTS:\n")

        for key, value in sorted_scores:
            print(f"{key} - {value} pts")

        input("\nThanks for playing Yatzy McRollface!")

    
    def print_logo(self):
        print("                                WELCOME TO                                  ")
        print("                                                                            ")
        print(" __     __   _               __  __      _____       _ _  __                ")
        print(" \ \   / /  | |             |  \/  |    |  __ \     | | |/ _|               ")
        print("  \ \_/ /_ _| |_ _____   _  | \  / | ___| |__) |___ | | | |_ __ _  ___ ___  ")
        print("   \   / _` | __|_  / | | | | |\/| |/ __|  _  // _ \| | |  _/ _` |/ __/ _ \ ")
        print("    | | (_| | |_ / /| |_| | | |  | | (__| | \ \ (_) | | | || (_| | (_|  __/ ")
        print("    |_|\__,_|\__/___|\__, | |_|  |_|\___|_|  \_\___/|_|_|_| \__,_|\___\___| ")
        print("                      __/ |                                                 ")
        print("                     |___/                                                  ")
        print("                                                                            ")
