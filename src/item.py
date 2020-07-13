class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}"

    def on_take(self, player):
        print(f"\nYou have picked up {self.name}.\n")

    def on_drop(self, player):
        print(f"\nYou have dropped {self.name}.\n")


class Weapon(Item):
    def __init__(self, name, description, attack_strength):
        super().__init__(name, description)
        self.attack_strength = attack_strength

    def on_take(self, player):
        player.attack_strength += self.attack_strength
        print(
            f"\nYou have picked up {self.name}.\nYour attack strength is now {player.attack_strength}.\n")

    def on_drop(self, player):
        player.attack_strength -= self.attack_strength
        print(
            f"\nYou have dropped {self.name}.\nYour attack strength is now {player.attack_strength}.\n")
