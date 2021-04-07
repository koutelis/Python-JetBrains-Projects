

class Board:
    """
    Tic Tac Toe board
    :cvar slots: Slots redirect keypad numbers to xo (grid) indexes
    :ivar xo: The board grid from upper left to lower right
    """

    slots = {1: 6, 2: 7, 3: 8, 4: 3, 5: 4, 6: 5, 7: 0, 8: 1, 9: 2}

    def __init__(self, xo=None):
        self.xo = xo
        if xo is None:
            self.xo = [7, 8, 9, 4, 5, 6, 1, 2, 3]

    def __str__(self):
        output = '\n' * 10
        rows = [' | '.join(map(str, self.xo[i*3:i*3+3])) for i in range(3)]
        output += '\n---------\n'.join(rows)
        return output
    
    def is_empty(self):
        return len(self.available_slots()) == len(self.xo)
    
    def is_slot_available(self, slot):
        """:return: True if there is at least one available slot, else False"""
        return isinstance(self.xo[slot], int)

    def available_slots(self):
        """:return: a list of available slots to move to."""
        return [i for i in range(len(self.xo)) if self.is_slot_available(i)]
    
    def is_winner(self, player):
        """
		Check if player wins.
		:return: True if the player wins, else False
		"""
        p, xo = player.mark, self.xo

        rows_check = any([all([p == slot for slot in xo[i:i+3]]) for i in range(0, 9, 3)])
        if rows_check: return True

        cols_check = any([all([p == slot for slot in xo[i::3]]) for i in range(3)])
        if cols_check: return True

        diags_check = any([all([p == slot for slot in xo[0:9:4]]),
                            all([p == slot for slot in xo[2:7:2]])])
        if diags_check: return True
        return False
