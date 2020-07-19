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