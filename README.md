# Knight's Tour Algorithm

This Python script implements a solution to the [Knight's Tour problem](https://en.wikipedia.org/wiki/Knight%27s_tour) using depth-first search.

## Description

The Knight's Tour problem is a classic problem in the field of computer science. The problem is to move a knight on a chessboard such that it visits every square exactly once.

This script uses a depth-first search algorithm to find a solution to the problem. The algorithm starts at a given position, then recursively explores all possible moves from that position. If a move leads to a solution, the algorithm stops and returns the solution.

## How to Run

To run the script, you need Python 3 and the following libraries:

- matplotlib
- numpy

You can install these libraries using pip:

```bash
pip install matplotlib numpy
```

Then you can run the script with:

```
python main.py
```

## Code Structure

size: The size of the chessboard.

board: A 2D list representing the chessboard. Each cell contains the move number when the knight visited that cell, or -1 if the cell has not been visited.

moves: A list of the eight possible moves of a knight.

is_valid_move(x, y): A function that checks if a move is valid.

possible_jumps(x, y): A function that returns all possible moves for a knight from a given position.

## Visualization
The script uses matplotlib to visualize the chessboard and the path of the knight. Each cell is labeled with the move number when the knight visited that cell.
