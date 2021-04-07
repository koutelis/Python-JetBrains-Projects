from controller import GameController


def play():
    """
    Run this function to start the Knight's Tour Puzzle.
    It can be solved either by user or CPU.
    """
    # board setup
    ctrl = GameController()
    board = ctrl.input_board_dimensions()
    # initial move
    board.current = ctrl.input_coordinates()
    # solution option (user or cpu)
    solve = ctrl.select_solution_option()
    # check if solvable
    if board.is_solvable():
        board.update_adj_possib()
        solve(ctrl)
    else:
        print('No solution exists!')


def result(gameboard):
    """Check end-game state and print result."""
    if gameboard.is_solved():
        print('What a great tour! Congratulations!')
    else:
        print('No more possible moves!')
        print(f'Your knight visited {gameboard.count_visited()} squares!')
