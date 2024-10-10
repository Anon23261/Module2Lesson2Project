# Task 1: Choose a Place
def adventure_game():
    while True:
        place = input("Choose a place (forest or cave): ").strip().lower()

        if place == "forest":
            action = input("You are in the forest. Choose an action (climb a tree or cross a river): ").strip().lower()
            if action == "climb a tree":
                print("You found a bird's nest!")
            elif action == "cross a river":
                print("You found a boat!")
            else:
                print("Now you are on an unknown path.") # Task 3: Default Path    

# Task 2: Setting the Scene
        elif place == "cave":
            action = input("You are in the cave. Choose an action (light a torch or proceed in the dark): ").strip().lower()
            if action == "light a torch":
                print("You see beautiful cave piantings!")
            elif action == "proceed in the dark":
                print("You stumble upon hidden treasure!")
            else:
                print("Now you are on an unknown path.") # Task 3: Default Path
        else:
            print("You are on an unknown path.") # Task 3: Default Path

        play_again = input("Do you want to play again? (yes or no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

adventure_game()