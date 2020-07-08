# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, current_room):
        self.name = "Steve"
        self.current_room = current_room
        self.items = []

    def move(self, dir):
        if bool(getattr(self.current_room, f"{dir}_to")):
            self.current_room = getattr(self.current_room, f"{dir}_to")
        else:
            print("\nThere isn't anything in that direction.")

    def print_inventory(self):
        if len(self.items) == 0:
            print("\nThere's nothing in your inventory.")
        else:
            inventory_str = "\n"
            for item in self.items:
                inventory_str += f"{item.name}: {item.description}\n"
            print(inventory_str)

    def add_item(self, item):
        self.items.append(item)
        item.on_take()

    def drop_item(self, index):
        return self.items.pop(index)
