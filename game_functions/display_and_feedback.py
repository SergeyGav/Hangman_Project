# ========================================
# HANGMAN GAME - DISPLAY & FEEDBACK
# ========================================

# --- FUNCTION 1 ---
# Write a function that returns the hangman ASCII art based on incorrect guesses.
# Use the stages from the "ascii_art.py" file.

# from common.ascii_art import hangman_7_stages
#
#
# def show_hangman(incorrect_guesses, hangman_art: list[str] = hangman_7_stages):
#     x = incorrect_guesses
#     return x

# --- FUNCTION 2 ---
# Write a function that displays the current game status.
# It should print: current display, alphabet with strikethroughs, and attempts remaining.
# Example output:
# Word: _ _ t h _ _
# Letters: a̶ b c d e̶ f g h i̶ j k l m n o p q r s t̶ u v w x y z
# Attempts remaining: 4

# Note:
#   This function requires the alphabet_display_with_guessed_letters_marked function
#   from game_logic.py to work properly

# def display_game_status(letters_alphabet, guessed_letters, hidden_word, attempts_remain):



# --- FUNCTION 3 ---
# Write a function that displays a win message.
# Example: "Congratulations! You guessed the word: python"

# def show_win_message(word):
#     print(f"Congratulations! You guessed the word:", word)



# --- FUNCTION 4 ---
# Write a function that displays a lose message.
# Example: "Game Over! The word was: python"

# def show_lose_message(word):
#     print(f"Game Over! The word was:", word)



# Test your functions here!
if __name__ == "__main__":
    ### --- Test Function 1: show_hangman --- ###

    ###Test 1.1 - No incorrect guesses (empty gallows)###
    # print(show_hangman(0))
    # Expected: empty gallows (stage 0)

    ###Test 1.2 - Three incorrect guesses###
    # print(show_hangman(3))
    # Expected: head, body, one arm (stage 3)

    ###Test 1.3 - Six incorrect guesses (full hangman)###
    # print(show_hangman(6))
    # Expected: complete hangman (stage 6)

    ###Test 1.4 - One incorrect guess###
    # print(show_hangman(1))
    # Expected: head only (stage 1)

    ### --- Test Function 2: display_game_status --- ###

    ###Test 2.1 - Mid-game status###
    # letters_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    # guessed_letters = {"a", "e", "i", "t"}
    # hidden_word = "but"
    # display_game_status(letters_alphabet, guessed_letters, hidden_word, 5)
    # Expected output:
    # Word: _ _ t
    # Letters: a̶ b c d e̶ f g h i̶ j k l m n o p q r s t̶ u v w x y z
    # Attempts remaining: 5

    ###Test 2.2 - Starting game###
    # letters_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    # guessed_letters = set()
    # hidden_word = "banana"
    # display_game_status(letters_alphabet, guessed_letters, hidden_word, 6)
    # Expected output:
    # Word: _ _ _ _ _ _
    # Letters: a b c d e f g h i j k l m n o p q r s t u v w x y z
    # Attempts remaining: 6

    ### --- Test Function 3: show_win_message --- ###

    ###Test 3.1###
    # show_win_message("python")

    ###Test 3.2###
    # show_win_message("hangman")

    ### --- Test Function 4: show_lose_message --- ###

    ###Test 4.1###
    # show_lose_message("python")

    ###Test 4.2###
    # show_lose_message("secret")

    pass