import random
import json


# Class
class Player:
    def __init__(self, character_type):
        self.character_type = character_type
        self.load_attributes()

    def load_attributes(self):
        with open('data/classes.json') as f:
            data = json.load(f)
        if self.character_type in data:
            attributes = data[self.character_type]
            self.max_hp = attributes["Health"]
            self.name = "Hero"
            self.level = 1
            self.ctype = self.character_type
            self.current_health = attributes["Health"]
            self.base_damage = attributes["BaseDamage"]
            self.strength = attributes["Strength"]
            self.dexterity = attributes["Dexterity"]
            self.intelligence = attributes["Intelligence"]
            self.defence = attributes["Defence"]
            self.crit_chance = attributes["Critical"]
            self.vitality = attributes["Vitality"]
            self.xp = 0

        else:
            raise ValueError(f"Character type '{self.character_type}' not found in JSON.")

    def choose_character():
        while True:
            choice = input("Choose your character type (Warrior/Mage): ").strip().capitalize()
            if choice in ["Warrior", "Mage"]:
                return choice
            else:
                print("Invalid choice. Please choose either 'Warrior' or 'Mage'.")

    def attack(self):
        attack_damage = self.base_damage
        crit_roll = random.randint(1, 10)  # Generate a random number between 1 and 10
        if crit_roll <= self.crit_chance:  # If the roll is less than or equal to the crit chance
            crit_attack = attack_damage * 2  # Double the damage
            print("Critical hit!")
            return crit_attack
        else:
            print(f"You attack and deal {attack_damage} damage!")
            return attack_damage

    def take_damage(self, damage):
        self.current_health -= damage
        if self.current_health <= 0:
            print("You have been defeated. Game Over!")
        else:
            print(f"You take {damage} damage! Your remaining hp: {self.current_health} / {self.max_hp}")

    def xp_calculations(self, required_xp):
        self.required_xp = 10 * 1.5 * self.level
        return required_xp

    def level_up(self):
        if self.xp >= self.required_xp:
            print(f"Congratulations! You have reached Level {self.level + 1}.")
            self.xp_calculations()
            self.level += 1
            self.xp = 0
            return True, self.required_xp
        else:
            print(f"Required XP till next level: {self.required_xp}")
            return False
    def increase_stat(self, stat):
        if self.level_up():
            if hasattr(self, stat):
                setattr(self, stat, getattr(self, stat) + 1)
                if stat == 'strength':
                    self.base_damage += 1
                if stat == 'vitality':
                    self.max_hp += 1
                    print(f"You now have a max health pool of {self.max_hp}")
                print(f"{stat.capitalize()} has been increased by 1.")
                print(f"Your HP has been fully healed!")
                self.current_health = self.max_hp
                return self
        else:
            print(f"Invalid stat: {stat}. Please choose a valid stat.")
            return self
