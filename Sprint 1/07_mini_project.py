# ========================================================
# Python Journey: Module 1 - Mini Project
# ========================================================
# This file contains a mini-project that combines all the
# concepts you've learned in the first module.
# ========================================================

print("=" * 50)
print("Python Journey: Module 1 - Mini Project")
print("=" * 50)

# ------------------------------------------------------
# ADVENTURE GAME: THE PYTHON'S QUEST
# ------------------------------------------------------
# This is a simple text-based adventure game that uses conditionals,
# loops, functions, lists, and user input. It's designed to practice
# all the concepts you've learned in Module 1.
# ------------------------------------------------------

print("\nWelcome to THE PYTHON'S QUEST")
print("An adventure game to test your Python knowledge!")

# Global variables
inventory = []
player_health = 100
visited_locations = []
current_location = "start"

# Game functions
def display_intro():
    """Display the game introduction and instructions."""
    print("\n" + "=" * 50)
    print("THE PYTHON'S QUEST - INTRODUCTION")
    print("=" * 50)
    print("""
You are an intrepid Python programmer on a quest to find the legendary 
Gem of Code, which is said to grant its owner the power of perfect 
programming. Your journey will take you through various challenges 
that will test both your wits and your newfound Python knowledge.

Instructions:
- Read the description of each location carefully
- Type your choices exactly as shown in the brackets [like this]
- Collect items to help you on your journey
- Use your Python knowledge to solve puzzles
- Try to reach the Gem of Code with full health

Good luck, adventurer! Your Python journey begins now...
    """)
    input("Press Enter to start your adventure...")

def display_status():
    """Display the player's current status."""
    print("\n" + "-" * 30)
    print(f"Health: {player_health}%")
    print(f"Inventory: {', '.join(inventory) if inventory else 'Empty'}")
    print("-" * 30)

def visit_location(location):
    """
    Handle visiting a location in the game.
    
    Args:
        location (str): The location ID to visit
        
    Returns:
        str: The next location ID
    """
    global player_health, inventory, visited_locations
    
    # Add to visited locations
    if location not in visited_locations:
        visited_locations.append(location)
    
    # Handle each location
    if location == "start":
        return start_location()
    elif location == "forest":
        return forest_location()
    elif location == "cave":
        return cave_location()
    elif location == "river":
        return river_location()
    elif location == "puzzle_room":
        return puzzle_room()
    elif location == "final_chamber":
        return final_chamber()
    elif location == "end_win":
        return end_win()
    elif location == "end_lose":
        return end_lose()
    else:
        print("Error: Location not found!")
        return "start"

def start_location():
    """Handle the starting location."""
    print("\n" + "=" * 50)
    print("THE CROSSROADS")
    print("=" * 50)
    print("""
You stand at a crossroads, with three paths ahead of you:
- A winding path through a dark [forest]
- A narrow trail leading to a mysterious [cave]
- A rocky path alongside a rushing [river]

Which path will you choose?
    """)
    
    while True:
        choice = input("> ").lower().strip()
        if choice == "forest":
            return "forest"
        elif choice == "cave":
            return "cave"
        elif choice == "river":
            return "river"
        else:
            print("I don't understand that choice. Try forest, cave, or river.")

def forest_location():
    """Handle the forest location."""
    global player_health, inventory
    
    print("\n" + "=" * 50)
    print("THE DARK FOREST")
    print("=" * 50)
    print("""
You enter a dense forest where the trees are so tall they block out most
of the sunlight. As you walk deeper into the woods, you spot something
glinting on the ground.

It's a [map]! This could be useful for your journey.

As you reach down to pick it up, you hear a rustling in the bushes.
A wild Python appears! It's not aggressive, but it seems to be
guarding something.

What will you do?
- Try to [take] the map quickly and run
- Try to [befriend] the Python
- Explore the [clearing] nearby
- Follow the [path] deeper into the forest
    """)
    
    while True:
        choice = input("> ").lower().strip()
        if choice == "take":
            print("\nYou quickly grab the map, but the Python feels threatened!")
            print("It hisses and nips at your hand as you escape.")
            print("You lose 20 health but gain a map.")
            player_health -= 20
            inventory.append("map")
            print("\nThe forest path continues and eventually leads to a puzzle room.")
            return "puzzle_room"
            
        elif choice == "befriend":
            print("\nYou slowly approach the Python, showing that you mean no harm.")
            print("You remember from your coding studies that Pythons are actually quite friendly!")
            print("The Python relaxes and slithers aside, revealing both the map and a small healing potion.")
            print("You gain a map and a potion!")
            inventory.append("map")
            inventory.append("potion")
            print("\nThe forest path continues and eventually leads to a puzzle room.")
            return "puzzle_room"
        
        elif choice == "clearing":
            print("\nYou explore the clearing and find a hidden stash of supplies!")
            print("You gain a shield and some food.")
            inventory.append("shield")
            inventory.append("food")
            print("\nThe forest path continues and eventually leads to a cave.")
            return "cave"
        
        elif choice == "path":
            print("\nYou follow the path deeper into the forest and encounter a wise old sage.")
            print("The sage offers you a riddle. Solve it to gain a special item.")
            print("Riddle: What has keys but can't open locks?")
            riddle_answer = input("> ").lower().strip()
            if riddle_answer == "piano":
                print("\nCorrect! The sage gives you a magic amulet.")
                inventory.append("amulet")
            else:
                print("\nIncorrect. The sage disappears.")
            print("\nThe forest path continues and eventually leads to a river.")
            return "river"
            
        else:
            print("I don't understand that choice. Try take, befriend, clearing, or path.")

def cave_location():
    """Handle the cave location."""
    global player_health, inventory
    
    print("\n" + "=" * 50)
    print("THE MYSTERIOUS CAVE")
    print("=" * 50)
    print("""
You enter a dark cave, with only a dim light from the entrance illuminating
your way. As your eyes adjust, you notice strange symbols carved into the
walls that look suspiciously like Python syntax.

One wall has a simple riddle engraved:
"I am the container that holds your treasures, 
 Values stored by index and accessed by your pleasure.
 What am I in Python?"

What data structure is it referring to?
- Is it a [list]?
- Is it a [dictionary]?
- Is it a [tuple]?
    """)
    
    while True:
        choice = input("> ").lower().strip()
        if choice == "list":
            print("\nThe wall glows with approval! A small alcove opens, revealing a lantern.")
            print("You now have a light source that will help you see in dark places.")
            print("You gain a lantern!")
            inventory.append("lantern")
            print("\nThe cave passage continues deeper and eventually leads to a puzzle room.")
            return "puzzle_room"
            
        elif choice in ["dictionary", "tuple"]:
            print("\nThe wall remains still. The ground trembles slightly, and some rocks fall from the ceiling.")
            print("One hits your shoulder. You lose 15 health.")
            player_health -= 15
            print("You reconsider your answer...")
            
        else:
            print("That's not one of the options. Try list, dictionary, or tuple.")

def river_location():
    """Handle the river location."""
    global player_health, inventory
    
    print("\n" + "=" * 50)
    print("THE RUSHING RIVER")
    print("=" * 50)
    print("""
You follow a path alongside a rushing river. The water is crystal clear,
and you can see colorful stones at the bottom.

As you walk, you notice a simple wooden bridge crossing the river.
Beside it stands an old sign with a Python loop written on it:
for i in range(3):
print("Step " + str(i+1))
The sign says: "To cross safely, tell me what this code outputs."

What do you say?
- [Three steps numbered 1, 2, 3]
- [Three steps numbered 0, 1, 2]
- [Two steps numbered 1, 2]
    """)
    
    while True:
        choice = input("> ").lower().strip()
        if choice == "three steps numbered 1, 2, 3":
            print("\nThe bridge strengthens as if by magic! You cross safely.")
            print("On the other side, you find a rope, which might be useful later.")
            print("You gain a rope!")
            inventory.append("rope")
            print("\nThe path continues along the river and eventually leads to a puzzle room.")
            return "puzzle_room"
            
        elif choice == "three steps numbered 0, 1, 2":
            print("\nThe bridge creaks ominously as you step on it.")
            print("Halfway across, a board breaks beneath your feet!")
            print("You manage to leap to safety, but not without injury.")
            print("You lose 25 health.")
            player_health -= 25
            print("\nOn the other side, the path continues to a cave.")
            return "cave"
            
        elif choice == "two steps numbered 1, 2":
            print("\nThe bridge collapses as you step on it!")
            print("You fall into the river and get swept downstream.")
            print("You lose 40 health.")
            player_health -= 40
            print("\nYou manage to crawl out of the river and find yourself back at the crossroads.")
            return "start"
            
        else:
            print("I don't understand that choice. Try one of the listed options.")

def puzzle_room():
    """Handle the puzzle room location."""
    global player_health, inventory
    
    print("\n" + "=" * 50)
    print("THE PUZZLE ROOM")
    print("=" * 50)
    print("""
All paths have led you here: a chamber with a large door at the far end.
In the center of the room stands a pedestal with a code puzzle.

The pedestal displays:
def mystery_function(x, y):
result = 0
for i in range(y):
result += x
return result
A plaque below asks: "What does mystery_function(4, 7) return?"

To unlock the door, you must solve this Python puzzle.
    """)
    
    # Function solving mini-game
    attempts = 0
    while attempts < 3:
        try:
            answer = int(input("Enter your answer: "))
            if answer == 28:
                print("\nCorrect! The door unlocks with a satisfying click.")
                print("The mystery function performs multiplication through repeated addition!")
                print("\nYou've proven your Python knowledge. The door opens to the final chamber.")
                return "final_chamber"
            else:
                attempts += 1
                print(f"Incorrect. The pedestal glows red. You have {3 - attempts} attempts remaining.")
        except ValueError:
            print("Please enter a valid number.")
    
    # If we get here, the player failed all attempts
    print("\nAfter three incorrect attempts, the floor beneath you gives way!")
    print("You fall into a pit, taking 40 damage!")
    player_health -= 40
    
    if player_health <= 0:
        print("\nYou're too injured to continue...")
        return "end_lose"
    
    print("\nYou manage to climb out of the pit and try again.")
    print("The correct answer was 28 (4 added to itself 7 times).")
    print("The door opens to the final chamber, but you're wounded from the fall.")
    return "final_chamber"

def final_chamber():
    """Handle the final chamber location."""
    global player_health, inventory
    
    print("\n" + "=" * 50)
    print("THE CHAMBER OF THE GEM")
    print("=" * 50)
    print("""
You've reached the final chamber! In the center, on a pedestal, 
glows the legendary Gem of Code, pulsing with Python energy.

However, between you and the gem is a deep chasm too wide to jump across.

How will you reach the gem?
    """)
    
    display_options()
    
    while True:
        choice = input("> ").lower().strip()
        result = handle_choice(choice)
        if result:
            return result

def display_options():
    """Display available options based on inventory."""
    options = []
    
    if "rope" in inventory:
        options.append("- Use the [rope] to swing across")
    
    if "map" in inventory:
        options.append("- Check the [map] for a hidden path")
    
    if "lantern" in inventory:
        options.append("- Use the [lantern] to look for a switch or bridge mechanism")
        
    if not options:
        options.append("- Try to [jump] across anyway (risky)")
    
    options.append("- [turn back] and look for another way")
    
    for option in options:
        print(option)

def handle_choice(choice):
    """Handle the player's choice in the final chamber."""
    global player_health, inventory
    
    if choice == "rope" and "rope" in inventory:
        print("\nYou tie the rope to a sturdy column and swing across the chasm!")
        print("Your grip on programming concepts has prepared you well.")
        return "end_win"
        
    elif choice == "map" and "map" in inventory:
        print("\nThe map reveals a hidden path around the chasm!")
        print("Your careful study of Python documentation has taught you to read maps well.")
        return "end_win"
        
    elif choice == "lantern" and "lantern" in inventory:
        print("\nWith your lantern, you spot a hidden control panel!")
        print("You press a button, and a bridge extends across the chasm.")
        print("Your illuminating knowledge of Python guides you to victory.")
        return "end_win"
        
    elif choice == "jump":
        print("\nWith no equipment to help, you take a running leap...")
        print("You barely catch the edge, scraping yourself badly.")
        player_health -= 50
        
        if player_health <= 0:
            print("You can't hold on and fall into the darkness below...")
            return "end_lose"
        else:
            print("You pull yourself up despite the pain. The gem is within reach!")
            return "end_win"
            
    elif choice == "turn back":
        print("\nYou decide to turn back, but the door has sealed behind you!")
        print("With no way out, you must face the chasm.")
        
    else:
        print("I don't understand that choice. Try one of the listed options.")
        return None

def end_win():
    """Handle the winning ending."""
    print("\n" + "=" * 50)
    print("VICTORY!")
    print("=" * 50)
    print(f"""
You reach the Gem of Code! As you grasp it, knowledge floods your mind.
The secrets of Python programming become clear to you.

With a health of {player_health}% and {len(inventory)} items collected
({', '.join(inventory) if inventory else 'none'}), you have completed
THE PYTHON'S QUEST!

The gem's power turns out to be the confidence and skill you've
gained in your Python journey. With these abilities, you're ready
to create amazing programs and continue your adventures in coding.

THE END

Thank you for playing this mini-project!
You've successfully applied multiple concepts from Module 1:
- Variables and data types
- Conditional statements
- Loops
- Functions
- Lists
- User input

Continue your Python journey with Module 2!
    """)
    return "game_over"

def end_lose():
    """Handle the losing ending."""
    print("\n" + "=" * 50)
    print("GAME OVER")
    print("=" * 50)
    print(f"""
Your health has dropped to {player_health}%. You're too weak to continue...

Despite your best efforts, the Gem of Code remains just out of reach.
However, this is not the end of your Python journey!

You've gained valuable experience and knowledge. With more practice,
you'll surely succeed next time.

Items collected: {', '.join(inventory) if inventory else 'none'}
Locations visited: {len(visited_locations)} out of 6

Thank you for playing this mini-project!
Would you like to try again with your new Python knowledge?

Continue your Python learning with Module 2, and return to defeat
this challenge another day!
    """)
    return "game_over"

# Main game function
def play_game():
    """Play the adventure game."""
    global current_location, player_health
    
    display_intro()
    
    # Game loop
    while current_location != "game_over":
        # Check if player is still alive
        if player_health <= 0:
            current_location = "end_lose"
        
        # Display player status
        display_status()
        
        # Visit current location
        current_location = visit_location(current_location)
        
        # Check for game over conditions
        if current_location in ["end_win", "end_lose"]:
            visit_location(current_location)
            current_location = "game_over"

# ------------------------------------------------------
# EXERCISE: EXTEND THE GAME
# ------------------------------------------------------
# Now it's your turn to extend the game with your own ideas!
#
# Some suggestions:
# 1. Add a new location
# 2. Add a new item with special abilities
# 3. Create a more complex puzzle using Python concepts
# 4. Add a scoring system based on time, health, and items
# ------------------------------------------------------

print("\n--- EXERCISE: EXTEND THE GAME ---")
print("Uncomment the function below and modify it to add your own extension to the game:")


# If this file is run directly, play the game
if __name__ == "__main__":
    play_game()
    
    print("\n" + "=" * 50)
    print("🏆 ACHIEVEMENT UNLOCKED: PYTHON JOURNEYER 🏆")
    print("You've completed Module 1 of Python Journey!")
    print("=" * 50)