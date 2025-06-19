from multiprocessing.connection import answer_challenge
from random import randint
EASY_NUMBER_TURNS= 10
HARD_NUMBER_TURNS=5
def level():
    which_level=input("enter your level easy or hard?").lower()
    if which_level == "easy":
        return EASY_NUMBER_TURNS

    else:
        return HARD_NUMBER_TURNS
def compare(user,actual,turns):
    if user > actual:
        print("too high")
        return turns -1
    elif user < actual:
        print("too low")
        return turns -1
    else:
        print("you win")
def game():

    print("welcome to the game known guess_number")
    actual_number= randint(1,100)
    print(f"the computer's first card is {actual_number}")

    turns=level()
    print(f" you have {turns} attempts remaining to guess the number")
    guess=0
    while guess != actual_number:
        print(f" you have {turns} attempts remaining to guess the number")
        guess= int(input("make a guess: "))
        turns= compare(guess,actual_number,turns)
        if turns == 0:
            print("you lose")
            return
        elif guess !=actual_number:
            print("guess again")
game()

