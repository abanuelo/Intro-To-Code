import turtle
from helper import *

'''
Helper Functions for Super Mario Turtle 
--------------------------------------------------------
move()
turn_left()
'''

if __name__ == "__main__":
  ### START CODE HERE ###
  # Hint1: You may want to write a turn_right() function
  # Hint2: Do the hurdles repeat? Can we make a function to jump hurdles?
  # Hint3: How many hurdles are there? Can we use a for loop to jump over?
  def turn_right():
    for i in range(3):
      turn_left()
    
  def jump_hurdle():
    move()
    move()
    move()
    turn_left()
    move()
    move()
    turn_right()
    move()
    move()
    turn_right()
    move()
    move()
    turn_left()

  for i in range(4):
    jump_hurdle()
    
  move()
  move()
  move()
  move()
  ### END CODE HERE ###