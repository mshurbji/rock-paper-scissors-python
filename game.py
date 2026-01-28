import random

# available choices in the game
CHOICES = {
    1: "Rock",
    2: "Paper",
    3: "Scissors"
}

def print_rules():
    # basic game rules for the user
    print(
        "Winning rules:\n"
        "Rock vs Paper -> Paper wins\n"
        "Rock vs Scissors -> Rock wins\n"
        "Paper vs Scissors -> Scissors wins\n"
    )

def get_user_choice():
    # keep asking until we get a valid input
    while True:
        try:
            choice = int(input("Enter your choice (1-Rock, 2-Paper, 3-Scissors): "))
            if choice in CHOICES:
                return choice
            print("Please enter 1, 2 or 3.")
        except ValueError:
            print("Invalid input, numbers only!")

def get_winner(user, computer):
    # returns the winning choice or DRAW if both are the same
    if user == computer:
        return "DRAW"
    if (user == 1 and computer == 3) or (user == 3 and computer == 1):
        return "Rock"
    if (user == 1 and computer == 2) or (user == 2 and computer == 1):
        return "Paper"
    return "Scissors"

def play_game():
    user_choice = get_user_choice()
    comp_choice = random.randint(1, 3)

    print(f"User choice: {CHOICES[user_choice]}")
    print(f"Computer choice: {CHOICES[comp_choice]}")

    winner = get_winner(user_choice, comp_choice)

    # print result based on the winner
    if winner == "DRAW":
        print("It's a tie!")
    elif winner == CHOICES[user_choice]:
        print("User wins!")
    else:
        print("Computer wins!")

def main():
    print_rules()
    while True:
        play_game()
        again = input("Play again? (Y/N): ").lower()
        if again != "y":
            print("Thanks for playing!")
            break

# entry point
if __name__ == "__main__":
    main()
