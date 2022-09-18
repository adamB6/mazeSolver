# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 15:57:18 2022

@author: asbot
"""

def generate_path(maze, path):
    # If node (row, col) is in path
    # update the value of the node to '.'
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if (row,col) in path:
                maze[row][col] = '.'

    for row in maze:
        line = ''.join(row)
        print(line)
    
    # Write solved maze to file
    with open("solved.txt", "w") as data:
        for row in maze:
            data.write( "".join(row))
            data.write("\n")

def solve(maze, source_col, source_row):

    currentRow = source_row
    currentCol = source_col
    current = (source_row, currentCol)
    previous = (source_row, source_col)
    path = set() # Path will store all moves.

    while True:
        current = (currentRow, currentCol)
        path.add(current)
        neighbors = [
            maze[currentRow + 1][currentCol],
            maze[currentRow][currentCol + 1],
            maze[currentRow - 1][currentCol],
            maze[currentRow][currentCol - 1],
        ]

        # Stop if one of the neighbors is the exit.
        if neighbors[0] == 'E' or neighbors[1] == 'E' or neighbors[2] == 'E' or neighbors[3] == 'E':
            break

        # If statements for determining where the wall is and which way
        # to move. Before updating position, sets previous() 
        # to current position (row, col).
        if neighbors[0] == '#' and neighbors[1] == ' ':   
            previous = (currentRow, currentCol)    
            currentCol += 1
        elif neighbors[1] == '#' and neighbors[2] == ' ':
            previous = (currentRow, currentCol)               
            currentRow -= 1
        elif neighbors[2] == '#' and neighbors[3] == ' ':
            previous = (currentRow, currentCol)            
            currentCol -= 1
        elif neighbors[3] == '#' and neighbors[0] == ' ':
            previous = (currentRow, currentCol)               
            currentRow += 1
        # If no wall is nearby, determine next move by checking
        # what the previous position is. This is to deal with corners.
        else:
            if previous == (currentRow + 1, currentCol):            
                currentCol += 1    
            elif previous == (currentRow, currentCol + 1):            
                currentRow -= 1     
            elif previous == (currentRow - 1, currentCol):
                currentCol -= 1   
            else:           
                currentRow += 1

    generate_path(maze, path)

def read_maze(maze_file):
    maze = []
    with open(maze_file, "r") as data:
        for line in data:
            line = line.rstrip()
            line = [ch for ch in line]
            maze.append(line)
    return maze

def main(maze_file):
    maze = read_maze(maze_file)
    
    source_col = 1
    source_row = len(maze) - 2

    print(maze)

    solve(maze, source_col, source_row)

if __name__ == "__main__":
    main("maze_c.txt")