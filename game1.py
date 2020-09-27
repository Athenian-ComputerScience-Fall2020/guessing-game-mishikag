'''
Use this file to write an "open" version of the game (no test code or defined format). This will be translated into a testable program later. Use the reponse statements provided to make that transition easier.
collaborators: none
"Your number is too high."
"Your number is too low."
"Your number is out of range."
"I'm sorry you are giving up!"
"I'm sorry, you are out of guesses."

'''
play = True 
while play:
  import random
  range = input("do you want to control the range of the random number? enter yes or no ")

  if range == "yes":
    start_range = int(input("enter the start of your range "))
    end_range = int(input("enter the end of your range "))
    n = random.randint(start_range,end_range)
  else:
    n = random.randint(0,10)

  chances_question = input("do you want to control the amount of chances you have? if yes, enter yes. if no, enter no. ")

  if chances_question == "yes":
    chances = int(input("how many chances do you want "))
    guess = int(input("enter a number to guess "))
  elif user_chances == "no":
    chanes = 5 
    guess = int(input("enter a number to guess. you have 5 chances "))
  print(n) #just to test
  try: 
    def guessing():
      while chances != 0:
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
        if chances == 0:
          print("sorry you ran out of guesses")
  except:
    print("please enter a number ")
    int(input("enter a number to guess "))
    guessing()
  if guess == n:
    print("yay! you guessed the right number which was" ,guess,)
  play_again = input("do you want to play again? enter yes or no ")
  if play_again == "no":
    play = False
    print("okay you are done playing the guessing game")

    
