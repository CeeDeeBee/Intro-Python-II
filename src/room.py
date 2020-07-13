# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = self.s_to = self.e_to = self.w_to = None
        self.items = []
        self.monsters = []

    def __str__(self):
        text = f"\n{self.name}\n{self.description}\n"
        if len(self.monsters) > 0:
            for monster in self.monsters:
                text += str(monster)
        return text

    def print_items(self):
        items = "\n"
        if not bool(len(self.items)):
            items += "There are no items in this room.\n"
        else:
            for item in self.items:
                items += f"{str(item)}\n"

        print(items)

    def monsters_attack(self, player):
        for monster in self.monsters:
            if monster.health > 0:
                monster.attack(player)
