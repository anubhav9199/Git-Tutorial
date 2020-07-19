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
