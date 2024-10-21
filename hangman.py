# The hangman game
import random

words = ["apple", "orange", "alpaca", "ant", "anteater", "antelope", "ape", "armadillo", "baboon", "badger", "bat", "bear", "beaver", "bee", "bison", "boar", "buffalo", "butterfly"]


# The hangman art is where you display the hangman through ascii art
# This is a dictionary of key:() (tuples as values)
hangman_art = { 0: ("   ",
                   "   ",
                   "   "),
                1: (" o ",
                   "   ",
                   "   "),
                2: (" o ",
                   " | ",
                   "   "),
                3: (" o ",
                   "/| ",
                   "   "),
                4: (" o ",
                   "/|\\",
                   "   "),
                5: (" o ",
                   "/|\\",
                   "/  "),
                6: (" o ",
                   "/|\\",
                   "/ \\")}


def display_man(wrong_guesses):
    print("************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("************")


def display_hint(hint):
    print(" ".join(hint))


def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter:" ).lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN! HURRAY!!!🥳")
            is_running = False
        elif wrong_guesses >= 6:
            display_man(wrong_guesses) 
            display_answer(answer)
            print("Is the answer!")
            print("YOU LOSE🥺")
            print("Better luck next time")
            is_running = False


if __name__ == "__main__":
    main()