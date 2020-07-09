class Monster:
    def __init__(self, name, health, attack_strength):
        self.name = name
        self.health = health
        self.attack_strength = attack_strength

    def __str__(self):
        if self.health > 0:
            return f"\nThere is a(n) {self.name} in the room! It looks to attack!\n"
        else:
            return f"\nThere is a(n) {self.name} in the room but it has been killed.\n"

    def on_attacked(self):
        if self.health > 0:
            print(
                f"\nYou attack the {self.name}! It now has {self.health} health.\n")
        else:
            print(f"\nYou have killed the {self.name}!\n")

    def attack(self, player):
        player.health -= self.attack_strength
        player.on_attacked(self)
