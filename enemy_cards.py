# Rewrite the below to suit enemy needs.

# Accessing starting cards under the "Warrior" part
warrior_starting_cards = data["Warrior"]["StartingCards"]

# Define the probability of selecting common and uncommon cards
probability_common = 0.7  # Adjust as needed
probability_uncommon = 1 - probability_common

# Randomly select a rarity based on probability
rarity = random.choices(["Common", "Uncommon"], weights=[probability_common, probability_uncommon])[0]

# Randomly select a card from the chosen rarity
selected_card_name = random.choice([card_name for card_name, card_data in warrior_starting_cards.items() if card_data["Rarity"] == rarity])

selected_card = warrior_starting_cards[selected_card_name]