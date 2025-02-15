import random

def get_player_choice():
    while True:
        choice = input("Enter your choice (Rock/Paper/Scissors): ").lower()
        if choice in ['rock','paper','scissors']:
            return choice
        print("Invalid choice. Please try again.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        print("It's a tie.")
    elif (
        (player_choice == 'rock' and computer_choice == 'scissors') or
        (player_choice == 'scissors' and computer_choice == 'paper') or
        (player_choice == 'paper' and computer_choice == 'rock')
    ):
        return "You win!"
    else: 
        return "Computer wins!"
    
# Main game loop
while True:
    rounds = 3 
    player_wins = 0
    computer_wins = 0

    for round in range(rounds):
        print(f"\nRound {round + 1}:")
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()

        print(f"You chose: {player_choice.capitalize()}")
        print(f"Computer chose: {computer_choice.capitalize()}")

        round_winner = determine_winner(player_choice, computer_choice)
       

        if round_winner == "You win!":
            player_wins += 1
            print("You win this round!")
        elif round_winner == "Computer wins!":
            computer_wins += 1
            print("Computer wins this one.")
        


    print("\nThat's the end of the rounds.")
    if player_wins > computer_wins:
        print("Congatulations you win!")
    elif player_wins < computer_wins:
        print("The Computer wins!")
    else:
        print("It's a tie!")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break

