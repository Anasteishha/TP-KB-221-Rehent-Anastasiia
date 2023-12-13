import random

def get_user_choice():
    user_choice = input("Enter your choice (stone, scissor, paper): ").lower()
    while user_choice not in ["stone", "scissor", "paper"]:
        print("Invalid choice. Please enter stone, scissor, or paper.")
        user_choice = input("Enter your choice (stone, scissor, paper): ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(["stone", "scissor", "paper"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "stone" and computer_choice == "scissor") or \
         (user_choice == "scissor" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "stone"):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    main()
