import random
from colorama import Fore, Style, init

init(autoreset=True)

def main():
    print(Fore.CYAN + Style.BRIGHT + "Welcome to the Number Guessing Game!")
    number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input(Fore.YELLOW + "Guess a number between 1 and 100: "))
            attempts += 1
            if guess < number:
                print(Fore.BLUE + "Too low! Try again.")
            elif guess > number:
                print(Fore.MAGENTA + "Too high! Try again.")
            else:
                print(Fore.GREEN + Style.BRIGHT + f"Congratulations! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print(Fore.RED + "Please enter a valid integer.")

if __name__ == "__main__":
    main()