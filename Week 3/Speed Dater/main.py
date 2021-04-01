### Speed Date ###
# Get to know your date some more and ask them some questions you want to know the answer to!

# I made this here: https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
'''
SETUP CODE: Setups our speed dater prompt
--------------------------------------------------------
''' 
speed_dater = """
 (                             (                            
 )\ )                   (      )\ )            )            
(()/(          (    (   )\ )  (()/(      )  ( /(   (   (    
 /(_))`  )    ))\  ))\ (()/(   /(_))  ( /(  )\()) ))\  )(   
(_))  /(/(   /((_)/((_) ((_)) (_))_   )(_))(_))/ /((_)(()\  
/ __|((_)_\ (_)) (_))   _| |   |   \ ((_)_ | |_ (_))   ((_) 
\__ \| '_ \)/ -_)/ -_)/ _` |   | |) |/ _` ||  _|/ -_) | '_| 
|___/| .__/ \___|\___|\__,_|   |___/ \__,_| \__|\___| |_|   
     |_|    
"""

print(speed_dater)
print("Get to know your date a little more. Ask them some questions. Don't be shy!")
print()

'''
STUDENT CODE: Your code goes in the main method :)
--------------------------------------------------------
'''
if __name__ == "__main__" :
  response1 = input("Do you like lizards? ")
  if response1 == "yes":
    print("Wow me too. That's a good start.")
  else:
    print("I think we should see other people. But I'll give you a shot.")
  
  response2 = input("Have you ever had a dog? ")
  if response2 == "yes":
    print("Nice! I had a chihuahua once.")
  else:
    print("What a bummer. You are mussing out!")
  

  ### START CODE HERE ###
  # Hint1: Use input to ask more questions and use the model above
  # Challenge1: How can you look for certain info in a response? see: if "<blank>" in response

  ### END CODE HERE ###

