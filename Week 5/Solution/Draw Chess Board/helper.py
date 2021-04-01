# import turtle package 
import turtle  
'''
SETUP CODE: Sets up screen and makes white and black square
--------------------------------------------------------
''' 
# create screen object 
s = turtle.Screen() 
s.setup(width=700, height=500, startx=0, starty=-200)
s.bgcolor("orange")
s.title("Draw Chess Board")
   
# create turtle object 
pen = turtle.Turtle() 
pen.speed('slow')
   
# method to draw white square 
def draw_white_square(): 
  pen.fillcolor("white")
  pen.begin_fill()
  for i in range(4): 
    pen.forward(30) 
    pen.left(90) 
  pen.forward(30)
  pen.end_fill()

# method to draw black square
def draw_black_square():
  pen.fillcolor("black")
  pen.begin_fill()
  for i in range(4): 
    pen.forward(30) 
    pen.left(90) 
  pen.forward(30)
  pen.end_fill()

# Setting the size of the chess board
size_of_board = 4