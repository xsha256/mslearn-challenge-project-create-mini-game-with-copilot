import random
def get_user_choice():
    while True:
        user_choice = input("Choose (rock, paper, or scissors): ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tied"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "you won"
    else:
        return "you lost"
    

def main():
    your_score = 0
    rounds = 0

    while True:
        user_choice = get_user_choice()
        options = ["rock", "paper", "scissors"]
        computer_choice = random.choice(options)

        print("Computer chose:", computer_choice)

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "you won":
            your_score += 1

        rounds += 1


        if not get_user_decision():
            break

    print(f"Your score is: {your_score}")
    print(f"Rounds: {rounds}")

def get_user_decision():
    while True:
        user_choice = input("Do you want to play again? (yes or no): ").lower()
        if user_choice == "yes":
            return True 
        elif user_choice == "no":
            return False 
        else:
            print("Invalid choice. Please choose yes, or no.")

if __name__ == "__main__":
    main()