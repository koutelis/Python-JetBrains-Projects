

class Cell:
    """
    Represents one of the cells comprising the (Knight's Tour Puzzle) Board's grid.
    Note: an adjacent cell is counted by knight's move (chess).

    :param board: the board this cell belongs to
    :param x: row position (as presented on board)
    :param y: column position (as presented on board)
    :ivar x: row position (0-based index)
    :ivar y: column position (0-based index)
    :ivar key: x and y concatenated
    :ivar mark: its printable character
    :ivar adj_count: number of possible cells it can lead to
    :ivar visited: boolean, whether the cell has been visited
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