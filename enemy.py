# Enemy Stuff
import json
import random


with open('data/enemies.json') as enemyjson:
    enemy_data = json.load(enemyjson)



class Enemy:
    # def __init__(self):

    def pick_enemy(self):
        # Actual command to randomise enemy
        #self.enemy_name = random.choice(list(enemy_data.keys()))

        # For testing Spider
        self.enemy_name = enemy_data["Spider"]["Name"]

        # Get the attributes of the randomly selected enemy
        self.enemy_health = enemy_data[self.enemy_name]["Health"]
        self.enemy_basedamage = enemy_data[self.enemy_name]["BaseDamage"]
        self.enemy_tier = enemy_data[self.enemy_name]["Tier"]

        # Create an instance of the Enemy class with the randomly selected attributes
        self.random_enemy = [self.enemy_name, self.enemy_health, self.enemy_basedamage, self.enemy_tier]
        return self.random_enemy

    def enemy_attack(self):
        starting_hand = enemy_data[self.enemy_name]["Cards"]
        choose_random_card1 = random.choice(list(starting_hand.keys()))
        #selected_card1 = starting_hand[choose_random_card1]

        # # Define the probability of selecting common and uncommon cards
        probability_common = 0.7  # Adjust as needed
        probability_uncommon = 1 - probability_common
        probability_rare = 1 - probability_common

        # # Randomly select a rarity based on probability
        # rarity = random.choices(["Common", "Uncommon", "Rare"], weights=[probability_common, probability_uncommon, probability_rare])[0]
        # print(rarity)
        # # Randomly select a card from the chosen rarity
        # selected_card_name = random.choice(
        #     [card_name for card_name, card_data in starting_hand.items() if card_data["Rarity"] == rarity])
        #
        # print(selected_card_name)

        while True:
            # Randomly select a rarity based on probability
            rarity = random.choices(["Common", "Uncommon", "Rare"],
                                    weights=[probability_common, probability_uncommon, probability_rare])[0]
            print("Attempting to select a card with rarity:", rarity)

            # Check if there are cards with the selected rarity
            available_cards = [card_name for card_name, card_data in starting_hand.items() if
                               card_data["Rarity"] == rarity]
            if available_cards:
                # Randomly select a card from the chosen rarity
                selected_card_type = random.choice(available_cards)
                print("Selected card:", selected_card_type)
                break  # Break the loop as a valid card has been selected
            else:
                print("No cards with rarity", rarity, "found in starting hand. Trying again.")

        selected_card = enemy_data[self.enemy_name]["Cards"][selected_card_type]
        # Card 1 details
        self.random_card_name = selected_card["Name"]
        self.random_card_damage = selected_card["Damage"]
        self.random_card_type = selected_card["Type"]
        self.random_card_rarity = selected_card["Rarity"]
        self.random_card_chance = selected_card["Chance"]

        self.card = [self.random_card_name, self.random_card_damage, self.random_card_type, self.random_card_rarity, self.random_card_chance]

        # Print info
        #rint(f"{self.random_card_name}")

        return self.card

if __name__ == '__main__':
    # Create an instance of the Enemy class
    enemy_instance = Enemy()

    # Call the pick_enemy method on the instance
    random_enemy = enemy_instance.pick_enemy()
    # print(random_enemy)

    random_enemy_card = enemy_instance.enemy_attack()
    print(f"{random_enemy_card}")