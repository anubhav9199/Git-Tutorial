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