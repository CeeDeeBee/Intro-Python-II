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
            # remove last \n on print
            print(inventory_str[:-1])

    def take_item(self, item_name):
        # list of names of items in room
        room_item_names = [
            item.name for item in self.current_room.items]
        # check if specified item is in the room
        if item_name in room_item_names:
            # remove item from room and put in inventory
            item_index = room_item_names.index(item_name)
            item = self.current_room.items.pop(item_index)
            self.items.append(item)
            item.on_take()
        else:
            print(
                f"\nThere is no item named {item} in this room.")

    def drop_item(self, item_name):
        # list of names of items in inventory
        player_item_names = [item.name for item in self.items]
        # check if the specified item is in the inventory
        if item_name in player_item_names:
            # remove item from inventory and put in room
            item_index = player_item_names.index(item_name)
            item = self.items.pop(item_index)
            self.current_room.items.append(item)
            item.on_drop()
        else:
            print(
                f"\nYou are not holding an item named {item}.")
