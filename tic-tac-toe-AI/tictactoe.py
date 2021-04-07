
from time import sleep
from board import Board
from player import create_player


class TicTacToe:

    def __init__(self, board=None, p1=None, p2=None):
        self.board = board
        self.player1, self.player2 = p1, p2
        self.current_player, self.opponent = self.player1, self.player2
        self.active = True
    
    def init_players(self):
        self.player1 = create_player('player1', 'X', self)
        self.player2 = create_player('player2', 'O', self)
        self.current_player, self.opponent = self.player1, self.player2
    
    def reset(self):
        self.board = Board()
        self.init_players()
    
    @classmethod
    def display_logo(cls):
        """Prints TicTacToe logo"""
        print('\n'*40)
        print('X O X',' '*11,'O X O')
        print('O X O','TIC-TAC-TOE'+' X O X')
        print('X O X',' '*11,'O X O')
        print('\n'*2)

    def swap_players(self):
        """Swap current player and opponent (use after a turn)."""
        if self.current_player == self.player1:
            self.current_player = self.player2
            self.opponent = self.player1
        else:
            self.current_player = self.player1
            self.opponent = self.player2

    def replay_menu(self):
        """
        Ask user whether to replay or quit.
        :return: boolean
        """
        input('Press enter to continue ')
        while True:
            TicTacToe.display_logo()
            try:
                user_input = input('Input [R]eplay or [Q]uit > ')
                if user_input[0].lower() == 'r':
                    return True
                elif user_input[0].lower() == 'q':
                    print('Thank you for playing !!')
                    return False
            except Exception:
                print('Invalid input')
    
    def check_gamestate(self):
        """Check if game has a winner, is a draw, or continue"""
        if self.board.is_winner(self.current_player):
            print(f'{self.current_player} WINS')
            self.active = False
        elif not len(self.board.available_slots()):
            print('Draw...')
            self.active = False

    def play(self):
        """Run this method to start the game."""
        self.display_logo()
        while self.active:
            # initialize
            self.reset()
            print(self.board)
            # start gameplay
            while self.active:
                move = self.current_player.move()
                self.board.xo[move] = self.current_player.mark
                print(self.board)
                self.check_gamestate()
                self.swap_players()
            # ask to replay or quit
            self.active = self.replay_menu()
