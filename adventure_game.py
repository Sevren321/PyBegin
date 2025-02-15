def adventure_game():
    print("Welcome to Tresure Hunter!")
    print("You find yourself at a crossroad in a dark forest.")

    while True:
        # First Decision Point
        choice = input("Do you go left towards the lake or right towards the mountain? (left/right): ").lower()

        if choice == "left":
            print("\nYou arrive at a serene lake. There's a boat waiting.")
            boat_choice = input("Do you take the boat to cross the lake or stay on shore? (boat/shore): ").lower()

            if boat_choice == "boat":
                print("You cross the lake and find the treasure chest! You win!")
            elif boat_choice == "shore":
                print("You decided to stay. A bear appears! GAME OVER")
            else: 
                print("Invalid choice, please decide again.")
                continue

        elif choice == "right":
            print("\nYou climb the mountain an reach a cave entrance.")
            cave_choice = input("Do you enter the cave or keep climbing? (cave/climb): ").lower()
            
            if cave_choice == "cave":
                print("Inside the cave you find ancient artifacts. You win!")
            elif cave_choice == "climb":
                print("You slip and fall. GAME OVER")
            else:
                print("Invalid choice, please decide again.")
                continue
        
        else: 
            print("Invalid choice, please decide again.")
            continue

        # Option to restart or end the game
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    adventure_game()   