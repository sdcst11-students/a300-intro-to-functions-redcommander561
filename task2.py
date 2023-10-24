"""
Task 2:
Create a program to play a number guessing game
There should be a function:
title()
displays instructions and how to play

game()
plays the games
"""
import random

def title():
    print("pick a number 1 through 10: ")

def game():
    guess = int(input(""))
    randNum = int(random.randint(0,10))
    if guess == randNum:
        print(f"you got it! the number was {randNum}")
    
    
    else:
        print(f"wrong, the number was {randNum} ")

title()

game()