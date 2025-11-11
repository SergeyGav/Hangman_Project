import random

print("Welcome to the Hangman game!")

list_of_words = [
    "banana",
    "monkey",
    "zoom",
    "cat",
    "dog",
    "avocado",
    "tomato",
    "epic"
]

def choose_a_random_word(word_list: list):
    len_of_list = len(word_list)
    random_index = random.randint(a=0, b=len_of_list - 1)
    return word_list[random_index]
random_word = choose_a_random_word(list_of_words)
print(random_word)
# def print_hidden_word(word):
#     ...
#
#
# if __name__ == '__main__':
#     print(choose_a_random_word(list_of_words))

def get_letter():
    letter = input("insert letter: ")
    if letter.isalpha() and len(letter) == 1:
        print(letter)
    else:
        print(False)
    return letter


inserted_letter = get_letter()

if inserted_letter in random_word:
    print("letter exists")
else:
    print("letter does not exist")
