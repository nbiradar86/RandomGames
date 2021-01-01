"""
Nihar Biradar
Tic Tac Toe Game: User vs. AI
12-8-20
"""

import copy
import random

board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]
         ]
current_player = 'X'
winner = 'None'


def display_board():
    print("  0   1   2")
    print("    |   |   ")
    print("0 " + board[0][0] + " | " + board[0][1] + " | " + board[0][2])
    print("    |   |   ")
    print(" ---+---+---")
    print("    |   |   ")
    print("1 " + board[1][0] + " | " + board[1][1] + " | " + board[1][2])
    print("    |   |   ")
    print(" ---+---+---")
    print("    |   |   ")
    print("2 " + board[2][0] + " | " + board[2][1] + " | " + board[2][2])
    print("    |   |   ")


def main():
    again = 'Y'
    while again == 'y' or again == 'Y':
        reset_game()

        while not game_over():
            display_board()
            p1_move()
            if not game_over():
                change_player()
                display_board()
                p2_move()
                if not game_over():
                    change_player()

        display_board()
        print("Winner =", winner)
        again = input("Play again?: ")[0]



def p1_move():
    global board
    global current_player
    print("It is {}'s' turn!".format(current_player))
    temp = True
    while temp:
        try:
            user_input_row = eval(input("Please enter a row:"))
            user_input_column = eval(input("Please enter a column:"))
            if board[user_input_row][user_input_column] == ' ':
                board[user_input_row][user_input_column] = current_player
                temp = False
            else:
                print("This space is occupied please choose a different spot!")
        except:
            print("Invalid input, TRY AGAIN!")


def p2_move():
    global board
    move = True
    # Winning
    for row in range(3):
        for col in range(3):
            copy_board = copy.deepcopy(board)
            if copy_board[row][col] == ' ':
                copy_board[row][col] = current_player
                if move and is_winner(copy_board, current_player):
                    board[row][col] = current_player
                    move = False
    # Blocking
    if move:
        for row in range(3):
            for col in range(3):
                copy_board = copy.deepcopy(board)
                if copy_board[row][col] == ' ':
                    copy_board[row][col] = 'X'
                    if move and is_winner(copy_board, 'X'):
                        board[row][col] = current_player
                        move = False
    # Cornering
    if move:
        corner_list = [(0, 0), (0, 2), (2, 0), (2, 2)]
        for pos in corner_list:
            if board[pos[0]][pos[1]] != ' ':
              corner_list.remove(pos)
        if len(corner_list) > 0:
            rand_side = random.choice(corner_list)
            board[rand_side[0]][rand_side[1]] = current_player
            move = False
    # Center
    if move:
        if board[1][1] == ' ':
            board[1][1] = current_player
            move = False
    # Sides
        else:
            while move == True:
                rand_int_row = random.randInt(0, 2)
                rand_int_col = random.randInt(0, 2)
                if board[rand_int_row][rand_int_col] == ' ':
                    board[rand_int_row][rand_int_col] = current_player
                    move = False


def reset_game():
    global winner
    winner = 'None'
    global board
    global current_player
    current_player = 'X'
    board = [[' ' for i in range(3)] for j in range(3)]


def game_over():
    global winner
    if is_winner(board, 'X'):
        winner = 'X'
        return True
    elif is_winner(board, 'O'):
        winner = 'O'
        return True
    else:
        return board_full(board)


def board_full(game_board):
    for i in game_board:
        if ' ' in i:
            return False
    return True


def is_winner(game_board, player):
    for col in range(3):
        if game_board[0][col] == game_board[1][col] == game_board[2][col] == player:
            return True
    for row in range(3):
        if game_board[row][0] == game_board[row][1] == game_board[row][2] == player:
            return True
    if game_board[0][0] == game_board[1][1] == game_board[2][2] == player \
        or game_board[2][0] == game_board[1][1] == game_board[0][2] \
            == player:
        return True


def change_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'
    return current_player


if __name__ == '__main__':
    main()
