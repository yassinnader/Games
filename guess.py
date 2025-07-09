import random
from colorama import Fore, Style  # For colored text

# Game settings
SECRET_WORDS = ["yassin", "python", "developer", "programming", "challenge"]
HINTS = {
    "yassin": ["It's a name", "Starts with Y", "Common in Arabic-speaking countries"],
    "python": ["A programming language", "Also a snake", "Starts with P"],
    "developer": ["Builds software", "Synonym: programmer", "Starts with D"],
    "programming": ["Related to coding", "Requires logic", "Starts with P"],
    "challenge": ["This game is a...", "Synonym: test", "Starts with C"]
}

def choose_difficulty():
    """Returns guess limit based on user's choice"""
    print(f"{Fore.CYAN}Choose difficulty:{Style.RESET_ALL}")
    print("1. Easy (5 guesses)")
    print("2. Medium (3 guesses)")
    print("3. Hard (1 guess)")
    choice = input("Enter choice (1-3): ")
    return 5 if choice == '1' else 3 if choice == '2' else 1

def get_hint(word, guess_count):
    """Provides progressive hints"""
    hints = HINTS.get(word, ["No hints available"])
    return hints[min(guess_count, len(hints)-1)]

def play_game():

    secret_word = random.choice(SECRET_WORDS)
    guess_limit = choose_difficulty()
    guess_count = 0
    score = 100  # Starting score
    hints_used = 0

    print(f"{Fore.YELLOW}Welcome to the Enhanced Guessing Game!{Style.RESET_ALL}")
    print(f"Your word has {len(secret_word)} letters. Good luck!\n")

    while guess_count < guess_limit:
        # Show current progress
        if guess_count > 0:
            print(f"{Fore.MAGENTA}Hint: {get_hint(secret_word, guess_count)}{Style.RESET_ALL}")
        
        guess = input(f"Guess {guess_count+1}/{guess_limit} (or 'quit' to exit): ").strip().lower()
        
        if guess == 'quit':
            print(f"{Fore.RED}Game exited. The word was: {secret_word}{Style.RESET_ALL}")
            return
        
        if not guess:
            print(f"{Fore.RED}Please enter a valid guess!{Style.RESET_ALL}")
            continue
        
        guess_count += 1
        score -= 20  # Deduct points for each guess
        
        # Check for partial matches
        if guess in secret_word:
            print(f"{Fore.GREEN}Good job! '{guess}' is in the word!{Style.RESET_ALL}")
        
        if guess == secret_word:
            print(f"\n{Fore.GREEN}Congratulations! You win with a score of {score}!{Style.RESET_ALL}")
            print(f"You used {guess_count} guesses and {hints_used} hints.")
            return

    print(f"\n{Fore.RED}Out of guesses! The secret word was: {secret_word}{Style.RESET_ALL}")
    print(f"Final score: {max(0, score)}")

def main():
    play_again = True
    while play_again:
        play_game()
        again = input("\nPlay again? (y/n): ").strip().lower()
        play_again = again.startswith('y')
        print("\n" + "="*50 + "\n" if play_again else "")

if __name__ == "__main__":
    main()