""" Rock Paper Scissors
----------------------------------------
"""
import random
import os
import re

os.system('cls' if os.name=='nt' else 'clear')

human_score = 0
ai_score = 0

def check_input(userChoice):
  if not re.match("[SsRrPp]", userChoice):
    print ("Please choose a letter:")
    print ("[R]ock, [S]cissors or [P]aper.")

def ai_choice():
  choices = ['R', 'P', 'S']
  opponenetChoice = random.choice(choices)
  return opponenetChoice

def compare_my_input_to_ai_input(userChoice, opponenetChoice):
  global ai_score
  global human_score
  if opponenetChoice == str.upper(userChoice):
    print ("Tie! ")
  elif opponenetChoice == 'R' and userChoice.upper() == 'S':      
    print ("Scissors beats rock, AI BOT win! ")
    ai_score += 1
  elif opponenetChoice == 'S' and userChoice.upper() == 'P':      
    print ("Scissors beats paper! AI BOT wins! ")
    ai_score += 1
  elif opponenetChoice == 'P' and userChoice.upper() == 'R':      
    print ("Paper beat rock, AI BOT wins! ")
    ai_score += 1
  else:       
    print ("You win!")
    human_score +=1


'''
STUDENT CODE: Your code goes in the main method :)
--------------------------------------------------------
'''
if __name__ == "__main__" :
  ### START CODE HERE ###
  while (True):
    print ("Rock, Paper, Scissors - Shoot!")
    userChoice = input("Choose your weapon [R]ock, [P]aper, or [S]cissors: ")
    check_input(userChoice)
  #Hint1: First check input to see if it is valid
  #Hint2: get the ai response and compare with your userChoice
  #Challenge1: Can you add a point system to this game?
  ### END CODE HERE ###