import matplotlib.pyplot as plt
import numpy as np

# the size of the chessboard
size = 8

# create a 2D list to represent the board
board = [[-1 for _ in range(size)] for _ in range(size)]

# define the eight possible moves of a knight
moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

# check if a move is valid
def is_valid_move(x, y):
    return 0 <= x < size and 0 <= y < size and board[x][y] == -1

# get all possible moves for a knight from a given position
def possible_jumps(x, y):
    jumps = []
    for dx, dy in moves:
        if is_valid_move(x + dx, y + dy):
            jumps.append((x + dx, y + dy))
    return jumps

# Recursive function to perform the knight's tour
def knight_tour(x, y, move_count):
    board[x][y] = move_count
    if move_count == size*size - 1:
        return True
    for next_x, next_y in possible_jumps(x, y):
        if knight_tour(next_x, next_y, move_count + 1):
            return True
    # Backtrack if no further moves are possible
    board[x][y] = -1
    return False

# visualize the board with a heatmap
def visualize_board():
    global board
    # convert the board list to a NumPy array for easier plotting
    board_array = np.array(board)
    fig, ax = plt.subplots()
    ax.matshow(board_array, cmap='magma')
    for i in range(size):
        for j in range(size):
            ax.text(j, i, str(board_array[i][j]), va='center', ha='center', color='blue')
    plt.show()

# start the knight's tour from the top-left corner of the board
if knight_tour(0, 0, 0):
    print("Knight's tour is complete:")
    visualize_board()
else:
    print("Knight's tour is not possible.")
