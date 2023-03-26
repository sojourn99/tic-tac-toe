from art import logo, board, board_layout
import re
import os

# dictionary for keeping state of moves
board_moves = {
    "1": " ",
    "2": " ",
    "3": " ",
    "4": " ",
    "5": " ",
    "6": " ",
    "7": " ",
    "8": " ",
    "9": " "
}


def is_choice_valid(field: str):
    # check if input is valid and board field is empty
    return re.search(r"^[1-9]$", field) and board_moves[field] == " "


def update_board(field, player):
    # remember player's choice
    board_moves[field] = player

    # draw updated board
    updated_board = board_layout
    for field in board_moves.keys():
        updated_board = updated_board.replace(field, board_moves[field])

    return updated_board


def play_game():
    print(logo)
    is_game_over = False
    print(board_layout)
    print(board)
    player = "X"

    while not is_game_over:

        field = input(f"Player {player} choose field: ")
        if is_choice_valid(field):
            updated_board = update_board(field, player)
            os.system("cls")
            print(logo)
            print(board_layout)
            print(updated_board)
            # switch player
            if player == "X":
                player = "O"
            else:
                player = "X"

        # TODO check if player wins
        # TODO check if all fields are used
        # is_game_over = True


while input("Do you want to play a game of Tic Tac Toe? Type 'y' or 'n': ") == "y":
    os.system("cls")
    play_game()


