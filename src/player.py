# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, current_room):
        self.name = "Steve"
        self.current_room = current_room

    def move(self, dir):
        if bool(getattr(self.current_room, f"{dir}_to")):
            self.current_room = getattr(self.current_room, f"{dir}_to")
        else:
            print("\nThere isn't anything in that direction.")
