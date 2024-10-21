# Rock Paper Scissor game using random module
import random

options = ("rock", "paper", "scissors")
playing = True

while playing:
    player = 0
    computer = random.choice(options)

    choice = input("Type 'start' to start game or 'quit' to quit the game ")
    if choice == "start":
        while player not in options:
            player = input(f"Enter a choice {options} ")
    else:
        print("You quit the game")
        playing = False

    if player and computer is not None:
        print(f"Player: {player}")
        print(f"Computer: {computer}")
        if player == computer:
            print("it's a tie!")
        elif player == "rock" and computer == "scissors":
            print("YOU WIN")
        elif player == "paper" and computer == "rock":
            print("YOU WIN")
        elif player == "scissor" and computer == "paper":
            print("YOU WIN")
        else:
            print("YOU lost! Better luck next time")
