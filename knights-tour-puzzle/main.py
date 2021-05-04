from game import play


if __name__ == "__main__":
    introduction = '''Welcome to the Knights Tour Puzzle!

- You will first be prompted to input the size of the board in the format x y
where x is x-axis and y is the y-axis. 
In other words input two numbers (representing columns by rows) separated by a space
- Then you will input the knight\'s starting position by coordinates of the same x y format.
- Select between automatic or manual solution. 
If you select manual, the program will calculate if the puzzle is solvable and report accordingly.
This process may take some time if the grid is big, so aim for a board less than 9 * 9\n'''

    print(introduction)
    play()
