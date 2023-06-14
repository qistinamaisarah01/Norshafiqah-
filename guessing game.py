#!/usr/bin/env python

import random

def main(): 
    """Start a music genre guessing game."""
    print("Welccome to the guessing game!")
          
# List of music genre that you can guess.
    musicgenre = ["k-pop","pop","rock","jazz"]

# Funtion will choose one random music genre from the list
    x = random.choice(musicgenre)
    guess = None

    while x != guess:
        
        guess = str(input("Pick a music genre between k-pop,pop,rock and jazz!"))

        if x == guess:
            print("You guessed it right,genius!")
            break
        else:
            print("Please try guessing again.")
main()