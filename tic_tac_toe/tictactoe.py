# Tic Tac Toe game against AI.
# Warning : You may never win.

import random

def printboard(board):
    # prints the tic tac toe board
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("--------------------")

def playerselect():
    # asks player to select X or O
    playerin = input("X or O: ").upper()
    if playerin == "X":
        player = "X"
        computer = "O"
    elif playerin == "O":
        computer = "X"
        player = "O"
    else:
        print("Baka select 'X' or 'O': ")
        player , computer = playerselect()
    return player , computer

def playermove(board):
    # input from player on position to move
    move = input("Where would you like to move: ")
    if move not in "1 2 3 4 5 6 7 8 9".split():
        print("Wrong input! Try again idiot")
        move  = playermove(board)
        return int(move)
    if board[int(move)-1] != " ":
        print("Position is already filled baka! Try again: ")
        move = playermove(board)
        return int(move)
    return int(move) - 1

def computermove(board , player , computer):
    
    # checks if computer can win in the next move.
    for i in range(9):
        cb = board[::]
        if board[i] == " ":
            cb[i] = computer
            if cheackwin(cb , computer):
                return i

    # checks if the player can win in the next move.
    for i in range(9):
        cb = board[::]
        if board[i] == " ":
            cb[i] = player
            if cheackwin(cb , player):
                return i
    
    if board[4] == " ":
        # takes the centre if it is empty.
        return 4 
    else:
        # takes any random empty place.
        emptyindex = []
        for i in range(9):
            if board[i] == " ":
                emptyindex.append(i)
        return random.choice(emptyindex)


def updateboard(board , position , var):
    board[position] = var
    return

def cheackwin(b , ch):
    return ((b[0] == b[1] == b[2] == ch) or (b[3] == b[4] == b[5] == ch) or (b[6] == b[7] == b[8] == ch) or
            (b[0] == b[3] == b[6] == ch) or (b[1] == b[4] == b[7] == ch) or (b[2] == b[5] == b[8] == ch) or
            (b[0] == b[4] == b[8] == ch) or (b[6] == b[4] == b[2] == ch))

def main():
    board = [" " for _ in range(0,9)]
    print("Konichiwa!\nTIC TAC TOE: ")
    printboard(board)
    player , computer = playerselect()
    choise = random.choice((player , computer))

    if choise == player:
        position = playermove(board)
    else:
        position = computermove(board , player ,computer)
    
    updateboard(board , position , choise)
    printboard(board)

    while (cheackwin(board , player) != True) and (cheackwin(board,computer) != True):
        if " " not in board:
            print("DRAW!!")
            break
        if choise == player:
            position = computermove(board , player , computer)
            choise = computer
        else:
            position = playermove(board)
            choise = player
        updateboard(board , position , choise)
        printboard(board)

    if cheackwin(board , player) == True:
        print("Congratulations! You defeated a machine.")
    elif cheackwin(board , computer) == True:
        print("The machine has taken over!")

    print("Ely Psy Congree!")

main()