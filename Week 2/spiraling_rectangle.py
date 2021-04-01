import turtle #cool graphics toolkit: https://docs.python.org/3/library/turtle.html#module-turtle
'''
SETUP CODE: Square Function and Turtle and Screen
--------------------------------------------------------
''' 
# Setting up the screen
s = turtle.Screen()
s.setup(width=700, height=500, startx=0, starty=0)
s.bgcolor("black")

# creating instance of turtle 
pen = turtle.Turtle()
pen.speed("slowest")
pen.color("red")

def my_sqrfunc(size):
   for i in range(4):
      pen.fd(size)
      pen.left(90)
      size = size - 5

'''
STUDENT CODE: Your code goes in the main method :)
--------------------------------------------------------
'''
if __name__ == "__main__":
  ### START CODE HERE ###
  # Hint1: Can you make a for loop to increase or decrease the size getting passed into my_sqrfunc
  # Hint2: Can we make a variable for size to modify in our for loop
  # Challenge1: Can you define a new function to make a spiraling triangle: this can help: https://www.geeksforgeeks.org/draw-spiraling-triangle-using-turtle-in-python/?ref=rp
  size = -150
  for i in range(16):
    my_sqrfunc(size-2)
  ### END CODE HERE ###