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