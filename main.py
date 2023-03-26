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
    """
    Checks if input is a valid field number and chosen field is empty.
    :param field: field number on playing board
    :type field: str
    :return: True or False
    :rtype: boolean
    """
    return re.search(r"^[1-9]$", field) and board_moves[field] == " "


def update_board(field: str, player: str):
    """
    Marks the player's field choice on the board.
    :param field: field number on playing board
    :type field: str
    :param player: the player making the field choice
    :type field: str
    :return: the updated board
    :rtype: str
    """

    # remember player's choice
    board_moves[field] = player

    # draw updated board
    updated_board = board_layout
    for field in board_moves.keys():
        updated_board = updated_board.replace(field, board_moves[field])

    return updated_board


def check_winner(player: str):
    """
    Checks if the given player has won.
    :param player: the player making the last move
    :type player: str
    :return: True or False
    :rtype: boolean
    """
    player_has_won = False
    if board_moves["1"] == player and board_moves["2"] == player and board_moves["3"] == player:
        player_has_won = True
    elif board_moves["4"] == player and board_moves["5"] == player and board_moves["6"] == player:
        player_has_won = True
    elif board_moves["7"] == player and board_moves["8"] == player and board_moves["9"] == player:
        player_has_won = True
    elif board_moves["1"] == player and board_moves["4"] == player and board_moves["7"] == player:
        player_has_won = True
    elif board_moves["2"] == player and board_moves["5"] == player and board_moves["8"] == player:
        player_has_won = True
    elif board_moves["3"] == player and board_moves["6"] == player and board_moves["9"] == player:
        player_has_won = True
    elif board_moves["1"] == player and board_moves["5"] == player and board_moves["9"] == player:
        player_has_won = True
    elif board_moves["3"] == player and board_moves["5"] == player and board_moves["7"] == player:
        player_has_won = True
    return player_has_won


def check_game_over():
    """
    Checks if all fields have player marks.
    :return: True or False
    :rtype: boolean
    """
    game_over = True
    for value in board_moves.values():
        if value == " ":
            game_over = False
            break
    return game_over


def reset_board():
    """
    Removes all player marks from board.
    """
    for field in board_moves.keys():
        board_moves[field] = " "


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

            if check_winner(player):
                is_game_over = True
                reset_board()
                print(f"{player} has won!")

            if check_game_over():
                is_game_over = True
                reset_board()
                print("Draw! Game over.")

            # switch player
            if player == "X":
                player = "O"
            else:
                player = "X"


while input("Do you want to play a game of Tic Tac Toe? Type 'y' or 'n': ") == "y":
    os.system("cls")
    play_game()
