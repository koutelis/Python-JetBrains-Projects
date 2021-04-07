from board import Board


class GameController:
    """
    Class responsible for user interaction, receiving input,
    validation of input and option selection.
    Manipulates the board according to user input.

    :ivar board: The game's board to be controlled
    """

    def __init__(self, board=None):
        self.board = board

    def input_board_dimensions(self):
        """
        Ask user to input two numbers, rows and columns.
        If input is valid: create and return a new game Board, else persist asking for input.
        """
        while True:
            user_input = input("Enter your board dimensions: ")
            if GameController.__validate_board_dimensions(user_input):
                rows, cols = tuple(map(int, user_input.split()))
                self.board = Board(cols, rows)  # inverted because the implementation matrix is transposed
                return self.board
            else:
                print('Invalid dimensions!')

    def input_coordinates(self):
        """
        Ask user to input two numbers, row and column, within board range.
        If input is valid: mark and return relevant cell, else persist asking for input.
        """
        if self.board.current:
            msg = 'Enter your next move: '
        else:
            msg = 'Enter the knight\'s starting position: '
        while True:
            user_input = input(msg)
            if self.__validate_coordinates(user_input):
                x, y = tuple(map(int, user_input.split()))
                if self.__validate_move(x, y):
                    return self.board.visit_cell(x, y)
                print('Invalid move! ', end='')
            else:
                print('Invalid dimensions!')

    @staticmethod
    def __validate_board_dimensions(dimensions):
        """
        Validate if given input is two numbers within correct ranges.
        1st number range: 1 - max number of board's rows
        2nd number range: 1 - max number of board's columns
        """
        dimensions = dimensions.split()
        if not GameController.__validate_length(dimensions):
            return False
        if not GameController.__validate_integers(dimensions):
            return False
        if int(dimensions[0]) < 1 or int(dimensions[1]) < 1:
            return False
        return True

    def __validate_coordinates(self, coordinates):
        """
        Validate if given input is two numbers within correct ranges.
        1st number range: 1 - max number of board's rows
        2nd number range: 1 - max number of board's columns
        """
        coordinates = coordinates.split()
        if not GameController.__validate_length(coordinates):
            return False
        if not GameController.__validate_integers(coordinates):
            return False
        coordinates = tuple(map(int, coordinates))
        if not self.__validate_range(coordinates):
            return False
        return True

    @staticmethod
    def __validate_length(data):
        """helper of validate_input()."""
        return len(data) == 2

    @staticmethod
    def __validate_integers(data):
        """helper of validate_input()."""
        x, y = data[0], data[1]
        return x.isdigit() and y.isdigit()

    def __validate_range(self, data):
        """helper of validate_input()."""
        x, y = data
        return 1 <= x <= self.board.cols and 1 <= y <= self.board.rows

    def __validate_move(self, x, y):
        """Return true if possible to move to given coordinates."""
        target_cell = self.board.get_cell(x, y)
        if self.board.current is None:
            return True
        adjacent = self.board.current.adjacent_cells()
        if target_cell not in adjacent or target_cell.visited:
            return False
        return True
    
    @staticmethod
    def select_solution_option():
        """Ask user to select a solution option and return the relevant function."""
        while True:
            user_input = input('Do you want to try the puzzle? (y/n): ')
            if user_input == 'y':
                return manual_solve
            if user_input == 'n':
                return auto_solve
            else:
                print('Invalid input')


def manual_solve(ctrl):
    """User manually solves the game."""
    board = ctrl.board
    board.display_possible_moves()
    possible = True
    while possible:
        board.current = ctrl.input_coordinates()
        board.display_possible_moves()
        possible = board.current.has_possible_moves()
    result(board)


def auto_solve(ctrl):
    """
    Automatic solution by recursion and backtracking.
    Implemented by Warnsdorff's rule.
    """
    board = ctrl.board
    board.mark_solution()
    if board.is_solved():
        print('Here\'s the solution!')
        print(board)
