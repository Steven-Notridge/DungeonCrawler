# Handle Player cards
import json
import random

with open('data/classes.json') as classes:
    starting_hand = json.load(classes)

# Debugging to make sure it allows a variable in the list for the cards
# choice = input("Choose Warrior: ").strip().capitalize()
# warrior_starting_cards = starting_hand[choice]["StartingCards"]

player_starting_cards = starting_hand["Warrior"]["StartingCards"]

# Randomly select one starting card
#random_card = random.choice(list(player_starting_cards.keys()))

#selected_card = player_starting_cards[random_card]

class Player_Cards:
    #def __init__(self):


    def randomise_cards(self):
        # Choose the initial cards, pre-reroll
        choose_random_card1 = random.choice(list(player_starting_cards.keys()))
        selected_card1 = player_starting_cards[choose_random_card1]
        choose_random_card2 = random.choice(list(player_starting_cards.keys()))
        selected_card2 = player_starting_cards[choose_random_card2]
        choose_random_card3 = random.choice(list(player_starting_cards.keys()))
        selected_card3 = player_starting_cards[choose_random_card3]

        # Card 1 details
        self.random_card1_name = choose_random_card1
        self.random_card1_damage = selected_card1["Damage"]
        self.random_card1_type = selected_card1["Type"]
        self.random_card1_rarity = selected_card1["Rarity"]

        # Card 2 details
        self.random_card2_name = choose_random_card2
        self.random_card2_damage = selected_card2["Damage"]
        self.random_card2_type = selected_card2["Type"]
        self.random_card2_rarity = selected_card2["Rarity"]

        # Card 3 details
        self.random_card3_name = choose_random_card3
        self.random_card3_damage = selected_card3["Damage"]
        self.random_card3_type = selected_card3["Type"]
        self.random_card3_rarity = selected_card3["Rarity"]


        # Create list for each card, with their information.
        card1 = [self.random_card1_name, self.random_card1_damage, self.random_card1_type, self.random_card1_rarity]
        card2 = [self.random_card2_name, self.random_card2_damage, self.random_card2_type, self.random_card2_rarity]
        card3 = [self.random_card3_name, self.random_card3_damage, self.random_card3_type, self.random_card3_rarity]


        # Show initial cards.
        print(f"{self.random_card1_name}")
        print(f"{self.random_card2_name}")
        print(f"{self.random_card3_name}")

        # Reroll card 2 if its the same as card 1
        if choose_random_card2 == choose_random_card1:
            print("Picked the same cards for 1 and 2, rerolling.")
            while choose_random_card2 == choose_random_card1:
                choose_random_card2 = random.choice(list(player_starting_cards.keys()))
                selected_card2 = player_starting_cards[choose_random_card2]
                self.random_card2_name = choose_random_card2
                self.random_card2_damage = selected_card2["Damage"]
                self.random_card2_type = selected_card2["Type"]
                self.random_card2_rarity = selected_card2["Rarity"]
                print(f"{self.random_card2_name}")

                if choose_random_card2 != choose_random_card1:
                    return True

        # Reroll card 3 if its the same as card 1
        if choose_random_card3 == choose_random_card1:
            print("Picked the same cards for 3 and 1")
            if choose_random_card3 == choose_random_card1:
                print("Picked the same cards for 3 and 1, rerolling.")
                while choose_random_card3 == choose_random_card1:
                    choose_random_card3 = random.choice(list(player_starting_cards.keys()))
                    selected_card3 = player_starting_cards[choose_random_card3]
                    self.random_card3_name = choose_random_card3
                    self.random_card3_damage = selected_card3["Damage"]
                    self.random_card3_type = selected_card3["Type"]
                    self.random_card3_rarity = selected_card3["Rarity"]
                    print(f"{self.random_card3_name}")
                    if choose_random_card3 != choose_random_card1:
                        return True

        # Check if Card 3 is the same as 2. This needs to happen in this order as 2 will be chosen before 3 and prevent an additional if statement.
        if choose_random_card3 == choose_random_card2:
            if choose_random_card3 == choose_random_card2:
                print("Picked the same cards for 3 and 2, rerolling.")
                while choose_random_card3 == choose_random_card2:
                    choose_random_card3 = random.choice(list(player_starting_cards.keys()))
                    selected_card3 = player_starting_cards[choose_random_card3]
                    self.random_card3_name = choose_random_card3
                    self.random_card3_damage = selected_card3["Damage"]
                    self.random_card3_type = selected_card3["Type"]
                    self.random_card3_rarity = selected_card3["Rarity"]
                    print(f"{self.random_card3_name}")

                    if choose_random_card3 != choose_random_card2:
                        return True

        return card1, card2, card3

#if __name__ == '__main__':
    #Player_Cards.randomise_cards()
    #print(f"{starting_hand}")
    #print(warrior_starting_cards)
    # print("Selected card:", random_card)
    # print(selected_card)
