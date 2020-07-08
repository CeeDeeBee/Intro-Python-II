# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = self.s_to = self.e_to = self.w_to = None
        self.items = []

    def __str__(self):
        items = ""
        if not bool(len(self.items)):
            items = "None"
        else:
            for item in self.items:
                items += f"{item.name}, "
            # remove last comma and space
            items = items[:-2]

        return f"\n{self.name}\n{self.description}\nItems: {items}\n"
