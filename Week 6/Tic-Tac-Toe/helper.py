#Helper code for the tic-tac-toe game

locations = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def check_if_game_done():
  if locations[0] == locations[1] and locations[1] == locations[2]:
    return True
  elif locations[0] == locations[3] and locations[3] == locations[6]:
    return True
  elif locations[0] == locations[4] and locations[4] == locations[8]:
    return True
  elif locations[1] == locations[4] and locations[4] == locations[7]:
    return True
  elif locations[2] == locations[5] and locations[5] == locations[8]:
    return True
  elif locations[3] == locations[4] and locations[4] == locations[5]:   return True
  elif locations[6] == locations[7] and locations[7] == locations[8]:
    return True
  elif locations[2] == locations[4] and locations[4] == locations[6]:
    return True
  else:
    return False

def print_board():
  print(" ____ ____ ____ ")
  print("|    |    |    |")
  print("| " + locations[0] + "  |  " + locations [1] + " |  " + locations[2] + " |")
  print(" ____ ____ ____ ")
  print("|    |    |    |")
  print("| " + locations[3] + "  |  " + locations [4] + " |  " + locations[5] + " |")
  print(" ____ ____ ____ ")
  print("|    |    |    |")
  print("| " + locations[6] + "  |  " + locations [7] + " |  " + locations[8] + " |")
  print(" ____ ____ ____ ")

def update_board(marker, location):
  if location == "1":
    locations[0] = marker
  elif location == "2":
    locations[1] = marker
  elif location == "3":
    locations[2] = marker
  elif location == "4":
    locations[3] = marker
  elif location == "5":
    locations[4] = marker
  elif location == "6":
    locations[5] = marker
  elif location == "7":
    locations[6] = marker
  elif location == "8":
    locations[7] = marker
  else:
    locations[8] = marker