# ========================================
# HANGMAN GAME - GAME LOGIC
# ========================================

# --- FUNCTION 1 ---
# Write a function that checks if a letter exists in a word.
# Return True if the letter is in the word, False otherwise.

def check_letter_in_word(letter, word):
    if letter in word:
        x = True
    else:
        x = False
    return x


# --- FUNCTION 2 ---
# Write a function that gets a word and a set of guessed_letters.
# The function will return the word, with space between each letter.
# Every letter in the word, that has not been guessed, will be "_" instead.

# For example: if the word is "python", and the guessed letters are {"a", "b", "f", "y", "o"}
# the function should return "_ y _ _ o _".

def get_hidden_word_with_visible_guessed_letters(word, guessed_letters):
    guessed_word = ""
    for i in word:
        if i in guessed_letters:
            guessed_word = guessed_word + (i + " ")
        else:
            guessed_word = guessed_word + ("_ ")
    return guessed_word


# --- FUNCTION 3 ---
# Write a function that adds a letter to the guessed letters set.
# It should modify the set in place (set.add("a")).

def update_guessed_letters(letter: str, guessed_letters: set):
    guessed_letters = guessed_letters.add(letter)
    return guessed_letters


# --- FUNCTION 4 ---
# Write a function that counts how many times a letter appears in a word.
# Return the count.

def count_letter_occurrences(letter, word):
    count = 0
    for i in word:
        if i == letter:
            count = count + 1
    return count


# --- FUNCTION 5 ---
# Write a function that gets a list of letters and a set of guessed letters.
# The function will return a string, with all the letters from a list (separated with white space).
# Every letter from the list, that is also in the guessed_letters set, will have the string "\u0336" added to it.

# Example:
#       if guessed_letters = {"c", "e"},
#       and letters_alphabet is ["a", "b", "c", "d", "e"]

#       then the function will return "a b c\u0336 d e\u0336"
#       (it will look like this if printed: "a b c̶ d e̶"

def alphabet_display_with_guessed_letters_marked(letters_alphabet, guessed_letters):
    string_return = ""
    for i in letters_alphabet:
        if i in guessed_letters:
            x = i + "\u0336"
        else:
            x = i
        string_return = string_return + (x + " ")
    return string_return



# --- FUNCTION 6 ---
# Write a function that receives a set of letters, and a letter.
# The function will remove the letter from the set.
# (The function will not return anything!)

def update_letters_to_be_guessed(hidden_letters, letter):
    hidden_letters.discard(letter)


# Test your functions here!
if __name__ == "__main__":
    ### --- Test Function 1: check_letter_in_word --- ###

    ###Test 1.1###
    # result = check_letter_in_word("p", "python")
    # print(result)  # Expected: True

    ###Test 1.2###
    # result = check_letter_in_word("x", "python")
    # print(result)  # Expected: False

    ###Test 1.3###
    result = check_letter_in_word("a", "banana")
    print(result)  # Expected: True

    ###Test 1.4###
    # result = check_letter_in_word("n", "banana")
    # print(result)  # Expected: True

    ### --- Test Function 2: get_hidden_word_with_visible_guessed_letters --- ###

    ###Test 2.1###
    # result = get_hidden_word_with_visible_guessed_letters("cat", {"c"})
    # print(result)  # Expected: "c _ _"
    #
    # #Test 2.2###
    result = get_hidden_word_with_visible_guessed_letters("banana", {"a", "n"})
    print(result)  # Expected: "_ a n a n a"
    #
    # ###Test 2.3###
    # result = get_hidden_word_with_visible_guessed_letters("hello", {"e", "l"})
    # print(result)  # Expected: "_ e l l _"
    # #
    # # ###Test 2.4###
    # result = get_hidden_word_with_visible_guessed_letters("python", {"y", "o"})
    # print(result)  # Expected: "_ y _ _ o _"
    # #
    # # ###Test 2.5###
    # result = get_hidden_word_with_visible_guessed_letters("word", set())
    # print(result)  # Expected: "_ _ _ _"

    ### --- Test Function 3: update_guessed_letters --- ###

    ###Test 3.1###
    letters = {"a", "b"}
    update_guessed_letters("c", letters)
    print(letters)  # Expected: {"a", "b", "c"}

    ###Test 3.2###
    # letters = set()
    # update_guessed_letters("x", letters)
    # print(letters)  # Expected: {"x"}

    ###Test 3.3###
    # letters = {"a", "b", "c"}
    # update_guessed_letters("d", letters)
    # print(letters)  # Expected: {"a", "b", "c", "d"}

    ### --- Test Function 4: count_letter_occurrences --- ###

    ###Test 4.1###
    # result = count_letter_occurrences("a", "banana")
    # print(result)  # Expected: 3

    ###Test 4.2###
    result = count_letter_occurrences("l", "hello")
    print(result)  # Expected: 2

    ###Test 4.3###
    # result = count_letter_occurrences("x", "python")
    # print(result)  # Expected: 0

    ###Test 4.4###
    # result = count_letter_occurrences("o", "programming")
    # print(result)  # Expected: 1

    ### --- Test Function 5: alphabet_display_with_guessed_letters_marked --- ###

    ###Test 5.1###
    # letters_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    # result = alphabet_display_with_guessed_letters_marked(letters_alphabet, {"a", "e", "t"})
    # print(result)  # Expected: "a̶ b c d e̶ f g h i j k l m n o p q r s t̶ u v w x y z"

    ###Test 5.2###
    letters_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    result = alphabet_display_with_guessed_letters_marked(letters_alphabet, set())
    print(result)  # Expected: "a b c d e f g h i j k l m n o p q r s t u v w x y z"

    ###Test 5.3###
    # letters_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    # result = alphabet_display_with_guessed_letters_marked(letters_alphabet, {"z", "a"})
    # print(result)  # Expected: "a̶ b c d e f g h i j k l m n o p q r s t u v w x y z̶"

    ### --- Test Function 6: update_letters_to_be_guessed --- ###

    ###Test 6.1###
    # hidden_letters = {"p", "y", "t", "h", "o", "n"}
    # update_letters_to_be_guessed(hidden_letters, "p")
    # print(hidden_letters)  # Expected: {"y", "t", "h", "o", "n"}

    ###Test 6.2###
    hidden_letters = {"a", "b", "c"}
    update_letters_to_be_guessed(hidden_letters, "b")
    print(hidden_letters)  # Expected: {"a", "c"}

    ###Test 6.3###
    # hidden_letters = {"x"}
    # update_letters_to_be_guessed(hidden_letters, "x")
    # print(hidden_letters)  # Expected: set() (empty set)

    pass