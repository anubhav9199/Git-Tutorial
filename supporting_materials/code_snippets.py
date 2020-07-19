######################################################################################
#                                  coding session 1                                  #
######################################################################################

### README.md

'''
# command line based Tic-Tac-Toe game
- 2 players
- colored X and O
'''


### helper_functions.py

game_board = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]

def show(game_board):
    
    # separator between moves
    print("---------------------------------")

    # header indicating column numbers
    header_row = " "
    for i in range(len(game_board)):
        header_row += "  " + str(i)
    print(header_row)
    
    # row numbers and actual game board
    for row_index, row in enumerate(game_board):
        print(row_index, row)
    
    # empty line for clarity
    print("")
    
    return



######################################################################################
#                                  coding session 2                                  #
######################################################################################

### README.md

'''
# Tic-Tac-Toe

The goal of this project is to craete a 2-player Tic-Tac-Toe game. 
The Xs and Os should be displayed in color.
'''


### helper_functions.py
### add at the end

def change(game_board, player):
    
    # game interaction
    print(f"Player {player}:")
    choice = input("Which position (row, column) do you want to play?: ")
    row, column = choice.split(",")
    row, column = int(row), int(column)

    # making the actual move
    if game_board[row][column] != 0:
        raise Exception("This position is already taken!")

    else:
        game_board[row][column] = player
        return game_board



######################################################################################
#                                  coding session 3                                  #
######################################################################################

### helper_functions.py
### add at the end

def determine_game_status(game_board):
    
    # horizontal winner
    for row in game_board:
        player = row[0]
        if row.count(player) == len(row) and player != 0:
            return "horizontal win"
        
    # vertical winner
    for index in range(len(game_board)):
        column_elements = []
        for row in game_board:
            column_elements.append(row[index])
        
        player = column_elements[0]
        if column_elements.count(player) == len(column_elements) and player != 0:
            return "vertical win"
        
    # diagonal winner (\)
    diagonal_elements = []
    for index in range(len(game_board)):
        diagonal_elements.append(game_board[index][index])
    
    player = diagonal_elements[0]
    if diagonal_elements.count(player) == len(diagonal_elements) and player != 0:
        return "diagonal win"
        
    # diagonal winner (/)
    diagonal_elements = []
    indices = range(len(game_board))
    for row, column in zip(indices, reversed(indices)):
        diagonal_elements.append(game_board[row][column])
    
    player = diagonal_elements[0]
    if diagonal_elements.count(player) == len(diagonal_elements) and player != 0:
        return "diagonal win"
        
    return "ongoing"


### helper_functions.py
### replace lines 1-3

def create_initial_game_board():

    game_size = int(input("How many rows/columns should the game board have? "))
    game_board = []
    for i in range(game_size):
        row = []
        for i in range(game_size):
            row.append(0)
        
        game_board.append(row)
            
    return game_board



######################################################################################
#                                  coding session 4                                  #
######################################################################################

### on branch 'dev'
### game.py

from itertools import cycle
from helper_functions import (
    create_initial_game_board,
    show,
    change,
    determine_game_status
)


players = cycle([1, 2])
playing = True

while playing:

    # game preparations
    game_board = create_initial_game_board()
    game_status = determine_game_status(game_board)

    while game_status == "ongoing":
        show(game_board)

        # player move
        current_player = next(players)
        game_board = change(game_board, current_player)

        # stopping condition for while-loop
        game_status = determine_game_status(game_board)
        if game_status != "ongoing":
            show(game_board)
            print("Game finished!!!")
            print(f"Player {current_player} has achieved a {game_status}! \n")
            
    keep_playing = input("Do you want to play again? (y/n) ")
    if keep_playing != "y":
        playing = False



######################################################################################
#                                  coding session 5                                  #
######################################################################################

### on branch 'all_the_same'
### helper_functions.py
### replace "determine_game_status" function

def determine_game_status(game_board):

    # helper function
    def all_the_same(lst):
        player = lst[0]
        if (lst.count(player) == len(lst)) and player != 0:
            return True
        else:
            return False
    
    # horizontal winner
    for row in game_board:
        if all_the_same(row):
            return "horizontal win"
        
    # vertical winner
    for index in range(len(game_board)):
        column_elements = []
        for row in game_board:
            column_elements.append(row[index])
        
        if all_the_same(column_elements):
            return "vertical win"
        
    # diagonal winner (\)
    diagonal_elements = []
    for index in range(len(game_board)):
        diagonal_elements.append(game_board[index][index])
    
    if all_the_same(diagonal_elements):
        return "diagonal win"
        
    # diagonal winner (/)
    diagonal_elements = []
    indices = range(len(game_board))
    for row, column in zip(indices, reversed(indices)):
        diagonal_elements.append(game_board[row][column])
    
    if all_the_same(diagonal_elements):
        return "diagonal win"
        
    return "ongoing"


### on branch 'master'
### helper_functions.py
### insert at line 86

# draw
free_positions = []
for row in game_board:
    for position in row:
        if position == 0:
            free_positions.append(position)

if len(free_positions) == 0:
    return "draw"


### on branch 'master'
### game.py
### replace lines 26-31

# stopping condition for while-loop
game_status = determine_game_status(game_board)
if game_status != "ongoing":
    show(game_board)
    print("Game finished!!!")

    if game_status == "draw":
        print("It is a draw! \n")
    else:
        print(f"Player {current_player} has achieved a {game_status}! \n")



######################################################################################
#                                  coding session 6                                  #
######################################################################################

### on branch 'valid_move'
### game.py
### replace lines 22-24

# player move
current_player = next(players)
valid_move = False
while not valid_move:
    try: 
        game_board = change(game_board, current_player)
        valid_move = True


### on branch 'master'
### simply rename function 'change' to 'make_move' in all places
### in helper_functions.py on line 34
### in game.py on lines 5 and 24


### on branch 'valid_move'
### game.py
### replace lines 22-28

# player move
current_player = next(players)
valid_move = False
while not valid_move:
    try: 
        game_board = change(game_board, current_player)
        valid_move = True
        
    except Exception as e:
        print("\n")
        print("Something went wrong:", e)
        print("Hint: The chosen position must be available on the board.")
        print("Hint: The values must be separated by a comma e.g. '0, 1'.")
        print("Try again!", "\n")



######################################################################################
#                                  coding session 7                                  #
######################################################################################

### helper_functions.py
### insert at beginning of file

from colorama import Fore, Style


### helper_functions.py
### replace lines 27-29

# row numbers and actual game board
for row_index, row in enumerate(game_board):
    colored_row = ""
    for item in row:
        if item == 0:
            colored_row += "   "
        elif item == "X":
            colored_row += Fore.GREEN + " X " + Style.RESET_ALL
        elif item  == "O":
            colored_row += Fore.MAGENTA + " O " + Style.RESET_ALL
    print(row_index, colored_row)


### game.py
### replace line 10

players = cycle(["X", "O"])