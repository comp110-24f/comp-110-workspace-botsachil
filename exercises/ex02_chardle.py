"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730771296"


def input_word():
    user_word: str = input("Enter a 5-character word: ")
    # asks user to type a 5 letter word
    if len(user_word) == 5:
        print("'" + user_word + "'")
        # when word length is 5 print word
    else:
        print("Error: Word must contain 5 characters.")
        print("'" + user_word + "'")
        exit()
        # else print error and word

    return user_word


def input_letter():
    user_char: str = input("Enter a single character: ")
    if len(user_char) == 1:
        print("'" + user_char + "'")
        # when character length is 1 print character
    else:
        print("Error: Character must be a single character.")
        print("'" + user_char + "'")
        exit()
        # else print error and word
    return user_char


def contains_char(word: str, character: str):
    print("Searching for " + character + " in " + word)
    count = 0
    if word[0] == character:
        print(character + " found at index 0")
        count = count + 1
    if word[1] == character:
        print(character + " found at index 1")
        count = count + 1
    if word[2] == character:
        print(character + " found at index 2")
        count = count + 1
    if word[3] == character:
        print(character + " found at index 3")
        count = count + 1
    if word[4] == character:
        print(character + " found at index 4")
        count = count + 1

    if count == 0:
        print("No instances of " + character + " found in " + word)
    elif count == 1:
        print(str(count) + " instance of " + character + " found in " + word)
    else:
        print(str(count) + " instances of " + character + " found in " + word)


def main():
    contains_char(word=input_word(), character=input_letter())


if __name__ == "__main__":
    main()
