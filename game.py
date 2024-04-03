# For Game stuff.

import json
import random

from player import Player
from player_cards import Player_Cards

# Add the other python files



#

class Game:
    def __init__(self):
        self.fight_round = 1
        self.end_round = False
        self.enemy_alive = True
        self.player_alive = True
        self.player_in_dungeon = False
        self.dungeon_floors = 0


    def reset_round(self):
        # Should reset the round and enemy.

    def start_dungeon(self):
        # Should start the dungeon.
        self.player_in_dungeon = True
        self.dungeon_floors = random.randint(3, 6)
        print("You have entered a dungeon!")
        while self.player_in_dungeon:
            print("Starting Dungeon.")
            print(f"This Dungeon has {self.dungeon_floors} floors.")
            return



    def fight_start(self):
        while not self.end_round:


    def start_shop(self):
        print("The shopkeeper tells you to go away as it's not ready yet.")

    def exploring(self):
        while self.exploring_mode:
            action = input("What will you do? (dungeon/shop) ").lower()

            if action == "dungeon":
                self.start_dungeon()

            if action == "shop":
                self.start_shop()

            else:
                print("Invalid action.")