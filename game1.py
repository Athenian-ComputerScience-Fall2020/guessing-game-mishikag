'''
Use this file to write an "open" version of the game (no test code or defined format). This will be translated into a testable program later. Use the reponse statements provided to make that transition easier.
collaborators: none
"Your number is too high."
"Your number is too low."
"Your number is out of range."
"I'm sorry you are giving up!"
"I'm sorry, you are out of guesses."

'''
import random
chances = 5
n = random.randint(0,10)
guess = int(input("enter a number to guess. you have 5 chances "))
chances-=1
try: 
    while chances > 0:
        if n < guess:
            chances-=1
            print("your guess",guess,"is too high")
            guess = int(input("enter a number to guess. "))
        if n > guess:
            chances-=1
            print("your guess",guess,"is too low")
            guess = int(input("enter a number to guess. "))
        if guess == n:
            break
        if guess == quit:
            quit = q
        if str(guess) == q:
            break
except:
    print("please enter a number ")
if str(guess)==q:
    print("okay, you are done playing the game")
if guess == n:
    print("yay! you guessed the right number which was" ,guess,)
if guess != n:
    print("sorry, you ran out of guesses")

    
