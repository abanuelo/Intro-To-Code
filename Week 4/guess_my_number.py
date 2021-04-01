#This repl.it gives an example on how to run while loops with variable manipulation
from random import randrange

my_number = randrange(1,6)
guess = 100000000000

while guess != my_number:
  print("Try to guess my number between 1-5")
  guess = int(input("My guess: ")) #this int() just converts input to a number

print("CONGRATS YOU FOUND MY NUMBER!")
