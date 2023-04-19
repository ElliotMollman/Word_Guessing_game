import random

def format_green(text):
    bg = lambda text, color: "\33[48;5;" + str(color) + "m" + text + "\33[0m"
    text = bg(text, 46) + " "
    return text
def format_yellow(text):
    bg = lambda text, color: "\33[48;5;" + str(color) + "m" + text + "\33[0m"
    text = bg(text, 226) + " "
    return text
def format_grey(text):
    bg = lambda text, color: "\33[48;5;" + str(color) + "m" + text + "\33[0m"
    text = bg(text, 231) + " "
    return text
def format_newline(text):
    print("\n")
def rules():
    print("WORD GAME!\n Try to guess the chosen word.\n\n Rules: Only enter 5 letter word with no"
          "special characters.\n        A green letter indicates the letter is in the word and in the right "
          "spot, and yellow means it is in the word")
    print("\nList of words:")
    for word in word_list:
        print(word, end=' ')
def main(word_list):
    Continue = 'y'
    while Continue == 'y':
        chosen_word = random.choice(word_list).upper()
        attempt_tally = 0
        max_tries = 0
        for count in range(6):
            max_tries += 1
            index = 0
            points = 0
            attempt_tally += 1
            guess = input(f"\n\n{attempt_tally}- Enter a five letter word: ").upper()
            if guess.isalpha() and len(guess) == 5:
                for letter in guess:
                    if letter in chosen_word and letter == chosen_word[index]:
                        print(format_green(letter), end=' ')
                        points += 1
                    elif letter in chosen_word:
                        print(format_yellow(letter), end=' ')
                    elif letter not in chosen_word:
                        print(letter, end=' ')
                    index += 1
            else:
                print("Sorry, enter only 5 alphabetical characters\n")
            if points == 5:
                print(f"\nCongratulations you guessed the word in {max_tries} attempt(s)!")
                break
        if max_tries == 6:
            print("\nYou've ran out of guesses.")
        Continue = input("Continue? y/n: ")
        if Continue == 'n':
            break
if __name__ =="__main__":
    word_list = ('WORDS', 'SPOON', 'SOCKS', 'LEMON', 'PAGES', 'ARROW', 'BUNNY', 'HORSE', 'PAPER')
    rules()
    main(word_list)
