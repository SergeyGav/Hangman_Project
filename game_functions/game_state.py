# ========================================
# HANGMAN GAME - GAME STATE
# ========================================

# --- FUNCTION 1 ---
# Write a function that checks if the player has won.
# The player wins when there are no more letters in the hidden_letters set.
# Return True if won, False otherwise.

def check_win_condition(hidden_letters):
    if len(hidden_letters) == 0:
        return True
    else:
        return False


# --- FUNCTION 2 ---
# Write a function that checks if the player has lost.
# The player loses when attempts_remaining reaches 0.
# Return True if lost, False otherwise.

def check_lose_condition(attempts_remaining):
    if attempts_remaining == 0:
        return True
    else:
        return False


# --- FUNCTION 3 ---
# Write a function that checks if the game is over (either won or lost).
# Use the previous two functions.
# Return True if game is over, False otherwise.

def is_game_over(hidden_letters, attempts_remaining):
    if check_win_condition(hidden_letters)  or check_lose_condition(attempts_remaining) :
        return True
    else:
        return False


# Test your functions here!
if __name__ == "__main__":
    ### --- Test Function 1: check_win_condition --- ###

    ###Test 1.1 - Empty set (all letters guessed)###
    # result = check_win_condition(set())
    # print(result)  # Expected: True

    ###Test 1.2 - Set with letters remaining###
    # result = check_win_condition({"p", "y", "n"})
    # print(result)  # Expected: False

    ###Test 1.3 - Set with one letter remaining###
    # result = check_win_condition({"x"})
    # print(result)  # Expected: False

    ### --- Test Function 2: check_lose_condition --- ###

    ###Test 2.1 - Zero attempts remaining (lost)###
    # result = check_lose_condition(0)
    # print(result)  # Expected: True

    ###Test 2.2 - Some attempts remaining###
    # result = check_lose_condition(3)
    # print(result)  # Expected: False

    # ##Test 2.3 - One attempt remaining###
    # result = check_lose_condition(1)
    # print(result)  # Expected: False

    ###Test 2.4 - Many attempts remaining###
    # result = check_lose_condition(6)
    # print(result)  # Expected: False

    ### --- Test Function 3: is_game_over --- ###

    ###Test 3.1 - Game won (no hidden letters remaining)###
    # result = is_game_over(set(), 3)
    # print(result)  # Expected: True (won)

    ###Test 3.2 - Game lost (no attempts remaining)###
    # result = is_game_over({"c", "a", "t"}, 0)
    # print(result)  # Expected: True (lost)

    ###Test 3.3 - Game still in progress###
    # result = is_game_over({"a", "t"}, 4)
    # print(result)  # Expected: False (still playing)

    ###Test 3.4 - Game won with attempts remaining###
    # result = is_game_over(set(), 6)
    # print(result)  # Expected: True (won)

    ##Test 3.5 - Last attempt, letters still hidden###
    # result = is_game_over({"x", "y"}, 1)
    # print(result)  # Expected: False (still playing)

    pass