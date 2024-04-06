# For Game stuff.

import random

# import player
from enemy import Enemy
from player import Player

# Add the other python files


character_type = Player.choose_character()
player = Player(character_type)
instance_enemy = Enemy()
# random_enemy = instance_enemy.pick_enemy()
# #
# print(random_enemy.health)

class Game:
    def __init__(self):
        self.fight_round = 1
        self.end_round = False
        self.enemy_alive = True
        self.player_alive = True
        self.player_in_dungeon = False
        self.dungeon_floors = 0
        self.current_floor = 0
        self.exploring_mode = True
        self.dungeon_completed = False
        # self.enemy_instance = Enemy()
        # self.random_enemy = self.enemy_instance.pick_enemy()
        # print(self.random_enemy)

    def reset_round(self):
        # Should reset the round and enemy.
        #instance_enemy.pick_enemy()
        self.enemy_alive = True
        self.fight_start()

    def start_dungeon(self):
        # Should start the dungeon.
        self.player_in_dungeon = True
        self.exploring_mode = False
        self.dungeon_completed = False
        self.dungeon_floors = random.randint(3, 6)
        print("You have entered a dungeon!")
        while self.player_in_dungeon:
            print("Starting Dungeon.")
            print(f"This Dungeon has {self.dungeon_floors} floors.")

            while self.current_floor != self.dungeon_floors:
                self.fight_start()
                self.current_floor += 1
                print(f"Inside while check for the dungeon. Currently on floor {self.current_floor}")

            if self.current_floor == self.dungeon_floors:
                self.dungeon_completed = True
                print("You have cleared the Dungeon!")
                break

    def fight_start(self):
        # Initialize the enemy.
        instance_enemy.pick_enemy()
        enemy_name = instance_enemy.get_enemy_name()
        enemy_health = instance_enemy.get_enemy_health()
        enemy_basedamage = instance_enemy.get_enemy_basedamage()
        enemy_tier = instance_enemy.get_enemy_tier()
        enemy_max_hp = instance_enemy.get_enemy_max_hp()

        while not self.end_round:
            while enemy_health > 0 and player.current_health > 0:
                action = input("What will you do? (attack/stats/kill/quit) ").lower()

                if action == "attack":
                    player_damage = player.attack()
                    if enemy_health > 0:
                        # Random enemy takes damage based on (player_damage)
                        instance_enemy.take_damage(player_damage)
                        if enemy_health > 0:
                            enemy_damage = instance_enemy.attack()
                            player.take_damage(enemy_damage)

                    if enemy_health == 0:
                        self.end_round = True

                elif action == "deck":
                    player.randomise_cards()

                elif action == "cards":
                    player.play_card()

                elif action == "stats":
                    print(f"{player.name} the Level {player.level} {player.ctype} ")
                    print(f"Current Health: {player.current_health}/{player.max_hp}")
                    print(f"Strength: {player.strength}")
                    print(f"Damage: {player.base_damage}")
                    print(f"Defence: {player.defence}")
                    print(f"Intelligence: {player.intelligence}")
                    print(f"Dexterity: {player.dexterity}")
                    print(f"Critical Strike Chance: {player.crit_chance}")
                    print(f"Vitality: {player.vitality}")
                    print(f"Experience: {player.xp}/{player.required_xp}")

                elif action == "kill":
                    print("You cheater.")
                    break

                elif action == "quit":
                    exit()

                elif action == "floor":
                    print(f"You are on floor {self.current_floor}/{self.dungeon_floors}")

                else:
                    print("Invalid action. Please choose 'attack', 'stats' or 'flee'.")

            if player.current_health > 0 and not self.end_round:
                print("You defeated all enemies. You are victorious!")
                self.enemy_alive = False
                xp_gain = random.randint(1, 10)
                player.xp += xp_gain
                print(f"You have gained xp: {xp_gain}")
                # player.level_up()

                if player.level_up():
                    print("Choose a stat to increase: (strength, defence, intelligence, vitality, dexterity)")
                    stat_has_been_chosen = False
                    while not stat_has_been_chosen:
                        chosen_stat = input().strip().lower()
                        if chosen_stat in ["strength", "defence", "intelligence", "vitality", "dexterity"]:
                            # Below references the chosen_stat and passes this to the increase_stat variable in Player
                            player.increase_stat(chosen_stat)
                            stat_has_been_chosen = True
                        else:
                            print("Invalid stat. Please choose a valid stat.")

                self.fight_round += 1
                break




    def start_shop(self):
        print("The shopkeeper tells you to go away as it's not ready yet.")

    def exploring(self):
        while self.exploring_mode:
            action = input("What will you do? (dungeon/shop) ").lower()

            if action == "dungeon":
                self.start_dungeon()
                #self.fight_start()

            if action == "shop":
                self.start_shop()

            else:
                print("Invalid action.")