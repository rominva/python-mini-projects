"""
GAME: Guess The Number
AUTHOR: Romina Valehi
DATE: 2026
VERSION: 4.0
DESCRIPTION: A number guessing game where the user has 5 attempts 
             to guess a randomly generated number within a custom range.
"""

"""
GUESS THE NUMBER GAME - SPECIFICATION
=====================================
REQUIREMENTS:
1. Get two numbers (min, max) from user
2. Generate random number in range [min, max]
3. User attempts to guess the number
4. Limited to 5 attempts
5. Provide feedback after each guess (higher/lower)

RULES:
- Input validation for all user entries
- Graceful error handling
- Clear user instructions
"""

import random


def main():
    show_welcome_message()

    while True:
        try:
            num1_str = input("Smaller number: ")
            num2_str = input("Bigger number: ")

            num1, num2 = validate_input(num1_str, num2_str)
            break
        except ValueError as e:
            print(e)

    # Generate a random number those between 2 numbers
    random_number = random.randint(num1, num2)

    # The user has 5 time opportunity
    guess_attempts = 5
    while guess_attempts > 0:
        # Ask the user for the random number
        try:
            guess = int(input(f"your remained attempt: {guess_attempts} => Guess a number between those two numbers: "))
        except ValueError:
            print("Your guess is not a valid number!🙄")
            continue  # To prevent quiting the program

        is_valid, is_correct, message = validate_guess(num1, num2, guess, random_number)
        print(message)
        if is_correct:
            break # User won
        guess_attempts -= 1
    else:
        print(f"You lost sucker!😝 Number was: {random_number} 💩💩💩")


# Welcome message
def show_welcome_message():
    try:
        from colorama import init, Fore, Style
        init()
        
        print(Fore.CYAN + """
╔══════════════════════════════════════════════╗
║           🎲 GUESS THE NUMBER 🎲             ║
╚══════════════════════════════════════════════╝""" + Style.RESET_ALL)
        
        print(Fore.YELLOW + "\n📖 HOW TO PLAY:" + Style.RESET_ALL)
        print(Fore.RED +   "  🔴 1. Choose two numbers (min and max)" + Style.RESET_ALL)
        print(Fore.GREEN + "  🟢 2. I'll pick a secret number between them" + Style.RESET_ALL)
        print(Fore.YELLOW +"  🟠 3. Try to guess what it is" + Style.RESET_ALL)
        print(Fore.BLUE +  "  🔵 4. I'll give hints if you're wrong" + Style.RESET_ALL)
        print(Fore.MAGENTA+"  🟣 5. Only 5 chances! Choose wisely!" + Style.RESET_ALL)
        
        print(Fore.CYAN + "\n" + "═"*50 + Style.RESET_ALL)
        print(Fore.GREEN + "🎯 GOOD LUCK! YOU'LL NEED IT! ❤" + Style.RESET_ALL)
        print()
        
    except ImportError:
        # The simpler message
        print("\n🎯 WELCOME TO GUESS THE NUMBER GAME! 🎯")

# Validate user inputs and turn them into integers
def validate_input(n1_str, n2_str):
    if not (n1_str.isdigit() and n2_str.isdigit()):
        raise ValueError("Please enter valid numbers!🤨")
    
    n1, n2 = int(n1_str), int(n2_str)

    if n2 <= n1:
        raise ValueError("Your second number must be greater than your first number!😶")

    return n1, n2


# Check thr guess for 3 things: is_valid, is_correct, message
def validate_guess(num1, num2, guess, random_number):
    # Check for valid range: is_valid=False, is_correct=False
    if guess > num2 or guess < num1:
        return False, False,"Your guess is not even between the range!😐"

    # is_valid=True, is_correct=True
    if guess == random_number: 
        return True, True, "Yeyyy! you won!!!🥳"
    # is_valid=True, is_correct=False
    elif guess > random_number:
        return True, False, "Your guess is grater than the random number!🙉"
    else:
        return True, False, "Your guess is smaller than the random number!🙈"


if __name__ == "__main__":
    main()
