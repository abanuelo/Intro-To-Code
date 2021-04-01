#give me your age
age = 1000000

#give me your name
name = "MY NAME GOES HERE"

#Do a name check with basic if else
if name == "MY NAME GOES HERE":
  print("You still have not changed your name")
else:
  print("Nice to meet you!")

#Do a more complex age check
if age < 10:
  print("An elementary student taking my class! Right on!")
elif age > 10 and age < 15:
  print("Middle schooler huh. Nice!")
elif age > 15 and age < 30:
  print("Welcome to the real world sunny.")
else:
  print("Age is but a number I guess.")

#Try using input
favorite_color = input("What is your favorite color? ")

if favorite_color == "blue":
  print("I love blue!")
elif favorite_color == "red":
  print("Red is aight")
elif favorite_color == "green":
  print("No thank you. Just kidding. Nice color.")
elif favorite_color == "pink":
  print("Pink is perfect.")
else:
  print("Okay then....")