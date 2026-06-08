"""
Hangman Game
Developed by: Eias Zananiri
CodeAlpha - Python Programming Internship

A simple text-based Hangman game where the player guesses a word one letter at a time.
"""

import random

def display_hangman(attempts):
    """Display the hangman figure based on number of incorrect attempts"""
    hangman_stages = [
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |     /|
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |     /
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |     / \\
           |     
           -
        """
    ]
    return hangman_stages[attempts]

def play_hangman():
    """
    Main function to run the Hangman game
    """
    # Predefined list of words for the game
    word_list = ["PYTHON", "JAVASCRIPT", "DEVELOPER", "PROGRAMMING", "HANGMAN"]
    
    # Select a random word from the list
    secret_word = random.choice(word_list)
    word_length = len(secret_word)
    
    # Game variables
    guessed_word = ["_"] * word_length
    guessed_letters = []
    attempts_left = 6
    game_over = False
    
    print("\n" + "=" * 60)
    print("🎮 WELCOME TO HANGMAN GAME 🎮".center(60))
    print("=" * 60)
    print(f"\n👤 Developed by: Eias Zananiri")
    print(f"📚 Total Words Available: {len(word_list)}")
    print(f"🔤 The word has {word_length} letters.")
    print("\n💡 TIP: You can only guess letters (A-Z). You have 6 attempts!")
    print("\n" + "-" * 60)
    
    while not game_over:
        # Display current game state
        print("\n" + display_hangman(6 - attempts_left))
        print(f"\n📝 Word: {' '.join(guessed_word)}")
        print(f"❌ Incorrect guesses left: {attempts_left}")
        print(f"🔍 Already guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        
        # Get player's guess
        while True:
            guess = input("\n🔢 Guess a letter: ").upper().strip()
            
            # Validate input
            if len(guess) != 1:
                print("⚠️ Please enter only ONE letter!")
            elif not guess.isalpha():
                print("⚠️ Please enter a valid letter (A-Z)!")
            elif guess in guessed_letters:
                print(f"⚠️ You already guessed '{guess}'. Try a different letter!")
            else:
                break
        
        # Add guess to guessed letters list
        guessed_letters.append(guess)
        
        # Check if the guess is in the secret word
        if guess in secret_word:
            print(f"\n✅ Good job! '{guess}' is in the word!")
            
            # Update the guessed word display
            for i, letter in enumerate(secret_word):
                if letter == guess:
                    guessed_word[i] = guess
            
            # Check if the player has won
            if "_" not in guessed_word:
                print("\n" + "🎉" * 15)
                print("🎉 CONGRATULATIONS! YOU WON! 🎉".center(40))
                print("🎉" * 15)
                print(f"\n✨ The word was: {secret_word}")
                print(f"📊 You guessed it in {len(guessed_letters)} tries!")
                game_over = True
        else:
            print(f"\n❌ Sorry! '{guess}' is NOT in the word.")
            attempts_left -= 1
            
            # Check if the player has lost
            if attempts_left == 0:
                print("\n" + display_hangman(6))
                print("\n💀" * 15)
                print("💀 GAME OVER! YOU LOST! 💀".center(40))
                print("💀" * 15)
                print(f"\n✨ The secret word was: {secret_word}")
                print("📊 Better luck next time!")
                game_over = True
    
    # Ask if player wants to play again
    print("\n" + "-" * 60)
    while True:
        play_again = input("\n🔄 Would you like to play again? (yes/no): ").lower().strip()
        if play_again in ['yes', 'y']:
            play_hangman()  # Restart the game
            break
        elif play_again in ['no', 'n']:
            print("\n" + "=" * 60)
            print("👋 THANKS FOR PLAYING HANGMAN!".center(60))
            print("👨‍💻 Developed by: Eias Zananiri".center(60))
            print("=" * 60)
            break
        else:
            print("⚠️ Please enter 'yes' or 'no'!")

# Run the game
if __name__ == "__main__":
    play_hangman()
