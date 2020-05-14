# Tic-Tac-Toe game

from random import choice
from time import sleep

class Board:
    """Tic Tac Toe board"""

    # xo is the board state from upper left to lower right
    starting_slots = (7, 8, 9, 4, 5, 6, 1, 2, 3)

    def __init__(self, xo=starting_slots):
        self.xo = list(xo)

    def __str__(self):
        xo = self.xo
        l0 = '\n' * 10
        l1 = ' {} | {} | {} '.format(xo[0], xo[1], xo[2])
        l2 = '---|---|---'
        l3 = ' {} | {} | {} '.format(xo[3], xo[4], xo[5])
        l4 = '---|---|---'
        l5 = ' {} | {} | {} '.format(xo[6], xo[7], xo[8])
        return f'{l0}{l1}\n{l2}\n{l3}\n{l4}\n{l5}'

    def available_slots(self):
        return [i for i, avail_slot in enumerate(self.xo) if isinstance(avail_slot, int)]

    def win_check(self, player):
        xo = self.xo
        # check rows
        if any([(player == xo[0] == xo[1] == xo[2]), (player == xo[3] == xo[4] == xo[5]), (player == xo[6] == xo[7] == xo[8])]):
            return True
        # check cols
        elif any([(player == xo[0] == xo[3] == xo[6]), (player == xo[1] == xo[4] == xo[7]), (player == xo[2] == xo[5] == xo[8])]):
            return True
        # check diag
        elif any([(player == xo[0] == xo[4] == xo[8]), (player == xo[2] == xo[4] == xo[6])]):
            return True
        return False


class Player:
    """Tic Tac Toe Player"""

    # slots redirect keypad numbers to board.xo indexes
    slots = {1: 6, 2: 7, 3: 8, 4: 3, 5: 4, 6: 5, 7: 0, 8: 1, 9: 2}

    def __init__(self, mark, mode):
        """ MARK: select 'X' or 'O' | MODE: select 'easy', 'medium' or 'hard' """
        self.mark = mark
        self.mode = mode

    def __str__(self):
        return self.mark


class human(Player):
    """Human Tic Tac Toe Player"""

    def move(self):
        """ human player moves by inputting coordinates"""
        while True:
            while True:
                try:
                    slot = int(input(f'{self.mark}: Enter a slot number > '))
                    break
                except Exception:
                    print('You should enter a number!')
            # check for valid coordinates
            if (slot < 1) or (slot > 9):
                print('You should enter a number from 1 to 9!')
            else:
                return self.slots[slot]


class cpu(Player):
    """CPU Tic Tac Toe Player"""

    best_move = None  # minimax algorithm changes this value

    def move(self):
        """CPU player plays according to specified mode of difficulty"""

        def move_random():
            """EASY difficulty: random move"""
            while True:
                slot = choice(list(self.slots.keys()))
                if isinstance(board.xo[self.slots[slot]], int):
                    return self.slots[slot]

        def win_next_move():
            """MEDIUM difficulty: test if possible to win next move"""
            for slot in range(9):
                if isinstance(board.xo[slot], int):
                    test_board = Board(board.xo * 1)
                    test_board.xo[slot] = self.mark
                    if test_board.win_check(self.mark):
                        return slot

        def block_next_move():
            """MEDIUM difficulty: test if opponent can win next move and block it"""
            for slot in range(9):
                if isinstance(board.xo[slot], int):
                    test_board = Board(board.xo * 1)
                    test_board.xo[slot] = opponent.mark
                    if test_board.win_check(opponent.mark):
                        return slot

        def minimax(player, temp_board):
            """HARD difficulty: returns best move based on minimax algorithm"""
            empty_slots = temp_board.available_slots()

            # terminal states
            if temp_board.win_check(current_player.mark):
                return 10
            elif temp_board.win_check(opponent.mark):
                return -10
            elif not len(empty_slots):
                return 0

            moves = []
            for slot in empty_slots:
                temp_board.xo[slot] = player.mark
                if player == current_player:
                    value = minimax(opponent, temp_board)
                else:
                    value = minimax(current_player, temp_board)

                temp_board.xo[slot] = 0
                moves.append((slot, value))

            if player == current_player:
                best_value = -666
                for slot, value in moves:
                    if value > best_value:
                        best_value = value
                        player.best_move = slot
                return best_value
            else:
                best_value = 666
                for slot, value in moves:
                    if value < best_value:
                        best_value = value
                        player.best_move = slot
                return best_value


        if self.mode == 'easy':
            return move_random()
        elif self.mode == 'medium':
            winning = win_next_move()
            if winning:
                return winning
            blocking = block_next_move()
            if blocking:
                return blocking
            return move_random()
        elif self.mode == 'hard':
            test_board = Board(board.xo * 1)
            minimax(self, test_board)
            return self.best_move


def intro():
    """intro menu"""
    while True:
        print('\n'*40)
        print('X O X',' '*11,'O X O')
        print('O X O','TIC-TAC-TOE'+' X O X')
        print('X O X',' '*11,'O X O')
        print('\n'*2)
        try:
            user_input = input('Input [P]lay or [Q]uit > ')
            if user_input[0].lower() == 'p':
                return True
            elif user_input[0].lower() == 'q':
                return False
        except Exception:
            print('Invalid input')


def players_menu(name, mark):
    """player can be set as either human or cpu"""
    """IMPLEMENT PRINTING INFORMATION TO THE USER"""
    while True:
        try:
            print('\n\n' + f'Select {name}: ')
            print('[Hu]man')
            print('[E]asy difficulty CPU')
            print('[M]edium difficulty CPU')
            print('[Ha]rd difficulty CPU')
            user_input = input(' > ')
            if user_input[:2].lower() == 'hu':
                return human(mark, 'user')
            elif user_input[0].lower() == 'e':
                return cpu(mark, 'easy')
            elif user_input[0].lower() == 'm':
                return cpu(mark, 'medium')
            elif user_input[:2].lower() == 'ha':
                return cpu(mark, 'hard')
            else:
                print('Invalid input')
        except Exception:
            print('Invalid input')


def swap_players(player):
    """Swap players after their turn"""
    if player == player1:
        return player2, player1
    else:
        return player1, player2


while True:
    # INIT
    active = intro()
    if active:
        player1 = players_menu('player1', 'X')
        player2 = players_menu('player2', 'O')
        current_player, opponent = player1, player2
        board = Board()
        print(board)
    else:
        break

    # START GAMING
    while active:
        # player move
        if isinstance(current_player, cpu):
            print(f'{current_player} making move, level "{current_player.mode}"')
        while True:
            move = current_player.move()
            if isinstance(board.xo[move], int):
                board.xo[move] = current_player.mark
                sleep(0.5)
                break
            else:
                print('This slot is occupied! Choose another one!')

        print(board)

        # winning conditions
        if board.win_check(current_player.mark):
            print(f'{current_player} WINS')
            break
        elif not len(board.available_slots()):
            print('Draw...')
            break

        current_player, opponent = swap_players(current_player)

    input('Press enter to continue ')

print('Thank you for playing !!')
