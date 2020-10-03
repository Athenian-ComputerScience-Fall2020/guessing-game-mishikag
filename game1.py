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

def guessing(chances, guess, n):
    #if chances don't equal 0, the code will run all this below
            while chances >= 1:
        #if the user inputs a guess that is higher than the number, it will print saying their guess is too high, and then will proceed to having them guess again
                if n < guess:
                    chances-=1
                    print("your guess",guess,"is too high")
                    guess = int(input("enter a number to guess. "))
        #if the user inputs a guess that is lower than the number, it will print saying their guess is too low, and then will proceed to having them guess again
                if n > guess:
                    chances-=1
                    print("your guess",guess,"is too low")
                    guess = int(input("enter a number to guess. "))
        #if the user guesses the correct number, the code will break out of the while loop
                if guess == n:
                    break
        #if the user runs out of guesses the code will break out of the while loop
                if chances == 0:
                    break

#using a boolean we can have the user play the game again without having to rerun the code 
play = True 
while play:
    #asks if the user wants to control the range
    choice_range = input("do you want to control the range of the random number? enter yes or no ")

#if they want to contorl the range, it will ask for the range, and if not the decided range will be 0-10
    if choice_range == "yes":
        start_range = int(input("enter the start of your range "))
        end_range = int(input("enter the end of your range "))
        n = random.randint(start_range,end_range)
    elif choice_range =="no":
        n = random.randint(0,10)

#this asks the user if they want to chose the number of chances they can have
    chances_question = input("do you want to control the amount of chances you have? if yes, enter yes. if no, enter no. ")
#if they enter yes, it will ask how many chances they want, and if no, then the amount of chances they have is 5
    if chances_question == "yes":
        chances = int(input("how many chances do you want "))
        guess = int(input("enter a number to guess "))
    elif chances_question == "no":
        chances = 5 
    #guessing now starts
        guess = int(input("enter a number to guess. you have 5 chances "))

    #try is if the user inputs a bad input
    try: 
    #all in a function to call it if the user uses a bad input and the code goes to the except or if they want to play again
        guessing(chances, guess, n)
    #if the user inputs a bad input the try and except will run and it will tell the user to enter a number and will continue the guessing game
    except:
        print("please enter a number ")
    #this calls the function guessing to run and to continue running the game
        guessing(chances, guess, n)

    #after breaking from the code because the user guessed the correct number, it will print a message saying they guessed the number
    if guess == n:
        print("yay! you guessed the right number which was" ,guess,)
    #after breaking from the code because the user ran out of guesses, it will print a message saying they ran out of guesses
    if chances == 0:
        print("sorry you ran out of guesses")
    
    #this part of the code is to ask the user if they want to play again without having to re-run the program
    play_again = input("do you want to play again? enter yes or no ")
    #if they enter no, play will become false, and the code will not run because on line 33 the while loop must be True for it to run
    if play_again == "no":
        play = False
        print("okay you are done playing the guessing game")
