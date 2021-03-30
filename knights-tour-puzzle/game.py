import controller


class Cell:
    """
    Represents one of the cells of the Board's grid.
    :param board: the board this cell belongs to
    :param x: row position
    :param y: column position
    :ivar key: x and y concatenated
    :ivar mark: its printable character
    :ivar adj_count: number of possible cells it can lead to
    :ivar visited: boolean, whether the cell has been visited
    Note: an adjacent cell is counted by knight's move (chess).
    """

    def __init__(self, x, y, board):
        self.board = board
        self.x = x - 1
        self.y = y - 1
        self.key = str(y) + str(x)
        self.mark = '_' * len(str(board.rows * board.cols))
        self.adj_count = None
        self.visited = False

    def __str__(self):
        return self.mark

    def __lt__(self, other):
        if self.adj_count is None or other.adj_count is None:
            return False
        return self.adj_count < other.adj_count

    def set_mark(self, mark):
        """Set the mark of the cell"""
        prefix = ' ' * (len(str(self.board.rows * self.board.cols)) - len(mark))
        self.mark = f"{prefix}{mark}"
        if {'*', 'x'}.intersection(set(self.mark)):
            self.visited = True

    def unset_mark(self):
        """Revert to original state"""
        self.mark = '_' * len(str(self.board.rows * self.board.cols))
        self.visited = False

    def adjacent_cells(self):
        """Return a set of Cells: possible to move to by Knight's move."""
        max_row = self.board.rows - 1
        max_col = self.board.cols - 1
        adjecent = {self.board.grid[self.x + r][self.y + c] for r in [-2, -1, 1, 2]
                    for c in [-2, -1, 1, 2] if 0 <= self.x + r <= max_row and
                    0 <= self.y + c <= max_col and abs(r) != abs(c)
                    and not self.board.grid[self.x + r][self.y + c].visited}
        return adjecent

    def update_possibilities(self):
        """Update how many possible moves are currently possible from this cell"""
        self.adj_count = len(self.adjacent_cells())

    def has_possible_moves(self):
        """Return true if there is at least one possible move from this cell"""
        return len(self.adjacent_cells()) != 0


class Board:
    """
    Represents the board of the Knight's Tour Puzzle.
    :param rows: number of rows across the y-axis
    :param cols: number of columns across the x-axis
    :ivar grid: 2D array (rows * cols)
    :ivar current: the current cell to make a move away from
    """

    def __init__(self, rows, cols):
        self.rows = rows  # vertical
        self.cols = cols  # horizontal
        self.grid = [[Cell(r, c, self) for c in range(1, cols + 1)] for r in range(1, rows + 1)]
        self.current = None
        self.solution = None

    def __str__(self):
        """
        Printable representation of the Board.
        columns on horizontal axis position (left -> right)
        rows on vertical axis position (bottom -> up)
        """
        l_margin_space = len(str(self.rows))
        cell_width = len(self.grid[0][0].mark) + 1
        line = f'{" " * l_margin_space}--{"-" * (cell_width * self.cols)}-'
        output = line + '\n'
        for r in range(self.rows, 0, -1):
            l_row_space = len(str(self.rows)) - len(str(r))
            output += f'{" " * l_row_space}{r}| '
            for c in range(self.cols):
                cell = self.grid[r - 1][c]
                output += f'{cell} '
            output += '|\n'
        output += f'{line}\n'
        cols_footer = ' ' * (l_margin_space + 1)
        for c in range(1, self.cols + 1):
            num = str(c)
            cols_footer += ' ' * (cell_width - len(num)) + num
        output += cols_footer
        return output

    def get_cell(self, x, y):
        """Return a cell from the grid according to given coordinates."""
        return self.grid[y - 1][x - 1]

    def visit_cell(self, x, y):
        """Mark the cell of given coordinates as 'x' and visited."""
        cell = self.get_cell(x, y)
        cell.set_mark('x')
        return cell

    def update_adj_possib(self):
        """Update the possibilities for each adjacent cell of the current cell"""
        for cell in self.current.adjacent_cells():
            cell.update_possibilities()

    def display_possible_moves(self):
        """
        Mark the number of possible moves for each of the
        adjacent cells of the current cell.
        """
        adjacent = self.current.adjacent_cells()
        self.update_adj_possib()
        for cell in adjacent:
            cell.set_mark(str(cell.adj_count))
        print(self)
        self.current.set_mark('*')
        for cell in adjacent:
            if not cell.visited:
                cell.unset_mark()

    def count_visited(self):
        """Return how many cells have been visited."""
        counter = 0
        for row in self.grid:
            for cell in row:
                if cell.visited:
                    counter += 1
        return counter

    def is_solved(self):
        """Return True if all cells have been visited."""
        for row in self.grid:
            for cell in row:
                if not cell.visited:
                    return False
        return True

    def mark_solution(self):
        """
        Mark each cell of the board with a number,
        according to the solution order.
        """
        if self.is_solvable():
            for i, cell in enumerate(self.solution):
                cell.set_mark(str(i + 1))
                cell.visited = True

    def is_solvable(self):
        """
        Return True if solution is known,
        otherwise try to solve and return if possible.
        """
        if self.solution is None:
            self.solve()
        return len(self.solution) == self.rows * self.cols

    def solve(self):
        """Solve the puzzle."""
        if self.solution is None:
            cell = self.current
            stack = [cell]
            adjacency = {cell: sorted(cell.adjacent_cells())}
            self.solution = self.__solve(stack, adjacency)
            for i, cell in enumerate(self.solution):
                cell.visited = False

    def __solve(self, stack, adj_dict):
        """
        Helper of solve().
        Iteratively solve the puzzle favoring the Warnsdorff rule.
        """
        while 0 < len(stack) < self.rows * self.cols:
            cell = stack[-1]
            cell.visited = True
            if cell not in adj_dict:
                adj_dict[cell] = sorted(cell.adjacent_cells())
            else:
                if len(adj_dict[cell]):
                    stack.append(adj_dict[cell].pop(0))
                else:
                    cell = stack.pop()
                    cell.visited = False
                    adj_dict.pop(cell)
        return stack


def result(gameboard):
    """Check end-game state and print result."""
    if gameboard.is_solved():
        print('What a great tour! Congratulations!')
    else:
        print('No more possible moves!')
        print(f'Your knight visited {gameboard.count_visited()} squares!')


def manual_solution(ctrl):
    """User manually solves the game."""
    board = ctrl.board
    board.display_possible_moves()
    possible = True
    while possible:
        board.current = ctrl.input_coordinates()
        board.display_possible_moves()
        possible = board.current.has_possible_moves()
    result(board)


def auto_solution(ctrl):
    """
    Automatic solution by recursion and backtracking.
    Implemented around Warnsdorff's rule.
    """
    board = ctrl.board
    board.mark_solution()
    if board.is_solved():
        print('Here\'s the solution!')
        print(board)


if __name__ == '__main__':
    # board setup
    ctrl = controller.GameController()
    board = ctrl.input_board_dimensions()
    # initial move
    board.current = ctrl.input_coordinates()
    # solution option
    solve = controller.select_option()
    # check if solvable
    if board.is_solvable():
        board.update_adj_possib()
        solve(ctrl)
    else:
        print('No solution exists!')
