import random
from board import Board
from abc import ABC, abstractmethod


class Player:
    """
    Tic-Tac-Toe player
    :ivar mark: 'X' or 'O'
    """

    def __init__(self, mark, game):
        self.mark = mark
        self.game = game
        self.board = game.board
        self.opponent = None

    def __str__(self):
        return self.mark


class Human(Player):
    """Human Tic-Tac-Toe player"""

    def move(self):
        """Player moves by inputting coordinate (a number 1-9)."""
        while True:
            try:
                slot = int(input(f'{self.mark}: Enter a slot number > '))
            except Exception:
                print('You should enter a number!')
                continue

            # check if valid coordinate
            if (slot < 1) or (slot > 9):
                print('You should enter a number from 1 to 9!')
            else:
                slot = self.board.slots[slot]
                if self.board.is_slot_available(slot):
                    return slot
                else:
                    print('This slot is occupied! Choose another one!')           


class Cpu(Player, ABC):
    """CPU Tic-Tac-Toe player"""

    best_move = None

    @abstractmethod
    def move(self):
        """
        This is a generic player and assumed to play on easy mode.
        Better instantiate a CPU player of certain difficulty.
        """
        pass

    def move_random(self):
        """
        EASY difficulty: cpu plays randomly
        :return: a random slot
        """
        while True:
            slot = random.choice(list(self.board.slots.keys()))
            slot = self.board.slots[slot]
            if self.board.is_slot_available(slot):
                return slot
    
    def win_next_move(self):
        """
        MEDIUM difficulty: cpu checks if possible to win next move.
        :return: winning slot if available, else None
        """
        for slot in range(9):
            if self.board.is_slot_available(slot):
                test_board = Board(self.board.xo * 1)
                test_board.xo[slot] = self.mark
                if test_board.is_winner(self):
                    return slot

    def block_next_move(self):
        """
        MEDIUM difficulty: cpu checks if opponent can win next move and blocks it
        :return: slot blocking opponent if available, else None
        """
        for slot in range(9):
            if self.board.is_slot_available(slot):
                test_board = Board(self.board.xo * 1)
                test_board.xo[slot] = self.game.opponent.mark
                if test_board.is_winner(self.game.opponent):
                    return slot

    def minimax(self, player, temp_board):
        """
        Minimax algorithm.
        Establishes Cpu.best_move by recursion and backtracking.
        """
        empty_slots = temp_board.available_slots()

        # terminal states
        if temp_board.is_winner(self.game.current_player):
            return 10
        elif temp_board.is_winner(self.game.opponent):
            return -10
        elif not len(empty_slots):
            return 0

        moves = []
        for slot in empty_slots:
            temp_board.xo[slot] = player.mark
            if player == self.game.current_player:
                value = self.minimax(self.game.opponent, temp_board)
            else:
                value = self.minimax(self.game.current_player, temp_board)

            temp_board.xo[slot] = 0
            moves.append((slot, value))

        if player == self.game.current_player:
            best_value = -666
            for slot, value in moves:
                if value > best_value:
                    best_value = value
                    Cpu.best_move = slot
            return best_value
        else:
            best_value = 666
            for slot, value in moves:
                if value < best_value:
                    best_value = value
                    Cpu.best_move = slot
            return best_value


class CpuEasy(Cpu):
    """
    CPU Tic-Tac-Toe player, easy to defeat.
    """

    def move(self):
        """
        Cpu plays a random move.
        :return: a slot to move to.
        """
        print(f'{self} making move, cpu level "easy"')
        return self.move_random()


class CpuMedium(Cpu):
    """
    CPU Tic-Tac-Toe player, medium difficulty.
    """

    def move(self):
        """
        Cpu checks if able to win next move.
        Otherwise, checks if able to block opponent's next move.
        Otherwise, plays a random move.
        :return: a slot to move to.
        """
        print(f'{self} making move, cpu level "medium"')
        winning = self.win_next_move()
        if winning:
            return winning
        blocking = self.block_next_move()
        if blocking:
            return blocking
        return self.move_random()


class CpuHard(Cpu):
    """
    CPU Tic-Tac-Toe player, impossible to defeat.
    """

    def move(self):
        """
        Calculates best possible move based on MiniMax algorithm.
        :return: a slot to move to (Cpu.best_move)
        """
        print(f'{self} making move, cpu level "hard"')
        # if first move, chose one of the corners
        if self.board.is_empty():
            return random.choice([0, 2, 6, 8])
        test_board = Board(self.board.xo * 1)
        self.minimax(self, test_board)
        return Cpu.best_move


def create_player(name, mark, game):
    """
    Menu for creating a Tic-Tac-Toe player whether human or cpu.
    :param name: player's name
    :param mark: player's mark ('X' or 'O')
    :return: a Player object
    """
    while True:
        try:
            print(f'\n\nSelect {name}: ')
            print('[Hu]man')
            print('[E]asy difficulty CPU')
            print('[M]edium difficulty CPU')
            print('[Ha]rd difficulty CPU')
            user_input = input(' > ')
            if user_input[:2].lower() == 'hu':
                return Human(mark, game)
            elif user_input[0].lower() == 'e':
                return CpuEasy(mark, game)
            elif user_input[0].lower() == 'm':
                return CpuMedium(mark, game)
            elif user_input[:2].lower() == 'ha':
                return CpuHard(mark, game)
            else:
                print('Invalid input')
        except Exception:
            print('Invalid input')
