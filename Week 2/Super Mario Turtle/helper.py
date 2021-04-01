import turtle #cool graphics toolkit: https://docs.python.org/3/library/turtle.html#module-turtle
'''
SETUP CODE: CREATES THE HURDLES, TURTLE, AND FLAG OBJECT
--------------------------------------------------------
'''
# Setting up the screen
s = turtle.Screen()
s.setup (width=650, height=400, startx=0, starty=0)
s.bgcolor("black")
s.title("Super Mario Turtle")

# Setting different turtles for each hurdle
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t4 = turtle.Turtle()
t5 = turtle.Turtle()
t6 = turtle.Turtle()
turt = turtle.Turtle()

# Setting Drawing Speed for Turtle
t1.speed('fastest')
t2.speed('fastest')
t3.speed('fastest')
t4.speed('fastest')
t5.speed('fastest')
t6.speed('fastest')
turt.speed('fastest')

# Set Hurdle Colors to White
t1.color("white")
t2.color("white")
t3.color("white")
t4.color("white")
t5.color("blue")
t6.color("blue")
turt.color("red")

# Create Hurdle Shape, Flag Pole and Flag
hurdle = ((-20,2),(20,2),(20,-2),(-20,-2))
s.register_shape('hurdle', hurdle)
flag_pole = ((-20,3),(70,3),(70,-3),(-20,-3))
s.register_shape('flag_pole',flag_pole)
flag = ((40,0),(0,-20),(0,0))
s.register_shape('flag', flag)

# Creating first hurdle
t1.penup()
t1.goto(-150,0)
t1.pendown()
t1.shape('hurdle')

# Creating second hurdle
t2.penup()
t2.goto(-50,0)
t2.pendown()
t2.shape('hurdle')

# Creating third hurdle
t3.penup()
t3.goto(50,0)
t3.pendown()
t3.shape('hurdle')

# Creating fourth hurdle
t4.penup()
t4.goto(150,0)
t4.pendown()
t4.shape('hurdle')

#Creating flag pole
t5.penup()
t5.goto(250,40)
t5.pendown()
t5.shape('flag_pole')

#Creating flag
t6.penup()
t6.goto(250,52)
t6.pendown()
t6.shape('flag')
t6.setheading(270)

# Set Turtle at Start Position
turt.penup()
turt.shape('turtle')
turt.goto(-230,-10)
turt.speed('normal')
turt.pendown()

'''
HELPER FUNCTIONS: move() and turn_left()
--------------------------------------------------------
'''

def isHittingHurdle(x,y):
  if (x >= -152 and x <= -148) and (y >= -20 and y <= 20):
    return True
  elif (x >= -52 and x <= -48) and (y >= -20 and y <= 20):
    return True
  elif (x >= 52 and x <= 48) and (y >= -20 and y <= 20):
    return True
  elif (x >= 152 and x <= 148) and (y >= -20 and y <= 20):
    return True
  else:
    return False

def isHittingFlag(x,y):
  if (x <= 255 and x >= 245) and (y >= -20 and y <= 70):
    return True
  else:
    return False

def move():
  turt.forward(20)
  x = int(turt.xcor())
  y = int(turt.ycor())
  #Check if hitting any hurdles
  didHitHurdle = isHittingHurdle(x,y)
  if didHitHurdle:
    print("You hit a hurdle. Invalid run!")
    quit()
    #Check if reached the end
  didHitFlag = isHittingFlag(x,y)
  if didHitFlag:
    print("CONGRATULATIONS! NICE HURDLING!")
    quit()

def turn_left():
  turt.left(90)