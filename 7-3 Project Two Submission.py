# TextBasedGame.py
# Full Name: NaTasha Hearn

# Function to display game instructions to the player
def show_instructions():
    print("Dragon Text Adventure Game")
    print("Collect 6 items to win the game, or be eaten by the dragon.")
    print("Move commands: go South, go North, go East, go West")
    print("Add to Inventory: get 'item name'")
    print("Type 'exit' to quit the game at any time.")
    print("---------------------------")

# Function to display the player's current status
def show_status(current_room, inventory, rooms):
    print(f"You are in the {current_room}")
    print(f"Inventory: {inventory}")
    if 'item' in rooms[current_room]:
        print(f"You see a {rooms[current_room]['item']}")

    # Show available directions
    directions = [key for key in rooms[current_room] if key != 'item']
    if directions:
        print(f"You can go: {', '.join(directions)}")
    print("---------------------------")


# Main function containing the game loop
def main():
    # Dictionary of rooms and their linked directions/items
    rooms = {
        'Great Hall': {'South': 'Bedroom', 'North': 'Dungeon', 'East': 'Kitchen', 'West': 'Library'},
        'Bedroom': {'North': 'Great Hall', 'East': 'Cellar', 'item': 'Armor'},
        'Cellar': {'West': 'Bedroom', 'item': 'Helmet'},
        'Kitchen': {'West': 'Great Hall', 'South': 'Gallery', 'item': 'Shield'},
        'Gallery': {'North': 'Kitchen', 'item': 'Sword'},
        'Library': {'East': 'Great Hall', 'North': 'Study', 'item': 'Potion'},
        'Study': {'South': 'Library', 'item': 'Lantern'},
        'Dungeon': {'South': 'Great Hall', 'item': 'Dragon'}  # Villain room
    }

    # Initialize game state
    current_room = 'Great Hall'
    inventory = []
    required_items = 6

    show_instructions()

    # Gameplay loop
    while True:
        show_status(current_room, inventory, rooms)
        command = input("Enter your move: ").strip()

        if command.lower().startswith('go '):
            direction = command[3:].capitalize()
            # Check if the direction exists in the current room
            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
                print(f"You move to the {current_room}.")
            else:
                print("You can't go that way!")

        elif command.lower().startswith('get '):
            item_requested = command[4:].capitalize()
            room_item = rooms[current_room].get('item', '').capitalize()
            if item_requested == room_item:
                if item_requested in inventory:
                    print("You already picked up that item.")
                else:
                    inventory.append(item_requested)
                    print(f"{item_requested} picked up!")
                    del rooms[current_room]['item']  # Remove the item from the room
            else:
                print("Can't get that item here.")

        elif command.lower() == 'exit':
            print("You have exited the game. Thanks for playing!")
            break  # Exit the game loop

        else:
            print("Invalid command. Please use 'go [direction]' or 'get [item]'.")

        # Win condition
        if current_room == 'Dungeon':
            if len(inventory) == required_items:
                print("Congratulations! You have collected all items and defeated the dragon!")
            else:
                print("NOM NOM...GAME OVER! The dragon has eaten you.")
            print("Thanks for playing the game. Hope you enjoyed it.")
            break


# Entry point of the script
if __name__ == "__main__":
    main()
