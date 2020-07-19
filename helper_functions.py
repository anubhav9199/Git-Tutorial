def create_initial_game_board():

    game_size = int(input("How many rows/columns should the game board have? "))
    game_board = []
    for i in range(game_size):
        row = []
        for i in range(game_size):
            row.append(0)
        
        game_board.append(row)
            
    return game_board

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

def make_move(game_board, player):
    
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

    # draw
    free_positions = []
    for row in game_board:
        for position in row:
            if position == 0:
                free_positions.append(position)

    if len(free_positions) == 0:
        return "draw"
        
    return "ongoing"