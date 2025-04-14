# ModuleSixMilestone.py
# Author: NaTasha Hearn
# Simplified Dragon Text Game (Based on Flowchart)

# Dictionary linking rooms and directions
rooms = {
    'Great Hall': {'South': 'Bedroom'},
    'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
    'Cellar': {'West': 'Bedroom'}
}

# Step 1: Place Player in Start Room
current_room = 'Great Hall'

# Step 2: Show Game Instructions (once)
print("Welcome to the Simplified Dragon Text Game!")
print("Move between rooms by typing a direction (North, South, East, West).")
print("Type 'exit' to quit the game.\n")

# Step 3: Main Game Loop
while True:
    # Step 4: Is current room 'exit'? If yes, end game
    if current_room == 'exit':
        print("You have exited the game. Thanks for playing!")
        break

    # Step 5: Show Player's Status
    print(f"\nYou are currently in the {current_room}.")
    print("Available directions:", ', '.join(rooms[current_room].keys()))

    # Step 6: Get Command From Player
    command = input("Enter a direction or 'exit' to quit: ").capitalize()

    # Step 7: What is the command?
    if command == 'Exit':
        # Set room to 'exit' and loop will break in the next iteration
        current_room = 'exit'
    elif command in rooms[current_room]:
        # Valid direction: move player
        new_room = rooms[current_room][command]
        print(f"You move {command} to the {new_room}.")
        current_room = new_room
    else:
        # Invalid command
        print("Invalid command. Please enter a valid direction or type 'exit' to quit.")
