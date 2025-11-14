# ========================================
# HANGMAN GAME - INPUT & VALIDATION
# ========================================
from main_game import inserted_letter


# --- FUNCTION 1 ---
# Write a function that asks the user to input a letter.
# The function will return the user's input (as lowercase).

# def get_letter_from_user():
#     inserted_letter = input("Input a letter: ")
#     inserted_letter = inserted_letter.lower()
#     return inserted_letter



# --- FUNCTION 2 ---
# Write a function that checks if the input_letter is a valid single letter.
# Valid means: exactly one character AND it's an alphabetical letter.
# Return True if valid, False otherwise.
# (you can use .isalpha())

# def is_valid_letter(input_letter):
#
#     if len(input_letter) == 1 and input_letter.isalpha():
#         return True
#     else:
#         return False


# --- FUNCTION 3 ---
# Write a function that checks if a letter has already been guessed.
# The function receives a letter and a set of guessed letters.
# Return True if the letter is in the set, False otherwise.

# def is_already_guessed(letter, guessed_letters):
#     returned_letter_status = False
#     for i in guessed_letters:
#         if letter == i:
#             returned_letter_status = True
#             break
#     return returned_letter_status

# --- FUNCTION 4 ---
# Write a function that keeps asking for input until a valid, new letter is entered. (looping until all conditions are met)
# Use the previous functions (get_letter_from_user, is_valid_letter, is_already_guessed).
# Return the valid letter.

def get_valid_guess(guessed_letters):
    ...


# Test your functions here!
if __name__ == "__main__":
    ### --- Test Function 1: get_letter_from_user --- ###
    # This function requires user input, so test it manually by uncommenting:

    ###Test 1.1###
    # print("Please enter a letter:")
    # letter = get_letter_from_user()
    # print(f"You entered: {letter}")  # Expected: lowercase version of your input

    ### --- Test Function 2: is_valid_letter --- ###

    ###Test 2.1###
    # result = is_valid_letter("G")
    # print(result)  # Expected: True

    ###Test 2.2###
    # result = is_valid_letter("a")
    # print(result)  # Expected: True

    ###Test 2.3###
    # result = is_valid_letter("tar")
    # print(result)  # Expected: False

    ###Test 2.4###
    # result = is_valid_letter("y-")
    # print(result)  # Expected: False

    ###Test 2.5###
    # result = is_valid_letter("")
    # print(result)  # Expected: False

    ###Test 2.6###
    # result = is_valid_letter("5")
    # print(result)  # Expected: False

    ###Test 2.7###
    # result = is_valid_letter(" ")
    # print(result)  # Expected: False

    ### --- Test Function 3: is_already_guessed --- ###

    ##Test 3.1###
    # result = is_already_guessed("a", {"a", "b", "c"})
    # print(result)  # Expected: True

    ###Test 3.2###
    # result = is_already_guessed("d", {"a", "b", "c"})
    # print(result)  # Expected: False

    ###Test 3.3###
    # result = is_already_guessed("x", set())
    # print(result)  # Expected: False

    ###Test 3.4###
    # result = is_already_guessed("b", {"a", "b", "c", "d", "e"})
    # print(result)  # Expected: True

    ### --- Test Function 4: get_valid_guess --- ###
    # This function requires user input, so test it manually by uncommenting:

    ###Test 4.1 - Test with empty guessed_letters###
    # print("Enter a valid letter (any letter should work):")
    # letter = get_valid_guess(set())
    # print(f"Valid letter entered: {letter}")  # Expected: the valid letter you entered

    ###Test 4.2 - Test with some already guessed letters###
    # print("Enter a valid letter that hasn't been guessed (try not to use 'a', 'b', or 'c'):")
    # letter = get_valid_guess({"a", "b", "c"})
    # print(f"Valid letter entered: {letter}")  # Expected: the valid letter you entered (not a, b, or c)

    ###Test 4.3 - Test validation (try entering invalid input first)###
    # print("Try entering: '123', 'abc', or an already guessed letter, then enter a valid one:")
    # letter = get_valid_guess({"x", "y", "z"})
    # print(f"Valid letter entered: {letter}")  # Expected: keeps asking until you enter a valid, unguessed letter

    pass