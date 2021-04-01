import turtle
from helper import *

'''
Helper Functions for Draw Chess Board
--------------------------------------------------------
draw_white_square()
draw_black_square()
'''
if __name__ == "__main__" :
  for i in range(size_of_board):
    pen.up()
    pen.setpos(-50, 30 * i)
    pen.down()
    for j in range(size_of_board):
        ### START CODE HERE ###
        # Hint1: When do we draw a black square vs a white square?
        # Hint2: Can we use the value of j and i? print(j) to see what it holds; print(i) to see what it holds
        # Challenge1: Can you make a new draw_square function with different square dimensions     
        draw_black_square()
        ### END CODE HERE ###