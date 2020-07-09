from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Add items
room['foyer'].items = [
    Item("Torch", "A burning torch made of wood and cloth."),
    Item("Rock", "Just a rock.")
]

#
# Main
#


# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
playing = True

while playing:
    print(player.current_room)

    command = input("What would you like to do? ").lower().split(" ")

    # if single word command is entered
    if len(command) == 1:
        command = command[0]
        if command == "n" or command == "s" or command == "e" or command == "w":
            player.move(command)
        elif command == "i" or command == "inventory":
            player.print_inventory()
        elif command == "q":
            print("\nThanks for playing!\n")
            playing = False
        else:
            print("\nInvalid command")
    # if multi word command is entered
    elif len(command) == 2:
        # if command keyword is a take or drop input
        if command[0] == "get" or command[0] == "take" or command[0] == "drop":
            input_item = command[1].capitalize()
            if command[0] == "drop":
                player.drop_item(input_item)
            # if command keyword is take input
            else:
                player.take_item(input_item)
        else:
            print("\nInvalid command")
    else:
        print("\nInvalid command")
