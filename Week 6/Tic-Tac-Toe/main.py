#DEMO DAY PROJECT FOR INTRO TO CODE
#NAME: <ENTER NAME HERE>
from helper import *


'''
Helper Functions to use:
- check_if_game_done() - this is a conditional
- print_board() - prints most updated board
- update_board(marker, location) tells you were to update the board
'''


if __name__ == "__main__" :
  while(True): #change this condition so that it ends when game is done
    print_board()
    #Player 1's turn
    x_player_loc = input("Player X, where do you want to go (1-9)? ")
    print("Player X selected position: " + str(x_player_loc))
    update_board("X", x_player_loc)
    # print_board()

    #Player 2's Turn - You Figure this out :)